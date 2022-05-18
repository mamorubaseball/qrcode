from cProfile import run
from flask import Flask, render_template, Response
from webcam2 import run_camera2
from GoogleSheet import Google_API

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

def gen():
    while True:
        frame,user_id = run_camera2()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')
        if user_id:
            google = Google_API()
            google.add(user_id = user_id)

@app.route('/video_feed')
def video_feed():
    return Response(gen(),
                    mimetype='multipart/x-mixed-replace;boundary=frame')
    

if __name__ == "__main__":
    app.run()
    # app.run(debug=False, host='0.0.0.0', port=80)