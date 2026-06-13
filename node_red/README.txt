====================================================
Node-RED Dashboard
====================================================

Purpose:
Real-time monitoring of smart waste bins.

Features:

• MQTT Integration
• HiveMQ Cloud Connectivity
• Fill Percentage Gauge
• Temperature Gauge
• Humidity Gauge
• Gas Level Gauge
• Alert Notifications
• Bin Status Display
• Fill Level Trend Chart

Data Flow:

ESP32 / Simulation
        ↓
      MQTT
        ↓
   HiveMQ Cloud
        ↓
    Node-RED
        ↓
Dashboard Widgets

Topic Used:

smartbin/+/data

Dashboard Components:

1. Fill Percentage Gauge
2. Temperature Gauge
3. Humidity Gauge
4. Gas Level Gauge
5. Current Status
6. Alerts Panel
7. Fill Trend Chart