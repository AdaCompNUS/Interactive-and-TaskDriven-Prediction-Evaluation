cmake_minimum_required(VERSION 2.8.3)
project(gamma_planner)

find_package(catkin REQUIRED COMPONENTS
  rospy
  std_msgs
  geometry_msgs
  nav_msgs
)

catkin_package(
  CATKIN_DEPENDS 
  rospy 
  std_msgs 
  geometry_msgs
  nav_msgs
  msg_builder 
)

include_directories(
  ${catkin_INCLUDE_DIRS}
)
