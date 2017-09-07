# RVIZ in Python
This is an attempt to learn how to use different markers in RVIZ with Python. I
wanted to do this with Python and could not find a better/simpler tutorial to
do this anywhere. This repository will include each and every step I followed
while learning. The plan is to update this while I learn.

## Install ROS

## Create a workspace (if needed)
- mkdir -p ~/rviz_ws/src
- cd rviz_ws/
- catkin_make

## Get this repository
- If you use git:
  - cd src
  - git clone https://github.com/kanishkegb/rviz_in_python.git
- Else
  - download the zip file
  - extract the file
  - copy and paste the extracted 'rviz-in-python-master' inside ~/rviz_ws/src

## Running
- cd to workspace: cd ~/rviz_ws
- if running for the first time, make the package: catkin_make
- make the file an executable: chmod +x src/rviz_in_python/plot_cube.py
- source: . devel/setup.bash
- run roscore: roscore
- run: rosrun rviz_in_python plot_cube.py
- run RVIZ: rosrun rviz rviz
