import os
from glob import glob
from setuptools import setup
 
package_name = 'maze_bot'
 
setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        # Queste due righe dicono a ROS 2 di copiare le cartelle worlds e launch!
        (os.path.join('share', package_name, 'worlds'), glob('worlds/*.sdf')),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='studente',
    maintainer_email='studente@todo.todo',
    description='Pacchetto per esplorazione labirinto con TurtleBot3',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            # Qui in futuro metteremo i tuoi nodi Python (es. il navigatore APF)
        ],
    },
)
 