import json 
import requests 

def validate_connection(conn:str)->bool: 
   """
   Validate node is accessible
   :args: 
      conn:str - connection string 
   :param:
      boolean:bool - boolean status 
   :return: 
      if node is accessible return True, else return False 
   """
   boolean = False 
   try:
      r = requests.get('http://%s' % conn, headers={'type': 'info', 'details': 'get status'})
   except Exception as e: 
      print(e) 

   if 'running' in r.json()['Status']:
      boolean=True  
   return boolean 


def send_data(payloads:list, conn:str, dbms:str, table_name:str, rest_format:str):
    """
    Send payload to node via REST 
    :args: 
        payloads:dict - data to store in database 
        conn:str - connection string 
        dbms:str - logical database to store data in 
        table_name:str - logical table to store data in 
        rest_format:str - format by which to send data via REST 
    :param:
        header:dict - REST PUT header info        
    """
    header = { 
        'type': 'json', 
        'dbms': dbms, 
        'table': table_name,
        'mode': rest_format, 
        'Content-Type': 'text/plain'
    }

    for payload in payloads: 
        json_payload = json.dumps(payload) 
        try: 
            requests.put('http://%s' % conn, headers=header, data=json_payload)
        except Exception as e:
            print(e) 
            
