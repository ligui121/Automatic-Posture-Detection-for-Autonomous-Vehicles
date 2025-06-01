# 🚗 ESE 525 Project — Automatic Posture Detection using MPU6050 in a Demo Car

This project demonstrates the application of the **MPU6050** sensor for **real-time posture detection** in an autonomous vehicle prototype. Built as part of the **ESE 525: Modern Sensors in AI Applications** course at Stony Brook University, this system integrates **accelerometer** and **gyroscope** data to monitor and adjust the vehicle's orientation in real time.

## 📌 Course Info

- **Course**: ESE 525 – Modern Sensors in AI Applications  
- **Semester**: Fall 2024  
- **Instructors**: L. Shterengas, R. Kamoua, M. Stanacevic  
- **Team Members**:  
  - Guoao Li – [guoao.li@stonybrook.edu](mailto:guoao.li@stonybrook.edu)  
  - Haotian Fu – [haotian.fu@stonybrook.edu](mailto:haotian.fu@stonybrook.edu)

---

## 🧠 Project Overview

The goal of this project is to design and build a demo car equipped with an MPU6050 sensor for detecting roll, pitch, and yaw. The system utilizes a **Raspberry Pi 4**, an **L298N motor driver**, and a **buzzer** for alert signaling. Sensor readings are processed to dynamically adjust the car’s orientation during operation.

Key features:

- Real-time attitude estimation using sensor fusion
- Edge computing on Raspberry Pi
- Low-cost, power-efficient design
- 3D-printed chassis for prototyping

---

## 🔧 System Architecture

### Components

| Type           | Component        |
|----------------|------------------|
| MCU            | Raspberry Pi 4   |
| Sensor         | MPU6050 IMU      |
| Actuator       | L298N Motor Driver, Buzzer |
| Communication  | I2C (MPU6050), UART (Buzzer) |
| Power          | 9V Battery       |

### Data Flow

MPU6050 → Raspberry Pi 4 → Motor Driver (via PWM) → Motors → Buzzer (via UART)

---

## 🧪 Features & Capabilities

- **Orientation Tracking**: Real-time detection of roll, pitch, yaw
- **Digital Motion Processor (DMP)**: Offloads sensor fusion from Pi
- **Stability Control**: Adjusts movement based on posture changes
- **Noise Compensation**: Accurate data in stable temperature conditions
- **Compact & Efficient**: Ideal for educational prototyping

---

## 🛠️ Hardware & Manufacturing

- **Chassis**: Designed in Shapr3D and printed using Bambu Lab A1
- **Mounting**: Hot glue and screws ensure stability
- **Materials**: Flexible and low-cost plastic

---

## 🧪 Testing & Results

- Posture change detection accuracy: **>95%**
- Performance verified on:
  - Flat and inclined terrains
  - Dynamic maneuvers with >30° attitude shifts
- Real-time data logging and adjustment during operation
- Power-efficient operation with reliable uptime

---

## 📁 Repository Structure
.
├── code/
│ └── main.py
├── model/
│ └── Demo.3mf
├── ESE525Abstract.pdf
├── ESE525Report.pdf
└── README.md

---

## 🚀 How to Run

1. Clone the repo
2. Upload the code to your Raspberry Pi 4.
3. Connect the MPU6050 via I2C.
4. Run `main.py` to begin posture detection and motor control.

> Ensure all GPIO and power connections are correct before powering the prototype.

---

## 📎 References

- MPU6050 Datasheet  
- Sugihara, T., *Motion Control Using Accelerometers and Gyroscopes*, Journal of Robotics and Automation, 2019  
- [MPU6050 GitHub Libraries](https://github.com/jeelabs/MPU6050-arduino)

---

## 🙏 Acknowledgments

We thank our professors for their invaluable guidance, and the support of our families and peers throughout the project.

---

