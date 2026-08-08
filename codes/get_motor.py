# from ultralytics import YOLO

# if __name__ == '__main__':
#     model = YOLO('yolo26n.pt')
    
#     # GPU에서 학습 진행 시 사용 
#     results = model.train(data='data.yaml', 
#                           epochs=200,
#                           batch=4,
#                           lr0=0.01,
#                           imgsz=640,
#                           pretrained=True, 
#                           device=0) 
    # CPU만 장착되어 있는 PC에서 학습 시, device=0 삭제 후 코드 구동 
    
    
from pymycobot import MechArm
import time
import keyboard

mc = MechArm('COM5', 115200)    
    
###### 모터의 각도 값 가져오기 ########
while True:
    angles = mc.get_angles()
    print("각도: ", angles)
    time.sleep(3)
    
    # 's' 키를 누르면 서보 모터 해제 
    if keyboard.is_pressed('s'):
        mc.release_all_servos()
        print("서보모터를 해제합니다.")
    
    # 'a' 키를 누르면 서보 모터 활성화 
    if keyboard.is_pressed('a'):
        print("모든 서보를 활성화합니다.")
        mc.power_on()
