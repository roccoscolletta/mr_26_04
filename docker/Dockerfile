# Usa l'immagine ufficiale di ROS 2 Jazzy con interfaccia grafica
FROM ros:jazzy
 
# Installa gli strumenti necessari, Gazebo Harmonic e il bridge ROS-GZ
RUN apt-get update && apt-get install -y \
    nano \
    python3-pip \
    python3-colcon-common-extensions \
    ros-jazzy-ros-gz \
    ros-jazzy-navigation2 \
    ros-jazzy-nav2-bringup \
    ros-jazzy-slam-toolbox \
    ros-jazzy-cv-bridge \
    ros-jazzy-vision-opencv \
    ros-jazzy-image-transport \
    libopencv-dev \
    python3-opencv \
    && rm -rf /var/lib/apt/lists/*
 
# Imposta la cartella di lavoro principale nel container
WORKDIR /ros2_ws
 
# Comando avviato di default
CMD ["bash"]