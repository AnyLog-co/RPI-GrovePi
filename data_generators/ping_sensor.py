"""
The following is data is based on historical data generated by Lite San Leandro for Ping
"""
import datetime
import random 
import string
import uuid

PING_DATA = {
        'ADVA FSP3000R7': {
            'parentelement': '62e71893-92e0-11e9-b465-d4856454f4ba',
            'webid': 'F1AbEfLbwwL8F6EiShvDV-QH70AkxjnYuCS6RG0ZdSFZFT0ugnMRtEzvxdFojNpadLPwI4gWE9NUEFTUy1MSVRTTFxMSVRTQU5MRUFORFJPXDc3NyBEQVZJU1xQT1AgUk9PTVxBRFZBIEZTUDMwMDBSN3xQSU5H',
            'min_value': 0,
            'max_value': 4
        },
        'Ubiquiti OLT': {
            'parentelement': 'd515dccb-58be-11ea-b46d-d4856454f4ba',
            'webid': 'F1AbEfLbwwL8F6EiShvDV-QH70Ay9wV1b5Y6hG0bdSFZFT0ugxACfpGU7d1ojPpadLPwI4gWE9NUEFTUy1MSVRTTFxMSVRTQU5MRUFORFJPXDc3NyBEQVZJU1xQT1AgUk9PTVxVQklRVUlUSSBPTFR8UElORw',
            'min_value': 0,
            'max_value': 49
        },
        'VM Lit SL NMS': {
            'parentelement': '1ab3b14e-93b1-11e9-b465-d4856454f4ba',
            'webid': 'F1AbEfLbwwL8F6EiShvDV-QH70ATrGzGrGT6RG0ZdSFZFT0ugQW05a2rwdFojNpadLPwI4gWE9NUEFTUy1MSVRTTFxMSVRTQU5MRUFORFJPXDc3NyBEQVZJU1xQT1AgUk9PTVxGLk8gTU9OSVRPUklORyBTRVJWRVJcVk0gTElUIFNMIE5NU3xQSU5H',
            'min_value': 0,
            'max_value': 11
        },
        'Catalyst 3500XL': {
            'parentelement': '68ae8bef-92e1-11e9-b465-d4856454f4ba',
            'webid': 'F1AbEfLbwwL8F6EiShvDV-QH70A74uuaOGS6RG0ZdSFZFT0ug4FckGTrxdFojNpadLPwI4gWE9NUEFTUy1MSVRTTFxMSVRTQU5MRUFORFJPXDc3NyBEQVZJU1xQT1AgUk9PTVxDQVRBTFlTVCAzNTAwWEx8UElORw',
            'min_value': 0,
            'max_value': 49
        },
        'GOOGLE_PING': {
            'parentelement': 'f0bd0832-a81e-11ea-b46d-d4856454f4ba',
            'webid': 'F1AbEfLbwwL8F6EiShvDV-QH70AMgi98B6o6hG0bdSFZFT0ugPdQ3gcXLd1ojPpadLPwI4gWE9NUEFTUy1MSVRTTFxMSVRTQU5MRUFORFJPXDc3NyBEQVZJU1xHT09HTEVfUElOR3xQSU5H',
            'min_value': 2,
            'max_value': 37
        },
}

def get_ping_data(frequency:float)->dict: 
   """
   Generate dict forr ping_data  
   :args: 
      frequency:float - multiplication of generated value 
   :param: 
      timestamp:str
      device_name:str
      parentelement:str 
      webiid:str - str 
      min/max value:int - value range to get value from 
   :sample: 
      {
         "device_name": "Catalyst 3500XL",
         "parentelement": "68ae8bef-92e1-11e9-b465-d4856454f4ba",
         "timestamp": "2020-12-08 02:20:11.024002",
         "value": 1,
         "webid": "F1AbEfLbwwL8F6EiShvDV-QH70A74uuaOGS6RG0ZdSFZFT0ug4FckGTrxdFojNpadLPwI4gWE9NUEFTUy1MSVRTTFxMSVRTQU5MRUFORFJPXDc3NyBEQVZJU1xQT1AgUk9PTVxDQVRBTFlTVCAzNTAwWEx8UElORw"
      }
   :return: 
      data dict based on information generated by PING_DATA 
   """
   timestamp = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f') 
   device_name = random.choice(list(PING_DATA.keys()))
   parentelement = PING_DATA[device_name]['parentelement'] 
   webid = PING_DATA[device_name]['webid'] 
   value = random.choice(range(PING_DATA[device_name]['min_value'], PING_DATA[device_name]['max_value'])) * frequency 

   data = {
      'timestamp': timestamp, 
      'device_name': device_name, 
      'parentelement': parentelement, 
      'webid': webid, 
      'value': value
   } 

   return data

