import io
from picamera2 import Picamera2
import datetime
from flask import Flask, Response, render_template, request
import stepper
import cv2

app = Flask(__name__)

camera = Picamera2()
camera.configure(camera.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))
camera.start()

def generate_frames():
    while True:
        frame = camera.capture_array()
        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')
        
@app.route('/mouse-event', methods=['POST'])


def handle_mouse_event():
    data = request.get_json()

    # Access the mouse event data
    x = data.get('x')
    y = data.get('y')
    button = data.get('button')

    # Do something with the mouse event data
    print(f"Mouse event at ({x}, {y}), button: {button}")
    stepper.movement('base')
    stepper.movement('top')
    # Return a JSON response
    return ({'message': [x, y]})


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

if __name__ == '__main__':
    stepper.setup()
    app.run(host='0.0.0.0', port=5000, threaded=True)
