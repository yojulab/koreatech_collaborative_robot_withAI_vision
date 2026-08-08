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

mc = MechArm('COM9', 115200)    
    
import time
import keyboard

# 현재 로봇 팔의 모드 상태를 저장하는 변수 (기본값 설정)
current_mode = "활성화 상태(Active)"

###### 모터의 각도 값 가져오기 ########
while True:
    angles = mc.get_angles()
    
    # print 문에 현재 모드(mode) 표시 추가
    print(f"[현재 모드: {current_mode}] 각도: {angles}")
    
    time.sleep(3)
    
    # 's' 키를 누르면 서보 모터 해제 
    if keyboard.is_pressed('s'):
        mc.release_all_servos()
        current_mode = "해제 상태(Released)"  # 모드 상태 업데이트
        print("서보모터를 해제합니다.")
    
    # 'a' 키를 누르면 서보 모터 활성화 
    if keyboard.is_pressed('a'):
        print("모든 서보를 활성화합니다.")
        mc.power_on()
        current_mode = "활성화 상태(Active)"  # 모드 상태 업데이트