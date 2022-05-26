from json.tool import main
import cv2
import numpy as np
from GoogleSheet import Google_API

from PIL import ImageGrab

# -----------------------------------------------------------
# ローカル環境で動作させるプログラム
# -----------------------------------------------------------

def run_camera():
    # -----------------------------------------------------------
    # Init
    # -----------------------------------------------------------
    font = cv2.FONT_HERSHEY_SIMPLEX

    # -----------------------------------------------------------
    # 画像キャプチャ
    # -----------------------------------------------------------
    # VideoCaptureインスタンス生成
    # 引数でカメラを選べれる。PC本体のカメラ➡️0、外部カメラ⇨1
    cap = cv2.VideoCapture(0)

    # QRCodeDetectorインスタンス生成
    qrd = cv2.QRCodeDetector()
    google = Google_API()
    while cap.isOpened():
        ret, frame = cap.read()
        # frame = np.array(ImageGrab.grab()) #スクリーンショット画像を使用
        
        if ret:
        # QRコードデコード
            retval, decoded_info, points, straight_qrcode = qrd.detectAndDecodeMulti(frame)
            if retval:
                points = points.astype(np.int32)
                for dec_inf, point in zip(decoded_info, points):
                    if dec_inf == '':
                        continue
                    # QRコードデータ
                    print('dec:', int(dec_inf))
                    # バウンディングボックス
                    frame = cv2.polylines(frame, [point], True, (0, 0, 255), 30, cv2.LINE_AA)
                    user_id = str(dec_inf)
                    google.add(user_id)
        
        cv2.imshow('cv2',frame)
        # quit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # キャプチャリソースリリース
    cap.release()
run_camera()
