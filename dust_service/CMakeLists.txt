cmake_minimum_required(VERSION 3.0.2)
project(dust_service)

find_package(catkin REQUIRED COMPONENTS
  message_generation
  rospy
  std_msgs
)

# Generate services in the 'srv' folder
add_service_files(
  FILES
  station.srv
)

generate_messages(
  DEPENDENCIES
  std_msgs
)

catkin_package(
#  INCLUDE_DIRS include
 LIBRARIES dust_service
 CATKIN_DEPENDS   rospy std_msgs std_msgs message_runtime
#  DEPENDS system_lib
)

catkin_install_python(PROGRAMS scripts/dust_client.py scripts/dust_server.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)