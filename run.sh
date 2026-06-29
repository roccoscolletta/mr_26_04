xhost +local:root
 
echo "Avvio del container ROS 2..."
docker run -it \
    --net=host \
    --env="DISPLAY" \
    --env="QT_X11_NO_MITSHM=1" \
    --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw" \
    --volume="$(pwd)/ros_ws:/ros2_ws" \
    --name="ros2_maze_container" \
    --rm \
    ros2_maze_explorer bash