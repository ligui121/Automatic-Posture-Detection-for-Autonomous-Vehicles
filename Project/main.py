import time
import math
import requests
from mpu6050 import mpu6050
import RPi.GPIO as GPIO

# GPIO 引脚定义
# L298N 控制引脚
IN1 = 5
IN2 = 6
IN3 = 13
IN4 = 19
ENA = 23  # PWM 控制 Motor A
ENB = 24  # PWM 控制 Motor B

# 蜂鸣器引脚
BUZZER_PIN = 17

# MPU6050 配置
MPU6050_ADDR = 0x68

# ThingSpeak 配置（可选，如果需要上传数据）
THINGSPEAK_API_KEY = 'GEDQKFKGBUVWOV3H'
THINGSPEAK_URL = 'https://api.thingspeak.com/update'

# 设定倾斜角度阈值
PITCH_THRESHOLD = 30.0  # 俯仰角度阈值，单位为度
ROLL_THRESHOLD = 30.0   # 横滚角度阈值，单位为度

# 初始化 GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)
GPIO.setup(ENA, GPIO.OUT)
GPIO.setup(ENB, GPIO.OUT)
GPIO.setup(BUZZER_PIN, GPIO.OUT)

# 初始化 PWM
pwm_a = GPIO.PWM(ENA, 100)  # 频率 100Hz
pwm_b = GPIO.PWM(ENB, 100)  # 频率 100Hz
pwm_a.start(0)
pwm_b.start(0)

# 初始化 MPU6050
sensor = mpu6050(MPU6050_ADDR)

GPIO.output(BUZZER_PIN, GPIO.HIGH)

def set_motor(left_speed, right_speed, direction='forward'):
    """
    控制电机的方向和速度
    left_speed 和 right_speed 的范围为 0-100
    direction: 'forward', 'backward', 'left', 'right', 'stop'
    """
    if direction == 'backward':
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)
    elif direction == 'forward':
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)
    elif direction == 'left':
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.HIGH)
        GPIO.output(IN3, GPIO.HIGH)
        GPIO.output(IN4, GPIO.LOW)
    elif direction == 'right':
        GPIO.output(IN1, GPIO.HIGH)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.HIGH)
    elif direction == 'stop':
        GPIO.output(IN1, GPIO.LOW)
        GPIO.output(IN2, GPIO.LOW)
        GPIO.output(IN3, GPIO.LOW)
        GPIO.output(IN4, GPIO.LOW)

    pwm_a.ChangeDutyCycle(left_speed)
    pwm_b.ChangeDutyCycle(right_speed)

def activate_buzzer():
    GPIO.output(BUZZER_PIN, GPIO.LOW)

def deactivate_buzzer():
    GPIO.output(BUZZER_PIN, GPIO.HIGH)

def calculate_orientation(accel_data):
    ax = accel_data['x']
    ay = accel_data['y']
    az = accel_data['z']

    # 计算俯仰角（Pitch）和横滚角（Roll）
    pitch = math.atan2(ax, math.sqrt(ay * ay + az * az)) * 180 / math.pi
    roll = math.atan2(ay, math.sqrt(ax * ax + az * az)) * 180 / math.pi
    return pitch, roll

def upload_to_thingspeak(pitch, roll, temp):
    params = {
        'api_key': THINGSPEAK_API_KEY,
        'field1': pitch,
        'field2': roll,
        'field3': temp
    }
    try:
        response = requests.get(THINGSPEAK_URL, params=params)
        if response.status_code == 200:
            print("数据已上传到 ThingSpeak")
        else:
            print("上传失败，状态码:", response.status_code)
    except Exception as e:
        print("上传异常:", e)

def read_and_control():
    accel_data = sensor.get_accel_data()
    pitch, roll = calculate_orientation(accel_data)
    temp = sensor.get_temp()

    print(f"Pitch: {pitch:.2f}°, Roll: {roll:.2f}°, Temperature: {temp:.2f}°C")
    # 上传数据到 ThingSpeak（可选）
    if THINGSPEAK_API_KEY != '你的Write API Key':  # 确保 API Key 已替换
        upload_to_thingspeak(pitch, roll, temp)

    # 根据姿态角控制小车
    if abs(pitch) > PITCH_THRESHOLD or abs(roll) > ROLL_THRESHOLD:
        print("检测到倾斜，停止小车并激活蜂鸣器！")
        set_motor(0, 0, 'stop')  # 停止小车
        activate_buzzer()        # 激活蜂鸣器
    else:
        deactivate_buzzer()      # 关闭蜂鸣器
        # 控制小车前进（可根据需要修改运动模式）
        set_motor(50, 50, 'forward')  # 设置速度和方向

if __name__ == "__main__":
    print("开始运行小车控制程序...\n")
    try:
        while True:
            read_and_control()
            time.sleep(1)  # 根据需要调整循环间隔
    except KeyboardInterrupt:
        print("停止程序")
    finally:
        set_motor(0, 0, 'stop')        # 停止小车
        deactivate_buzzer()            # 关闭蜂鸣器
        pwm_a.stop()
        pwm_b.stop()
        GPIO.cleanup()                 # 清理 GPIO 资源
