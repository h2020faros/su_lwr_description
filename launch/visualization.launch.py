from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import PathJoinSubstitution, LaunchConfiguration
from launch_ros.substitutions import FindPackageShare
from launch_ros.actions import Node

def generate_launch_description():

    rviz_config_file = PathJoinSubstitution([FindPackageShare(LaunchConfiguration('description_package')), LaunchConfiguration('rviz_config')])
    
    return LaunchDescription([
        DeclareLaunchArgument(
            name='description_package',
            default_value='lwr_description',
            description='Description package.'
        ),
        DeclareLaunchArgument(
            name='rviz_config',
            default_value='config/lwr_default.rviz',
            description='Rviz configuration relative to description_package.'
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            arguments=['-d', rviz_config_file],
            output='screen')
        ])
        
