import io
import picamera
import datetime
from flask import Flask, Response, render_template, request
import stepper

app = Flask(__name__)

def generate_frames():
    with picamera.PiCamera() as camera:
        camera.resolution = (640, 480)
        camera.framerate = 24
        stream = io.BytesIO()

        for _ in camera.capture_continuous(stream, 'jpeg', use_video_port=True):
            stream.seek(0)
            yield b'--frame\r\nContent-Type: image/jpeg\r\n\r\n' + stream.read() + b'\r\n'
            stream.seek(0)
            stream.truncate()

@app.route('/mouse-event', methods=['POST'])
def handle_mouse_event():
    data = request.get_json()

    # Access the mouse event data
    x = data.get('x')
    y = data.get('y')
    button = data.get('button')

    # Do something with the mouse event data
    print(f"Mouse event at ({x}, {y}), button: {button}")
    stepper.movement()
    # Return a JSON response
    return ({'message': [x, y]})

def z():
    print("hello world")

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/')
def hello():
    return render_template('index.html', utc_dt=datetime.datetime.utcnow())

if __name__ == '__main__':
    stepper.setup()
    app.run(host='0.0.0.0', port=5000, threaded=True)
