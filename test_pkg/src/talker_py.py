#!/usr/bin/env python3	# 파이썬을 쓴다면 반드시 달아주자
#-*- coding:utf-8 -*-	# 한글 주석을 달기 위해 사용한다.
import requests
from bs4 import BeautifulSoup
import rospy				# ROS 라이브러리
from test_pkg.msg import test_msg	# 패키지의 메시지 파일
from indy_utils import indydcp_client as client
from indy_utils.indy_program_maker import JsonProgramComponent
class Get():
    def __init__(self):
        rospy.init_node('talker', anonymous=True)
        #'anonymous=True' 인수는 동일한 이름을 가진 여러 노드가 ROS 네트워크에 존재하는 경우 이름에 임의의 문자열을 추가하여 고유한 이름을 부여하도록 지정합니다.
        self.pub = rospy.Publisher('dust', test_msg, queue_size=10)
        self.rate = rospy.Rate(5) # 10hz
        self.msg = test_msg()	# 메시지 변수 선언
        self.count = 0	

    def get_dust(self):
        URL = "http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty"
        SERVICE_PARAM = '?serviceKey='
        SERVICE_KEY='gQj%2BcdJTZwGMhLPNhJuDPOptupzoJL7D9hJlIp6kzxp9DdqlCXxMtCPgJm%2F8kUAy0IgX0pQ5WqfgsQB26RIlVA%3D%3D'
        TYPE_PARAM = '&returnType=xml'
        ITEMS="&numOfRows=120"
        PAGE_NUM="&pageNo=1"
        # SIDONAME="&sidoName=서울"
        SIDONAME="&sidoName=경기"
        VERSION='&ver=1.0'
        URL=URL+SERVICE_PARAM+SERVICE_KEY+TYPE_PARAM+ITEMS+PAGE_NUM+SIDONAME+VERSION 
        res = requests.get(URL)
        soup = BeautifulSoup(res.text,'html.parser')
        soup.findAll('item')
        item_list = soup.findAll('item')
        self.stationName=[]
        self.pm10Value=[]
        self.pm25Value=[]
        for item in item_list:
            self.stationName.append(item.find('stationname').text)
            self.pm10Value.append(item.find('pm10value').text)
            self.pm25Value.append(item.find('pm25value').text)
        # self.station_find=self.stationName.index('봉산동')
def main():
    try:
        dust = Get()
        dust.get_dust()
        print("Input station name\n")
        station = input()
        print(type(station))
        station_find = dust.stationName.index(station)
        print(station_find)
        # robot_ip = "192.168.0.5"    # 예시 STEP IP 주소
        # robot_name = "NRMK-Indy7"   # IndyRP2의 경우 "NRMK-IndyRP2"
        # indy = client.IndyDCPClient(robot_ip, robot_name) # indy 객체 생성
        # indy.connect()
        # status = indy.get_robot_status()
        # print(status)
    except:
        print("Again")
        station = input()
        
        station_find = dust.stationName.index(station)
    else:
        while not rospy.is_shutdown():
            dust.get_dust()
            dust.msg.station = dust.stationName[station_find]
            dust.msg.dust = int(dust.pm10Value[station_find])
            rospy.loginfo("station: %s", dust.msg.station)
            dust.pub.publish(dust.msg)
            dust.rate.sleep()

if __name__ == '__main__':
    try:
        main()
    except rospy.ROSInterruptException:
        pass