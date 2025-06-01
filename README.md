# Autonomous Posture-Detecting Vehicle with MPU6050

This project demonstrates a posture-aware autonomous vehicle prototype using the MPU6050 sensor and Raspberry Pi 4. It detects and responds to changes in orientation (pitch and roll) using real-time motion tracking, motor control, and an alert system.

## 🧠 Project Overview

- **Course:** ESE 525 - Modern Sensors in AI Applications  
- **Team Members:** Guoao Li, Haotian Fu  
- **Instructor:** Prof. L. Shterengas, R. Kamoua, M. Stanacevic  
- **Semester:** Fall 2024  
- **Hardware:** MPU6050, Raspberry Pi 4, L298N Motor Driver, Buzzer  
- **Software:** Python (with GPIO and mpu6050 libraries)  
- **Link:** [GitHub Repository](https://github.com/Haotian-Fu/ESE525Project.git)

## ⚙️ Features

- Real-time orientation monitoring using 6-axis MPU6050 (pitch & roll)
- Automatic stopping and buzzer alert when threshold angles are exceeded
- PWM-based motor control for autonomous motion
- Optional upload to [ThingSpeak](https://thingspeak.com/) for IoT data logging

## 🏗 System Architecture

- **MPU6050**: Measures acceleration & gyroscope data
- **Raspberry Pi 4**: Central controller, processes sensor data and manages actuation
- **L298N Motor Driver**: Controls two motors based on Raspberry Pi commands
- **Buzzer**: Activates on unsafe tilt angles
- **Python Script**: `main.py` handles sensing, decision-making, and actuation

## 🔩 Hardware Setup

| Component        | Description                        |
|------------------|------------------------------------|
| MPU6050 Sensor   | 6-axis IMU via I2C                 |
| Raspberry Pi 4   | Main microcontroller               |
| L298N Module     | Motor driver for DC motors         |
| Buzzer           | Alert mechanism via GPIO           |
| Power Supply     | 9V battery for motors              |

## 🧪 Core Logic (`main.py`)

- **Orientation Calculation** using trigonometric functions
- **Threshold Detection** at 30° pitch or roll
- **Control Flow**:
  - If angle exceeds threshold → stop motors + activate buzzer
  - Else → resume forward motion + deactivate buzzer
- **ThingSpeak API Integration** (optional): pitch, roll, and temperature logging

## 🚀 Getting Started

### Requirements

- Python 3
- Raspberry Pi OS
- Install dependencies:
```bash
pip install mpu6050-raspberrypi RPi.GPIO requests
