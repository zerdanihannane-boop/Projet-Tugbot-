PROJET TUGBOT - COMMANDES DE LANCEMENT

Terminal 1 : lancer la simulation Gazebo

source /opt/ros/jazzy/setup.bash
source ~/projet_robotique/install/setup.bash
ros2 launch tugbot_gazebo tugbot_depot.launch.py


Terminal 2 : lancer le bridge ROS2-Gazebo

source /opt/ros/jazzy/setup.bash
source ~/projet_robotique/install/setup.bash
ros2 launch tugbot_gazebo ign_ros2_bridge.launch.py


Terminal 3 : lancer le robot autonome

source /opt/ros/jazzy/setup.bash
source ~/projet_robotique/install/setup.bash
python3 ~/projet_robotique/src/tugbot_gazebo/scripts/avoid_tugbot.py


Terminal 4 : lancer RViz

source /opt/ros/jazzy/setup.bash
source ~/projet_robotique/install/setup.bash
rviz2

Dans RViz :
Fixed Frame = base_link

Ajouter LaserScan avant :
/world/world_demo/model/tugbot/link/scan_front/sensor/scan_front/scan

Ajouter LaserScan arrière :
/world/world_demo/model/tugbot/link/scan_back/sensor/scan_back/scan

Ajouter PointCloud2 :
/world/world_demo/model/tugbot/link/scan_omni/sensor/scan_omni/scan/points

Ajouter Image caméra :
/world/world_demo/model/tugbot/link/camera_front/sensor/color/image
