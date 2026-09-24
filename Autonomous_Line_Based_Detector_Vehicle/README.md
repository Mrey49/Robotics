# ROBOTRACE: Autonomous Vision-Based Line Follower

A ROS 2 and Gazebo-based autonomous line-following robot that uses a forward-facing RGB camera and OpenCV for visual navigation.

The robot detects the track from camera images, calculates its position relative to the image center, and uses proportional control to steer along the line. It also includes line-loss recovery, marker detection, lap counting, and automatic stopping after lap completion.

## Features

- OpenCV-based line detection
- ROI-based image processing
- Contour and centroid detection
- Proportional steering control
- Line-loss recovery
- Lap marker detection
- Lap counting
- Automatic lap completion and safe shutdown
- Gazebo simulation with a differential-drive robot
- ROS 2 camera and velocity control

## Build

```bash
cd ~/25b3976_Sor_Project
colcon build
source install/setup.bash
```

## Running the Project

### SOR Track

Open a separate terminal for each step.

**Terminal 1: Launch the Gazebo track and robot**

```bash
cd ~/25b3976_Sor_Project
source install/setup.bash
ros2 launch follower sor_track.launch.py
```

**Terminal 2: Run the follower node**

```bash
cd ~/25b3976_Sor_Project
source install/setup.bash
ros2 run follower follower
```

**Terminal 3: Start the follower**

```bash
cd ~/25b3976_Sor_Project
source install/setup.bash
ros2 service call /start_follower std_srvs/srv/Empty
```

## Expected Result

The robot should autonomously detect and follow the track, recover when the line is temporarily lost, detect lap markers, complete the lap, and stop safely.
