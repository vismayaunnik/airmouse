import cv2
import mediapipe as mp
import pyautogui
import time
import math

#Prevent pyautogui fail-safe
pyautogui.FAILSAFE = False

#Webcam 
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 480)

#MediaPipe Hands 
mp_hands = mp.solutions.hands

hand_detector = mp_hands.Hands(
    min_detection_confidence=0.7,
    min_tracking_confidence=0.7,
    max_num_hands=1
)

drawing_utils = mp.solutions.drawing_utils

#Screen size
screen_width, screen_height = pyautogui.size()

#Click cooldown timer
click_time = 0

# Finger State Function
def fingers_up(landmarks):

    fingers = []

    #Thumb
    if landmarks[4].x < landmarks[3].x:
        fingers.append(1)
    else:
        fingers.append(0)

    #Other fingers
    tips = [8, 12, 16, 20]

    for tip in tips:

        if landmarks[tip].y < landmarks[tip - 2].y:
            fingers.append(1)
        else:
            fingers.append(0)

    return fingers


while True:

    success, frame = cap.read()

    if not success:
        break

    frame = cv2.flip(frame, 1)

    frame_height, frame_width, _ = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    output = hand_detector.process(rgb_frame)

    hands = output.multi_hand_landmarks

    if hands:

        for hand in hands:

            drawing_utils.draw_landmarks(
                frame,
                hand,
                mp_hands.HAND_CONNECTIONS
            )

            landmarks = hand.landmark

            index_x = 0
            index_y = 0
            thumb_x = 0
            thumb_y = 0
            pinky_x = 0

            for id, landmark in enumerate(landmarks):

                x = int(landmark.x * frame_width)
                y = int(landmark.y * frame_height)

                #Index
                if id == 8:

                    cv2.circle(frame, (x, y), 10, (0,255,255), -1)

                    index_x = screen_width / frame_width * x
                    index_y = screen_height / frame_height * y

                #Thumb 
                if id == 4:

                    cv2.circle(frame, (x, y), 10, (0,255,0), -1)

                    thumb_x = screen_width / frame_width * x
                    thumb_y = screen_height / frame_height * y

                #Pinky 
                if id == 20:

                    pinky_x = screen_width / frame_width * x

            click_distance = math.hypot(
                index_x - thumb_x,
                index_y - thumb_y
            )

            current_time = time.time()

            #Finger states
            finger_state = fingers_up(landmarks)

            #Click: Index and thumb close together
            if click_distance < 45 and current_time - click_time > 0.8:

                pyautogui.click()

                click_time = current_time

                cv2.putText(
                    frame,
                    "CLICK",
                    (50,100),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,255,0),
                    3
                )

            #Scroll Up: Open Palm
            elif finger_state == [1,1,1,1,1] and thumb_x < pinky_x:

                pyautogui.scroll(80)

                cv2.putText(
                    frame,
                    "SCROLL UP",
                    (50,150),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (255,0,0),
                    3
                )

            #Scroll Down: Back of Palm
            elif thumb_x > pinky_x:

                pyautogui.scroll(-80)

                cv2.putText(
                    frame,
                    "SCROLL DOWN",
                    (50,150),
                    cv2.FONT_HERSHEY_SIMPLEX,
                    1,
                    (0,0,255),
                    3
                )
            
            #Move: Only index finger up
            else:

                pyautogui.moveTo(index_x, index_y)

  
            cv2.putText(
                frame,
                f"ClickDist: {int(click_distance)}",
                (10,40),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (0,255,0),
                2
            )

            cv2.putText(
                frame,
                f"Fingers: {finger_state}",
                (10,80),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                (255,0,0),
                2
            )

    cv2.imshow("Smart AirMouse", frame)

    #Exit: Press 'Esc' key
    key = cv2.waitKey(1)

    if key == 27:
        break


cap.release()
cv2.destroyAllWindows()