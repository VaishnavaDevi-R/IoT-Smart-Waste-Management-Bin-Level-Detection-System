====================================================
Smart Waste Management Circuit Connections
====================================================

ESP32 Connections

HC-SR04 Ultrasonic Sensor
-----------------------------------
VCC  -> 5V
GND  -> GND
TRIG -> GPIO 5
ECHO -> GPIO 18

DHT22 Temperature & Humidity Sensor
-----------------------------------
VCC  -> 3.3V
GND  -> GND
DATA -> GPIO 4

MQ135 Gas Sensor
-----------------------------------
VCC  -> 5V
GND  -> GND
AOUT -> GPIO 34

Communication
-----------------------------------
ESP32 -> WiFi -> HiveMQ Cloud

Data Flow
-----------------------------------
Sensors
   ↓
ESP32
   ↓
MQTT
   ↓
HiveMQ Cloud
   ↓
Node-RED Dashboard
   ↓
Python Subscriber
   ↓
SQLite Database
   ↓
Streamlit Dashboard