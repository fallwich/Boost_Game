#!/usr/bin/env python3
from __future__ import print_function
from dust_service.srv import station, stationResponse
import requests
from bs4 import BeautifulSoup
import rospy
class Get_dust():
    def __init__(self):
        print("클라이언트 노드에 도시명을 입력하세요.")

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
        # print(self.stationName)
        # self.station_find=self.stationName.index('봉산동')

    def get_station(self, req):
        self.get_dust()
        self.station = req.a
        self.station_find = self.stationName.index(self.station)
        print("station: %s"%(self.stationName[self.station_find]))
        print("pm10: %d"%int(self.pm10Value[self.station_find]))
        print("pm25: %d"%int(self.pm25Value[self.station_find]))
        # return AddTwoIntsResponse(self.station_find)
        # print("Returning [%s + %s = %s]"%(req.a, req.b, (req.a + req.b)))
        return stationResponse(req.a)

    def dust_server(self):
        rospy.init_node('dust_server')
        s = rospy.Service('dust_node', station, self.get_station)
        rospy.spin()


if __name__ == '__main__':
    try:
        dust = Get_dust()
        dust.dust_server()
    except rospy.ROSInterruptException:
        pass
