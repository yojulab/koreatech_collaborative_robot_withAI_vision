from pymycobot import MechArm
import time
from ultralytics import YOLO
import cv2

mc = MechArm('COM5', 115200) 

model = YOLO('best2.pt')

###### 움직임 함수 #######
def initial_pose():
    mc.send_angles([0,0,0,0,0,0], 50)

def position1():
    mc.send_angles([11.6, 32.87, -13.0, 6.15, 64.86, -66.0], 40)
    time.sleep(1.2)
    mc.set_basic_output(5, 0)
    time.sleep(4)
    mc.send_angles([12.12, -2.46, -12.91, 0.0, 69.96, -66.0], 40)
    time.sleep(1.2)
    mc.send_angles([22.5, -6.41, 3.86, -8.34, 41.66, -61.52], 40)

def position2():
    mc.send_angles([21.62, 21.26, 9.14, 1.14, 67.23, -58.79], 40)
    time.sleep(1.2)
    mc.set_basic_output(5, 0)
    time.sleep(4)
    mc.send_angles([22.32, -2.46, -10.19, -0.26, 78.22, -59.41], 40)
    time.sleep(1.2)
    mc.send_angles([22.5, -6.41, 3.86, -8.34, 41.66, -61.52], 40)

def move_green():
    initial_pose()
    mc.send_angles([-62.92, 44.2, -30.32, -2.1, 76.37, -68.73], 40)
    time.sleep(1.2)
    mc.set_basic_output(5, 1)
    time.sleep(4)
    initial_pose()

def move_error():
    initial_pose()
    mc.send_angles([27.86, 76.55, -79.18, 7.55, 58.71, -83.67], 40)
    time.sleep(1.2)
    mc.set_basic_output(5, 1)
    time.sleep(4)
    initial_pose()

###### YOLO 모델 사용 #######
def detect(cap):
    ret, frame = cap.read()
    if not ret:
        print("FRAME ERROR")
        return None
    
    results = model.predict(frame, conf=0.3, verbose=False)
    boxes = results[0].boxes
    
    if boxes is not None and len(boxes) > 0:
        class_ids = boxes.cls.cpu().numpy()
    else:
        return None

#### Main 함수 #######
def main():
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("FRAME ERROR")
        return 
    
    position1()
    time.sleep(1)
    
    result = detect(cap) # YOLO 모델 사용 및 결과 확인 
    
    if result == 0:
        print("RESULT: NORMAL")
        move_green()
    elif result == 1:
        print("RESULT: ERROR")
        move_error()
    else:
        print("NOT DETECTED")

    cap.release()
    
if __name__ == '__main__':
    main()
