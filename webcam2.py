import imp
import cv2
import numpy as np
from GoogleSheet import Google_API


def run_camera2():
    # -----------------------------------------------------------
    # Init
    # -----------------------------------------------------------
    font = cv2.FONT_HERSHEY_SIMPLEX

    # -----------------------------------------------------------
    # 画像キャプチャ
    # -----------------------------------------------------------
    # VideoCaptureインスタンス生成
    # 引数でカメラを選べれる。PC本体のカメラ➡️0、外部カメラ⇨1
    cap = cv2.VideoCapture(1)

    # QRCodeDetectorインスタンス生成
    qrd = cv2.QRCodeDetector()
   
    ret, frame = cap.read()

    user_id = None

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
                
    ret, jpeg = cv2.imencode('.jpg', frame)
    return jpeg.tobytes(),user_id

