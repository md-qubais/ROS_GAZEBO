# TurtleBot3 Reactive Control in Gazebo

This project implements a reactive control system for the TurtleBot3 robot in ROS and Gazebo. The robot moves forward and stops when an obstacle is detected using LiDAR data.

## Features
- Simple control script to move the robot forward and stop when obstacles are detected.
- Fully automated ROS + Gazebo setup.
- Reactive behavior based on sensor input from `/scan` topic.

## Requirements
- Ubuntu 20.04 with ROS Noetic.
- Gazebo 11.
- TurtleBot3 simulation packages.

## Installation

### Step 1: Install ROS Noetic and TurtleBot3
1. Install ROS Noetic (if not already installed):
   sudo apt update
   sudo apt install ros-noetic-desktop-full -y


2. Install TurtleBot3 simulation packages:
   sudo apt install ros-noetic-turtlebot3-gazebo ros-noetic-turtlebot3-description ros-noetic-turtlebot3-teleop -y

3. Set the TURTLEBOT3_MODEL environment variable:
    echo "export TURTLEBOT3_MODEL=burger" >> ~/.bashrc\
    source ~/.bashrc


### Step 2: Clone the Repository
    git clone https://github.com/<your-username>/turtlebot3_reactive_control.git
    cd turtlebot3_reactive_control

### Step 3: Run the project
Terminal 1: Start ROS Core 
        roscore
Terminal 2: Launch Gazebo
        roslaunch turtlebot3_gazebo turtlebot3_empty_world.launch
Terminal 3: Run the Reactive Control Script
        python3 reactive_control.py

### Step 4: Place obstacles in front of the TurtleBot3 in Gazebo, and observe its behavior.


