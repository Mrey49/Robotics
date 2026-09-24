import os
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PathJoinSubstitution, Command
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    pkg = get_package_share_directory('erc_sor_ros_session1')

    rviz_launch_arg = DeclareLaunchArgument(
        'rviz',
        default_value='true',
        description='Open RViz.'
    )

    world_arg = DeclareLaunchArgument(
        'world',
        default_value='empty.sdf',
        description='World file'
    )

    model_arg = DeclareLaunchArgument(
        'model',
        default_value='mogi_bot.urdf',
        description='Robot model'
    )

    urdf_file_path = PathJoinSubstitution([
        pkg,
        'urdf',
        LaunchConfiguration('model')
    ])

    world_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(pkg, 'launch', 'world.launch.py')
        ),
        launch_arguments={
            'world': LaunchConfiguration('world')
        }.items()
    )

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        output='screen',
        parameters=[
            {
                'robot_description': Command(
                    ['xacro', ' ', urdf_file_path]
                ),
                'use_sim_time': True
            }
        ]
    )

    spawn_urdf_node = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name', 'mogi_bot',
            '-topic', 'robot_description',
            '-x', '0.0',
            '-y', '0.0',
            '-z', '0.2'
        ],
        output='screen'
    )

    gz_bridge_node = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/clock@rosgraph_msgs/msg/Clock[gz.msgs.Clock',
            '/cmd_vel@geometry_msgs/msg/Twist@gz.msgs.Twist',
            '/odom@nav_msgs/msg/Odometry@gz.msgs.Odometry',
        ],
        output='screen'
    )

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        arguments=['-d', os.path.join(pkg, 'rviz', 'rviz.rviz')],
        condition=IfCondition(LaunchConfiguration('rviz')),
        parameters=[{'use_sim_time': True}]
    )

    ld = LaunchDescription()

    ld.add_action(rviz_launch_arg)
    ld.add_action(world_arg)
    ld.add_action(model_arg)

    ld.add_action(world_launch)
    ld.add_action(robot_state_publisher_node)
    ld.add_action(spawn_urdf_node)
    ld.add_action(gz_bridge_node)
    ld.add_action(rviz_node)

    return ld
