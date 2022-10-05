import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration, PythonExpression

def generate_launch_description():

    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource([os.path.join(
            get_package_share_directory('lwr_description'),
            'launch',
            'lwr_upload.launch.py')
            ]),
        ),
        DeclareLaunchArgument(
            name='robot_ns',
            default_value='/',
            description='Robot namespace.'
        ),
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='world_ns_connector',
            namespace=LaunchConfiguration('robot_ns'),
            arguments=["0 0 0 0 0 0 /world ",PythonExpression(['\'',LaunchConfiguration('robot_ns'),'/world\''])]
        ),
        Node(
            package='robot_state_publisher',
            executable='robot_state_publisher',
            name='robot_state_publisher',
            namespace=LaunchConfiguration('robot_ns'),
            output='screen',
            parameters=[{
                'robot_description': LaunchConfiguration('robot_description'),
                'publish_frequency': 100.,
                'frame_prefix': LaunchConfiguration('robot_ns'),
            }]
        ),
        Node(
            package='joint_state_publisher_gui',
            executable='joint_state_publisher_gui',
            name='joint_state_publisher',
            namespace=LaunchConfiguration('robot_ns'),
            output='screen',
            parameters=[{
                'robot_description': LaunchConfiguration('robot_description'),
                'use_gui':True,
                'publish_default_velocities':True,
                'publish_default_efforts':True,
                'rate': 100,
            }]
        ),
        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            # arguments=['-d', rviz_config_file],
            output='screen')
        ])
        
