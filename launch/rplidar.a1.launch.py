import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():


    falkor_rplidar_cfgs = os.path.join(
        get_package_share_directory("rplidar_ros"),
        "params",
        "rplidar_conf.yaml"
    )
    
    
    rpLiDAR_node = Node(
        package="rplidar_ros",
        executable="rplidar_node",
        name="lidar",
        namespace="falkor",
        parameters=[falkor_rplidar_cfgs],
        #arguments=['--ros-args', '--log-level', "DEBUG"],
        output={
            "stdout": "screen",
            "stderr": "screen",#"log",
        }
    )
    
   
    ld= LaunchDescription([])
    
    ld.add_action(rpLiDAR_node)
    
    return ld