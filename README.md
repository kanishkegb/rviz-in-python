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
  - git clone https://github.com/kanishkegb/rviz-in-python.git
- Else
  - download the zip file
  - extract the file
  - copy and paste the extracted 'rviz-in-python-master' inside ~/rviz_ws/src

## Running
- cd to workspace: cd ~/rviz_ws
- if running for the first time, make the package: catkin_make
- give permission: chmod 777 src/rviz-in-python/plot_cube.py
