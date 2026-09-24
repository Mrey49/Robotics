import rclpy
from rclpy.node import Node

from sensor_msgs.msg import Image
from geometry_msgs.msg import Twist
from cv_bridge import CvBridge

import cv2
import numpy as np
import threading


class ImageSubscriber(Node):

    def __init__(self):
        super().__init__('image_subscriber')

        # Subscribe to camera
        self.subscription = self.create_subscription(
            Image,
            'camera/image',
            self.image_callback,
            1
        )

        # Publisher for robot movement
        self.publisher = self.create_publisher(
            Twist,
            'cmd_vel',
            10
        )

        self.bridge = CvBridge()

        # Latest camera frame
        self.latest_frame = None
        self.frame_lock = threading.Lock()

        # Control flag
        self.running = True

        # Stop when ball becomes sufficiently large
        self.STOP_AREA = 15000

        # Start ROS spinning in a separate thread
        self.spin_thread = threading.Thread(
            target=self.spin_thread_func,
            daemon=True
        )
        self.spin_thread.start()

    # ---------------------------------------------------------
    # ROS SPIN THREAD
    # ---------------------------------------------------------

    def spin_thread_func(self):
        while rclpy.ok() and self.running:
            rclpy.spin_once(self, timeout_sec=0.05)

    # ---------------------------------------------------------
    # CAMERA CALLBACK
    # ---------------------------------------------------------

    def image_callback(self, msg):
        try:
            frame = self.bridge.imgmsg_to_cv2(
                msg,
                "bgr8"
            )

            with self.frame_lock:
                self.latest_frame = frame.copy()

        except Exception as e:
            self.get_logger().error(
                f"Image conversion error: {e}"
            )

    # ---------------------------------------------------------
    # DISPLAY LOOP
    # ---------------------------------------------------------

    def display_image(self):

        cv2.namedWindow(
            "frame",
            cv2.WINDOW_NORMAL
        )

        cv2.resizeWindow(
            "frame",
            800,
            600
        )

        while rclpy.ok() and self.running:

            frame = None

            with self.frame_lock:
                if self.latest_frame is not None:
                    frame = self.latest_frame.copy()
                    self.latest_frame = None

            if frame is not None:

                mask, contour, crosshair = self.process_image(
                    frame
                )

                result = self.add_small_pictures(
                    frame,
                    [mask, contour, crosshair]
                )

                cv2.imshow(
                    "frame",
                    result
                )

            key = cv2.waitKey(1) & 0xFF

            if key == ord('q'):
                self.running = False
                break

        cv2.destroyAllWindows()

    # ---------------------------------------------------------
    # IMAGE PROCESSING
    # ---------------------------------------------------------

    def process_image(self, img):

        msg = Twist()

        # Default: robot stopped
        msg.linear.x = 0.0
        msg.linear.y = 0.0
        msg.linear.z = 0.0

        msg.angular.x = 0.0
        msg.angular.y = 0.0
        msg.angular.z = 0.0

        rows, cols = img.shape[:2]

        # -----------------------------------------------------
        # RED COLOR DETECTION
        # -----------------------------------------------------

        R, G, B = self.convert2rgb(img)

        redMask = self.threshold_binary(
            R,
            (220, 255)
        )

        # Remove small noise
        kernel = np.ones(
            (5, 5),
            np.uint8
        )

        redMask = cv2.morphologyEx(
            redMask,
            cv2.MORPH_OPEN,
            kernel
        )

        redMask = cv2.morphologyEx(
            redMask,
            cv2.MORPH_CLOSE,
            kernel
        )

        # -----------------------------------------------------
        # CREATE DISPLAY MASKS
        # -----------------------------------------------------

        stackedMask = np.dstack(
            (
                redMask,
                redMask,
                redMask
            )
        )

        contourMask = stackedMask.copy()
        crosshairMask = stackedMask.copy()

        # -----------------------------------------------------
        # FIND CONTOURS
        # -----------------------------------------------------

        contours, hierarchy = cv2.findContours(
            redMask.copy(),
            cv2.RETR_EXTERNAL,
            cv2.CHAIN_APPROX_NONE
        )

        if len(contours) > 0:

            # Largest red object
            c = max(
                contours,
                key=cv2.contourArea
            )

            area = cv2.contourArea(c)

            print(
                f"\rBall Area: {area:.0f}",
                end="",
                flush=True
            )

            # -------------------------------------------------
            # CENTROID
            # -------------------------------------------------

            M = cv2.moments(c)

            if M["m00"] != 0:

                cx = int(
                    M["m10"] / M["m00"]
                )

                cy = int(
                    M["m01"] / M["m00"]
                )

            else:

                cx = 0
                cy = 0

            # -------------------------------------------------
            # DRAW CONTOUR
            # -------------------------------------------------

            cv2.drawContours(
                contourMask,
                [c],
                -1,
                (0, 255, 0),
                3
            )

            cv2.circle(
                contourMask,
                (cx, cy),
                8,
                (0, 255, 0),
                -1
            )

            # -------------------------------------------------
            # DRAW CROSSHAIRS
            # -------------------------------------------------

            cv2.line(
                crosshairMask,
                (cx, 0),
                (cx, rows),
                (0, 0, 255),
                3
            )

            cv2.line(
                crosshairMask,
                (0, cy),
                (cols, cy),
                (0, 0, 255),
                3
            )

            # Camera center
            center_x = int(cols / 2)

            cv2.line(
                crosshairMask,
                (center_x, 0),
                (center_x, rows),
                (255, 0, 0),
                3
            )

            # -------------------------------------------------
            # STOP IF BALL IS CLOSE
            # -------------------------------------------------

            if area > self.STOP_AREA:

                msg.linear.x = 0.0
                msg.angular.z = 0.0

                cv2.putText(
                    crosshairMask,
                    "STOP - BALL CLOSE",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (0, 255, 0),
                    2
                )

            # -------------------------------------------------
            # CHASE THE BALL
            # -------------------------------------------------

            else:

                error = center_x - cx

                # Ball is not centered
                if abs(error) > 20:

                    msg.linear.x = 0.0

                    if error > 0:

                        # Ball is to the left
                        msg.angular.z = 0.2

                    else:

                        # Ball is to the right
                        msg.angular.z = -0.2

                # Ball is approximately centered
                else:

                    msg.linear.x = 0.2
                    msg.angular.z = 0.0

                cv2.putText(
                    crosshairMask,
                    f"Error: {error}",
                    (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    0.8,
                    (255, 255, 255),
                    2
                )

        else:

            # No ball detected
            msg.linear.x = 0.0
            msg.angular.z = 0.0

            cv2.putText(
                crosshairMask,
                "NO BALL",
                (20, 40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.8,
                (0, 0, 255),
                2
            )

        # -----------------------------------------------------
        # PUBLISH ROBOT COMMAND
        # -----------------------------------------------------

        self.publisher.publish(msg)

        return (
            redMask,
            contourMask,
            crosshairMask
        )

    # ---------------------------------------------------------
    # BGR -> RGB CHANNELS
    # ---------------------------------------------------------

    def convert2rgb(self, img):

        R = img[:, :, 2]
        G = img[:, :, 1]
        B = img[:, :, 0]

        return R, G, B

    # ---------------------------------------------------------
    # THRESHOLD
    # ---------------------------------------------------------

    def threshold_binary(
        self,
        img,
        thresh=(200, 255)
    ):

        binary = np.zeros_like(img)

        binary[
            (img >= thresh[0]) &
            (img <= thresh[1])
        ] = 1

        return binary * 255

    # ---------------------------------------------------------
    # COMBINE SMALL IMAGES
    # ---------------------------------------------------------

    def add_small_pictures(
        self,
        img,
        small_images,
        size=(160, 120)
    ):

        # Make a copy so original camera image is untouched
        result = img.copy()

        height, width = result.shape[:2]

        small_width = size[0]
        small_height = size[1]

        # Resize main image if necessary so three
        # 160px images always fit safely.
        required_width = (
            40 +
            3 * small_width +
            2 * 40
        )

        required_height = max(
            height,
            small_height + 20
        )

        if width < required_width:

            new_width = required_width

            scale = new_width / width

            new_height = int(
                height * scale
            )

            result = cv2.resize(
                result,
                (new_width, new_height)
            )

            height, width = result.shape[:2]

        # -----------------------------------------------------
        # PLACE SMALL IMAGES
        # -----------------------------------------------------

        x_offset = 40
        y_offset = 10

        for small in small_images:

            # Resize
            small = cv2.resize(
                small,
                size
            )

            # Convert grayscale -> BGR
            if len(small.shape) == 2:

                small = cv2.cvtColor(
                    small,
                    cv2.COLOR_GRAY2BGR
                )

            # Make sure dimensions match
            if (
                y_offset + small_height <= height
                and
                x_offset + small_width <= width
            ):

                result[
                    y_offset:
                    y_offset + small_height,

                    x_offset:
                    x_offset + small_width
                ] = small

            x_offset += (
                small_width + 40
            )

        return result

    # ---------------------------------------------------------
    # STOP NODE
    # ---------------------------------------------------------

    def stop(self):

        self.running = False

        if self.spin_thread.is_alive():

            self.spin_thread.join(
                timeout=1.0
            )


# =============================================================
# MAIN
# =============================================================

def main(args=None):

    print(
        "OpenCV version: %s"
        % cv2.__version__
    )

    rclpy.init(args=args)

    node = ImageSubscriber()

    try:

        node.display_image()

    except KeyboardInterrupt:

        pass

    finally:

        node.stop()

        # Publish stop command before shutting down
        stop_msg = Twist()

        stop_msg.linear.x = 0.0
        stop_msg.angular.z = 0.0

        node.publisher.publish(
            stop_msg
        )

        node.destroy_node()

        rclpy.shutdown()


if __name__ == '__main__':
    main()
