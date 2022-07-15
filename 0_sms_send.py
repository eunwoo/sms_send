# -*- coding: utf-8 -*-
import requests
import json
import os
import certifi

# print(certifi.where())
# print('SSL Error. Adding custom certs to Certifi store...')
# cafile = certifi.where()
# with open('certicate.pem', 'rb') as infile:
#         customca = infile.read()
# with open(cafile, 'ab') as outfile:
#         outfile.write(customca)


send_url = 'https://apis.aligo.in/send/' # 요청을 던지는 URL, 현재는 문자보내기
sender = os.environ.get(
        "SENDER_NUMBER"
        )  # 보내는 번호 => 현재 지영님 폰 번호만 인증이 되어서 다른 번호는 사용 불가
phone_list = ["010-3562-9501"]
print(phone_list)
phone_list = list(map(lambda x: x.replace("-", ""), phone_list))
print(phone_list)
content = "시험문자"
# ================================================================== 문자 보낼 때 필수 key값
# API key, userid, sender, receiver, msg
# API키, 알리고 사이트 아이디, 발신번호, 수신번호, 문자내용

# sms_data={'key': 'apikey', #api key
#         'userid': 'aligo_id', # 알리고 사이트 아이디
#         'sender': 'sender', # 발신번호
#         'receiver': '01000000000', # 수신번호 (,활용하여 1000명까지 추가 가능)
#         'msg': '%고객명% test', #문자 내용 
#         'msg_type' : 'msg_type', #메세지 타입 (SMS, LMS)
#         'title' : 'title', #메세지 제목 (장문에 적용)
#         'destination' : '01000000000|홍길동', # %고객명% 치환용 입력
#         #'rdate' : '예약날짜',
#         #'rtime' : '예약시간',
#         #'testmode_yn' : '' #테스트모드 적용 여부 Y/N
# }
sms_data = {
        "key": "axngr7ld8l3ng1qteoidm66axvjdlmdu",  # api key
        "userid": "jjy1229",  # 알리고 사이트 아이디
        "sender": sender,  # 발신번호
        "receiver": ",".join(phone_list),  # 수신번호 (,활용하여 1000명까지 추가 가능)
        "msg": content,  # 문자 내용
        "msg_type": "LMS",  # 메세지 타입 (SMS, LMS)
        "title": "[T-QEMS 알림] T-QEMS 알림 안내",  # 메세지 제목 (장문에 적용)
        # 'destination' : '01000000000|홍길동', # %고객명% 치환용 입력
}

send_response = requests.post(send_url, data=sms_data)
print (send_response.json())
