import streamlit as st
import numpy as np
import scipy.spatial.distance as dist
import dlib
import cv2
import pandas as pd
import time
from imutils import face_utils
import imutils

def mouth_aspect_ratio(mouth):
    A = dist.euclidean(mouth[13], mouth[19])
    B = dist.euclidean(mouth[14], mouth[18])
    C = dist.euclidean(mouth[15], mouth[17])
    D = dist.euclidean(mouth[12], mouth[16])
    mar = (A + B + C) / (2.0 * D)
    return mar

def eye_aspect_ratio(eye):
    A = dist.euclidean(eye[1], eye[5])
    B = dist.euclidean(eye[2], eye[4])
    C = dist.euclidean(eye[0], eye[3])
    ear = (A + B) / (2.0 * C)
    return ear

def main():
    st.title("Yawn and Blink Detection App")
    st.write("This app uses computer vision to detect yawns and blinks in real-time.")
    st.write("To use this app, please grant access to your webcam when prompted.")
    st.write("Please note that this app is for educational purposes only and should not be used as a substitute for medical advice.")

    thresh_mouth = 0.4
    thresh_eye = 0.25
    frame_check = 20
    detect = dlib.get_frontal_face_detector()
    predict = dlib.shape_predictor(r"C:\Users\Nb\Downloads\shape_predictor_68_face_landmarks.dat\shape_predictor_68_face_landmarks.dat")

    (mStart, mEnd) = (48, 68)
    (lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
    (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]

    cap = cv2.VideoCapture(0)
    flag_mouth = 0
    flag_eye = 0
    start_time = time.time()
    df = pd.DataFrame(columns=["real time", "time", "yawn", "blink"])

    stframe = st.empty()
    while True:
        ret, frame = cap.read()
        frame = imutils.resize(frame, width=450)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        subjects = detect(gray, 0)
        for subject in subjects:
            shape = predict(gray, subject)
            shape = face_utils.shape_to_np(shape)

            # Yawn detection
            mouth = shape[mStart:mEnd]
            mar = mouth_aspect_ratio(mouth)
            mouthHull = cv2.convexHull(mouth)
            cv2.drawContours(frame, [mouthHull], -1, (0, 255, 0), 1)

            # Blink detection
            leftEye = shape[lStart:lEnd]
            rightEye = shape[rStart:rEnd]
            leftEAR = eye_aspect_ratio(leftEye)
            rightEAR = eye_aspect_ratio(rightEye)
            ear = (leftEAR + rightEAR) / 2.0
            leftEyeHull = cv2.convexHull(leftEye)
            rightEyeHull = cv2.convexHull(rightEye)
            cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
            cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

            if mar > thresh_mouth:
                flag_mouth += 1
            else:
                flag_mouth = 0

            if ear < thresh_eye:
                flag_eye += 1
            else:
                flag_eye = 0

            if flag_mouth >= frame_check or flag_eye >= frame_check:
                cv2.putText(frame, "*****ALERT!*****", (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                cv2.putText(frame, "*****ALERT!*****", (10,325),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
                current_time = time.time()
                df = df.append({"real time": time.strftime("%H:%M:%S"), "time": current_time - start_time, "yawn": int(flag_mouth >= frame_check), "blink": int(flag_eye >= frame_check)}, ignore_index=True)
            else:
                df = df.append({"real time": time.strftime("%H:%M:%S"), "time": time.time() - start_time, "yawn": 0, "blink": 0}, ignore_index=True)

        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        stframe.image(frame)

        if st.button("Stop"):
            break

    df.plot(x="time", y=["yawn", "blink"])
    st.pyplot()

if _name_ == "_main_":
    main()