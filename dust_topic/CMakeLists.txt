cmake_minimum_required(VERSION 3.0.2)
project(dust_topic)

find_package(catkin REQUIRED COMPONENTS
  roscpp
  rospy
  std_msgs
  message_generation
)

# add_message_files의 주석을 풀고 수정한다.
add_message_files(
  FILES
  dust_msg.msg
)

# generate_messages의 주석을 푼다.
generate_messages(
  DEPENDENCIES
  std_msgs
)

# LIBRARIES, CATKIN_DEPENDS의 주석을 풀고, message_runtime을 추가한다.
catkin_package(
#  INCLUDE_DIRS include
  LIBRARIES dust_topic
  CATKIN_DEPENDS roscpp rospy std_msgs message_runtime
#  DEPENDS system_lib
)

# 주석을 풀고 스크립트 이름을 입력한다. talker_py.py, listener.py를 파이썬으로 사용한다는 이야기
catkin_install_python(PROGRAMS
  src/talk.py
  src/listen.py
  # src/indy_utils/indy_program_maker.py
  # src/indy_utils/indydcp_client.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION} #
)#DESTINATION: 이 키워드는 Python 스크립트가 설치될 패키지 구조 내의 대상 위치를 지정합니다.
#${CATKIN_PACKAGE_BIN_DESTINATION}: ROS 패키지 내 바이너리 파일의 대상 위치를 나타내는 Catkin 변수입니다. 
#이 변수를 사용하면 Python 스크립트가 적절한 바이너리 위치(일반적으로 lib/<package_name>)에 설치됩니다.