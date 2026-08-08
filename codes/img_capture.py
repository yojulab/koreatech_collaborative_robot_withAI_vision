import cv2
import os

def capture_image():
    cap = cv2.VideoCapture(0)  # 일반 웹캠 (기본 카메라)

    save_directory = "dataset/images"
    os.makedirs(save_directory, exist_ok=True)

    image_count = 0

    print("📸 'c' 누르면 저장 / 'q' 누르면 종료")

    while True:
        ret, frame = cap.read()
        if not ret:
            print("카메라를 열 수 없습니다.")
            break

        # 화면 출력
        cv2.imshow("Webcam", frame)

        key = cv2.waitKey(1) & 0xFF

        # c 누르면 저장
        if key == ord('c'):
            file_name = f"{save_directory}/img_{image_count}.jpg"
            cv2.imwrite(file_name, frame)
            print(f"✅ 저장됨: {file_name}")
            image_count += 1

        # q 누르면 종료
        elif key == ord('q'):
            print("종료합니다.")
            break

    cap.release()
    cv2.destroyAllWindows()


capture_image()