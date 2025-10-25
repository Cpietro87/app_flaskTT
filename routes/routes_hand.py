from flask import Blueprint, render_template, Response
import cv2
import mediapipe as mp

routes_hand = Blueprint('routes_hand', __name__, url_prefix='/hand')

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

hands = mp_hands.Hands(
    max_num_hands=1,
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7
)

def count_fingers(hand_landmarks):
    tips_ids = [4, 8, 12, 16, 20]  # pulgar, indice, medio, anular, meñique
    fingers = []

    # Pulgar
    if hand_landmarks.landmark[tips_ids[0]].x < hand_landmarks.landmark[tips_ids[0]-1].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Otros dedos
    for id in range(1, 5):
        if hand_landmarks.landmark[tips_ids[id]].y < hand_landmarks.landmark[tips_ids[id]-2].y:
            fingers.append(1)
        else:
            fingers.append(0)
    return fingers.count(1)

def gen_frames():
    cap = cv2.VideoCapture(0)

    while True:
        success, frame = cap.read()
        if not success:
            break

        image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        result = hands.process(image_rgb)

        if result.multi_hand_landmarks:
            for hand_landmarks in result.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
                finger_count = count_fingers(hand_landmarks)
                cv2.putText(frame, f'Dedos: {finger_count}', (10, 50),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 255, 0), 3)

        ret, buffer = cv2.imencode('.jpg', frame)
        frame = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

    cap.release()

@routes_hand.route('/camera')
def hand_camera():
    return render_template('hand_camera.html')

@routes_hand.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

