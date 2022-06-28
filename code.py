import conf
from boltiot import Sms, Bolt
import json, time

threshold = 30

mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)
response = mybolt.serialRead('10')
print(response)

while True: 
    print ("Reading sensor value")
    mybolt.serialWrite("GetAnalogData")
    response = mybolt.serialRead(10)
    data = json.loads(response) 
    print("Sensor value is: " + str(data['value']))
    try:
        sensor_value = int(data['value'])
        if  sensor_value < threshold:
            print("Making request to Twilio to send a SMS")
            response = sms.send_sms("The Water level from ground is " +str(sensor_value) + " indicating the possibility of floods.")
            print("Response received from Twilio is: " + str(response))
            print("Status of SMS at Twilio is :" + str(response.status))
    except Exception as e: 
        print ("Error occured: Below are the details")
        print (e)
    time.sleep(10)
