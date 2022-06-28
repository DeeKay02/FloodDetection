# FloodDetection
“Sensor for rise is Water Level for Flood Indication” is an simple system which keeps close watch over the water level to predict a flood and send emergency notification, so we can embrace ourselves forcaution, to minimize the damage caused by the flood.

The system has WIFI connectivity, thus its collected data can be accessed from anywhere quite easily using IoT.

A solution to this problem is making use of the advanced IoT available in this world. The IoT device we have in mind are sensors. we decided to place sensors at certain positions above the river bank and when it reaches a threshold height it will set off an alarm and send SMS messages to everyone around the area to which the sensor is registered.

Utilising the Internet of Things and the APIs available we have created a system that can help
in such a situation to send alerts before the possibility of a flood.

When the circuit is powered on, the device will keep passing the real-time data that is being sensed by the IoT system set up in a post, a few meters above the rivers, any water bodies or areas which can be a source of causing floods, to the cloud and once the Water Level is noticed to be above the given limit which is set based on the environment, it will send an alert by turning on the piezo buzzer and will also alert the respective people regarding the same via an SMS which will be triggered by an API call.

The Arduino measures the water level using the ultrasonic sensor and sends it to serial and if the water level is less than the threshold, then the buzzer will also be triggered.

The Python code in the cloud takes the water level data from the Arduino’s serial port and checks the threshold and if the water level is less than the threshold, a message will be sent to the given mobile number by calling the Twilio API.

   ![Picture1](https://user-images.githubusercontent.com/48171972/176244232-5f89133d-ee98-427b-99ee-7eaa3ff79a39.png)<br/>
                             The above image is the circuit implemented.<br/><br/>
                           ![image](https://user-images.githubusercontent.com/48171972/176244407-d104fd1b-1b55-44da-b0ff-5e0bb323ae0a.png)

Since the range of an Ultrasonic sensor used for experimenting can measure only short distance, the threshold has been set as 30cm. When implementing in large scale, much powerful sensor with other sensors for more confirmations can be used
