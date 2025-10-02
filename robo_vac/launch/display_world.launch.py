from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os

from ament_index_python.packages import get_package_share_directory

def generate_launch_description():

    package_name='robo_vac'

    pkg_path = get_package_share_directory(package_name)
    world_path = os.path.join(pkg_path, 'worlds', 'small_house.world')

    return LaunchDescription([
        ExecuteProcess(
            cmd=['gazebo', '--verbose', world_path],
            output='screen'),
    ])
