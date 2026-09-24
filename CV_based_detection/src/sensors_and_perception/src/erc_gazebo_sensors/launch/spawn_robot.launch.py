import os

from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
    TimerAction
)
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import (
    LaunchConfiguration,
    PathJoinSubstitution,
    Command
)
from launch_ros.actions import Node

from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    # =========================================================
    # PACKAGE
    # =========================================================

    pkg_erc_gazebo_sensors = get_package_share_directory(
        'erc_gazebo_sensors'
    )

    # =========================================================
    # GAZEBO MODEL PATH
    # =========================================================

    gazebo_models_path = os.path.expanduser(
        '~/sor_ws/src/sensors_and_perception/gazebo_models'
    )

    os.environ['GZ_SIM_RESOURCE_PATH'] = (
        gazebo_models_path
        + os.pathsep
        + os.environ.get('GZ_SIM_RESOURCE_PATH', '')
    )

    # =========================================================
    # ARGUMENTS
    # =========================================================

    rviz_arg = DeclareLaunchArgument(
        'rviz',
        default_value='true',
        description='Open RViz'
    )

    world_arg = DeclareLaunchArgument(
        'world',
        default_value='home.sdf',
        description='Gazebo world'
    )

    model_arg = DeclareLaunchArgument(
        'model',
        default_value='erc_bot.urdf',
        description='Robot model'
    )

    # =========================================================
    # ROBOT URDF
    # =========================================================

    urdf_file_path = PathJoinSubstitution([
        pkg_erc_gazebo_sensors,
        'urdf',
        LaunchConfiguration('model')
    ])

    # =========================================================
    # GAZEBO WORLD
    # =========================================================

    world_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                pkg_erc_gazebo_sensors,
                'launch',
                'world.launch.py'
            )
        ),
        launch_arguments={
            'world': LaunchConfiguration('world')
        }.items()
    )

    # =========================================================
    # RVIZ
    # =========================================================

    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        arguments=[
            '-d',
            os.path.join(
                pkg_erc_gazebo_sensors,
                'rviz',
                'rviz.rviz'
            )
        ],
        condition=IfCondition(
            LaunchConfiguration('rviz')
        ),
        parameters=[
            {
                'use_sim_time': True
            }
        ],
        output='screen'
    )

    # =========================================================
    # ROBOT SPAWN
    # =========================================================

    spawn_robot_node = Node(
        package='ros_gz_sim',
        executable='create',
        arguments=[
            '-name',
            'erc_bot',

            '-topic',
            'robot_description',

            '-x',
            '2.5',

            '-y',
            '1.5',

            '-z',
            '0.0',

            '-Y',
            '-1.5707'
        ],
        output='screen',
        parameters=[
            {
                'use_sim_time': True
            }
        ]
    )

    # =========================================================
    # ROBOT STATE PUBLISHER
    # =========================================================

    robot_state_publisher_node = Node(
        package='robot_state_publisher',
        executable='robot_state_publisher',
        name='robot_state_publisher',
        output='screen',

        parameters=[
            {
                'robot_description': Command([
                    'xacro',
                    ' ',
                    urdf_file_path
                ]),
                'use_sim_time': True
            }
        ],

        remappings=[
            ('/tf', 'tf'),
            ('/tf_static', 'tf_static')
        ]
    )

    # =========================================================
    # JOINT STATE PUBLISHER
    # =========================================================

    joint_state_publisher_gui_node = Node(
        package='joint_state_publisher_gui',
        executable='joint_state_publisher_gui',
        output='screen'
    )

    # =========================================================
    # RED BALL
    # =========================================================

    red_ball_model = os.path.join(
        gazebo_models_path,
        'red_ball_10in',
        'model.sdf'
    )

    spawn_ball_node = Node(
        package='ros_gz_sim',
        executable='create',

        arguments=[
            '-name',
            'red_ball',

            '-file',
            red_ball_model,

            # These are the coordinates you confirmed
            # give the correct camera alignment and distance.
            '-x',
            '2.5',

            '-y',
            '-1.5',

            '-z',
            '0.13'
        ],

        output='screen'
    )

    # Wait for Gazebo to start before spawning ball
    delayed_ball_spawn = TimerAction(
        period=5.0,
        actions=[
            spawn_ball_node
        ]
    )

    # =========================================================
    # LAUNCH DESCRIPTION
    # =========================================================

    return LaunchDescription([

        rviz_arg,

        world_arg,

        model_arg,

        world_launch,

        rviz_node,

        robot_state_publisher_node,

        spawn_robot_node,

        joint_state_publisher_gui_node,

        delayed_ball_spawn
    ])
