# Red Ball Chasing Robot — ROS 2

This project implements a simulated mobile robot in ROS 2 and Gazebo that uses its RGB camera to detect a red ball using OpenCV and autonomously move towards it.

The robot receives camera data from Gazebo, processes the image using OpenCV to locate the red ball, and generates velocity commands to steer the robot towards the ball.

The simulation uses a custom Gazebo environment with the ERC robot and a red ball.

## Requirements

- ROS 2 Jazzy
- Gazebo Sim
- OpenCV
- ROS–Gazebo Bridge
- colcon

## Setup
```bash
cd ~/sor_ws
colcon build
source install/setup.bash
```
## Run

### 1. Gazebo

Launches the simulator and spawns the robot.

```bash
ros2 launch erc_gazebo_sensors spawn_robot.launch.py
```

### 2. ROS-Gazebo Bridge

Forwards the camera image, velocity commands and simulation clock between Gazebo and ROS 2.

```bash
ros2 run ros_gz_bridge parameter_bridge \
/camera/image@sensor_msgs/msg/Image@gz.msgs.Image \
/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist \
/clock@rosgraph_msgs/msg/Clock@gz.msgs.Clock
```

### 3. OpenCV

Runs the node that detects the red ball and chases it.

```bash
ros2 run erc_gazebo_sensors_py chase_the_ball
```
