# Assignment 3: ROS 2 Gazebo Teleoperation

A ROS 2 and Gazebo project featuring a differential-drive robot with caster wheels and terminal-based keyboard teleoperation.

## Features

- Differential-drive robot simulation
- Front and rear caster wheels
- Gazebo simulation environment
- ROS 2 control through `/cmd_vel`
- Keyboard-based teleoperation using `teleop_twist_keyboard`
- ROS-Gazebo communication

## Run

Open a separate terminal for each step.

### Terminal 1: Launch Gazebo

```bash
cd ~/sor_ws
source install/setup.bash
ros2 launch erc_sor_ros_session1 spawn_robot.launch.py
```

### Terminal 2: Start Teleoperation

```bash
source ~/sor_ws/install/setup.bash
ros2 run teleop_twist_keyboard teleop_twist_keyboard
```

Use the keyboard commands provided by `teleop_twist_keyboard` to move the robot.

## Result

The robot can be spawned in Gazebo and controlled remotely through ROS 2 terminal-based keyboard teleoperation.
