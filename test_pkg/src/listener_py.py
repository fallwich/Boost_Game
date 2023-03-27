#!/usr/bin/env python3
#-*- coding:utf-8 -*- 

import rospy
from test_pkg.msg import test_msg

# 퍼블리셔 노드로부터 토픽을 받아들이는 콜백 함수
def callback(dust):
    rospy.loginfo("pm10: %d", dust.dust)    
def main():
    # 노드 초기화. 이름은 listener
    rospy.init_node('listener', anonymous=True)

    # 토픽 callback이라는 이름의 함수로 받아들이며, 메시지 타입은 test_msg
    rospy.Subscriber("dust", test_msg, callback)

    rospy.spin()
 
if __name__ == '__main__':
    main()