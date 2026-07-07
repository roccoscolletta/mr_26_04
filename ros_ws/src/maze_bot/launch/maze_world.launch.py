import os
 
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, SetEnvironmentVariable
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
 
def generate_launch_description():
    # Percorsi
    turtlebot3_gazebo_dir = get_package_share_directory('turtlebot3_gazebo')
    ros_gz_sim_dir = get_package_share_directory('ros_gz_sim')
    maze_bot_dir = get_package_share_directory('maze_bot')
    
    # Argomenti
    x_pose = LaunchConfiguration('x_pose', default='0.0')
    y_pose = LaunchConfiguration('y_pose', default='0.0')
    use_sim_time = LaunchConfiguration('use_sim_time', default='true')
    
    # Percorso del mondo
    world_path = os.path.join(maze_bot_dir, 'worlds', 'maze.sdf')
 
    # Forza la variabile d'ambiente per il TurtleBot3 direttamente da Python
    set_model_env = SetEnvironmentVariable('TURTLEBOT3_MODEL', 'waffle')
    
    # 1. Lancia Gazebo con il mondo
    gz_sim = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(ros_gz_sim_dir, 'launch', 'gz_sim.launch.py')
        ),
        launch_arguments=[('gz_args', ['-r -v4 ', world_path])]
    )
    
    # 2. Robot State Publisher 
    robot_state_publisher = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(turtlebot3_gazebo_dir, 'launch', 'robot_state_publisher.launch.py')
        ),
        launch_arguments=[('use_sim_time', use_sim_time)]
    )
    
    # 3. Spawn del TurtleBot3
    spawn_turtlebot = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(turtlebot3_gazebo_dir, 'launch', 'spawn_turtlebot3.launch.py')
        ),
        launch_arguments=[
            ('x_pose', x_pose),
            ('y_pose', y_pose)
        ]
    )
 
    # 4. Bridge (ros_gz_bridge) - SOLO SENSORI E COMANDI
    bridge_node = Node(
        package='ros_gz_bridge',
        executable='parameter_bridge',
        arguments=[
            '/scan@sensor_msgs/msg/LaserScan[gz.msgs.LaserScan',
            '/odom@nav_msgs/msg/Odometry[gz.msgs.Odometry',
            '/cmd_vel@geometry_msgs/msg/Twist]gz.msgs.Twist',
        ],
        output='screen'
    )
    
    # 5. Avvio di RViz2
    rviz_config_dir = os.path.join(maze_bot_dir, 'rviz', 'maze_bot.rviz')
    
    rviz_node = Node(
        package='rviz2',
        executable='rviz2',
        name='rviz2',
        arguments=['-d', rviz_config_dir],
        parameters=[{'use_sim_time': use_sim_time}],
        output='screen'
    )
 
    return LaunchDescription([
        set_model_env,
        gz_sim,
        robot_state_publisher,
        spawn_turtlebot,
        bridge_node,
        rviz_node,
    ])