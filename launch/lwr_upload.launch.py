
import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import Command, FindExecutable, LaunchConfiguration

### Generate robot description ###
def generate_launch_description():
    #Robot description from xacro
    robot_description = Command(
        [
            FindExecutable(name="xacro"), " ",
            os.path.join(
                get_package_share_directory('lwr_description'),
                "robots",
                "kuka_lwr.urdf.xacro"
            ), " ",
            "robot_name:=", LaunchConfiguration('robot_name'), " ",
            "load_base:=", LaunchConfiguration('load_base'), " ",
            "load_ati_sensor:=", LaunchConfiguration('load_ati_sensor'), " ",
            "load_calib_tool:=", LaunchConfiguration('load_calib_tool'), " ",
            "load_handle:=", LaunchConfiguration('load_handle'), " ",
            "load_laser:=", LaunchConfiguration('load_laser'), " ",
            "load_weight:=", LaunchConfiguration('load_weight'), " ",
            "load_head_cam:=", LaunchConfiguration('load_head_cam'), " ",
            "load_screwdriver:=", LaunchConfiguration('load_screwdriver'), " ",
            "load_table:=", LaunchConfiguration('load_table'), " ",
            "load_gazebo_ros_control:=", LaunchConfiguration('load_gazebo_ros_control')
        ]
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            name='robot_name',
            default_value='lwr',
            description='Set robot name.'
        ),
        DeclareLaunchArgument(
            name='load_base',
            default_value='false',
            description='Load base.'
        ),
        DeclareLaunchArgument(
            name='load_ati_sensor',
            default_value='false',
            description='Load ATI sensor.'
        ),
        DeclareLaunchArgument(
            name='load_calib_tool',
            default_value='false',
            description='Load calib tool.'
        ),
        DeclareLaunchArgument(
            name='load_handle',
            default_value='false',
            description='Load handle.'
        ),
        DeclareLaunchArgument(
            name='load_laser',
            default_value='false',
            description='Load laser.'
        ),
        DeclareLaunchArgument(
            name='load_weight',
            default_value='false',
            description='Load weight.'
        ),
        DeclareLaunchArgument(
            name='load_head_cam',
            default_value='false',
            description='Load head cam.'
        ),
        DeclareLaunchArgument(
            name='load_screwdriver',
            default_value='false',
            description='Load screwdriver.'
        ),
        DeclareLaunchArgument(
            name='load_table',
            default_value='false',
            description='Load table.'
        ),
        DeclareLaunchArgument(
            name='load_gazebo_ros_control',
            default_value='false',
            description='Load Gazebo ROS control.'
        ),
        DeclareLaunchArgument(
            name='robot_description',
            default_value=robot_description,
            description='Description of IIWA Med7 at SU.'
        )
        ])
        
