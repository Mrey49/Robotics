from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                PathJoinSubstitution([
                    FindPackageShare("urdf_launch"),
                    "launch",
                    "display.launch.py"
                ])
            ),
            launch_arguments={
                "urdf_package": "erc_sor_ros_session1",
                "urdf_package_path": "urdf/mogi_bot.urdf",
                "jsp_gui": "true"
            }.items()
        )
    ])
