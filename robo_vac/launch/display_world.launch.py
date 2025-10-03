import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory


def generate_launch_description():

    # Declare a launch argument for the world file
    world_arg = DeclareLaunchArgument(
        "world",
        default_value=os.path.join(
            get_package_share_directory("turtlebot3_gazebo"),
            "worlds",
            "turtlebot3_world.world"
        ),
        description="Full path to the world file to load"
    )

    world_path = LaunchConfiguration("world")

    # Include Gazebo launch (standard launch file)
    gazebo_launch_file = os.path.join(
        get_package_share_directory("gazebo_ros"),
        "launch",
        "gazebo.launch.py"
    )

    gazebo = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(gazebo_launch_file),
        launch_arguments={"world": world_path}.items(),
    )

    # Spawn TurtleBot3 Waffle from SDF (avoids robot_description issue)
    spawn_turtlebot = Node(
        package="gazebo_ros",
        executable="spawn_entity.py",
        arguments=[
            "-entity", "turtlebot3_waffle",
            "-file", os.path.join(
                get_package_share_directory("turtlebot3_gazebo"),
                "models", "turtlebot3_waffle_pi", "model.sdf"
            )
        ],
        output="screen"
    )

    return LaunchDescription([
        world_arg,
        gazebo,
        spawn_turtlebot
    ])
