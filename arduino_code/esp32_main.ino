/*
====================================================
IoT Smart Waste Management System
Predictive Bin Monitoring using ESP32
====================================================

Hardware Components:
- ESP32
- HC-SR04 Ultrasonic Sensor
- DHT22 Temperature & Humidity Sensor
- MQ135 Gas Sensor

Communication:
- MQTT Protocol
- HiveMQ Cloud

Author:
Vaishnava Devi

====================================================
*/

#include <WiFi.h>
#include <PubSubClient.h>
#include <DHT.h>

#define TRIG_PIN 5
#define ECHO_PIN 18

#define DHTPIN 4
#define DHTTYPE DHT22

#define MQ135_PIN 34

DHT dht(DHTPIN, DHTTYPE);

const char* ssid = "YOUR_WIFI";
const char* password = "YOUR_PASSWORD";

const char* mqtt_server = "YOUR_HIVEMQ_SERVER";

WiFiClient espClient;
PubSubClient client(espClient);

void setup()
{
    Serial.begin(115200);

    pinMode(TRIG_PIN, OUTPUT);
    pinMode(ECHO_PIN, INPUT);

    dht.begin();

    WiFi.begin(ssid, password);

    while (WiFi.status() != WL_CONNECTED)
    {
        delay(500);
        Serial.print(".");
    }

    client.setServer(mqtt_server, 1883);

    Serial.println("Connected");
}

void loop()
{
    float temperature = dht.readTemperature();
    float humidity = dht.readHumidity();

    int gasLevel = analogRead(MQ135_PIN);

    long duration;
    float distance;

    digitalWrite(TRIG_PIN, LOW);
    delayMicroseconds(2);

    digitalWrite(TRIG_PIN, HIGH);
    delayMicroseconds(10);

    digitalWrite(TRIG_PIN, LOW);

    duration = pulseIn(ECHO_PIN, HIGH);

    distance = duration * 0.034 / 2;

    Serial.println("Smart Bin Data");

    Serial.print("Distance: ");
    Serial.println(distance);

    Serial.print("Temperature: ");
    Serial.println(temperature);

    Serial.print("Humidity: ");
    Serial.println(humidity);

    Serial.print("Gas Level: ");
    Serial.println(gasLevel);

    delay(5000);
}