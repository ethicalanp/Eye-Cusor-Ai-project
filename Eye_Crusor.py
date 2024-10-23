import cv2
import mediapipe as mp
import pyautogui

tracking = False

face_mesh =mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w,screen_h = pyautogui.size()

def start_tracking():
    global tracking
    tracking = True

cam = cv2.VideoCapture(0)

crusor_buffer = []

while True:
    ret, frame = cam.read()
    if not ret:
        break
    frame=cv2.flip(frame,1)
    rgb_frame =cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    output = face_mesh.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    frame_h, frame_w,_ = frame.shape
 
    if landmark_points:
        landmarks = landmark_points[0].landmark
        for id,landmark in enumerate(landmarks[474:478]):
            x=int(landmark.x * frame_w)
            y=int(landmark.y * frame_h)
            cv2.circle(frame,(x,y),3,(0,0,255))
            if id==1:
                screen_x=screen_w/frame_w * x
                screen_y=screen_h/frame_h * y 
                crusor_buffer.append((screen_x,screen_y))
                pyautogui.moveTo(screen_x,screen_y)
        left = [landmarks[145],landmarks[159]]
        for landmark in left: 
            x=int(landmark.x * frame_w)
            y=int(landmark.y * frame_h)
            cv2.circle(frame,(x,y),3,(255,0,255))

        if (left [0].y-left[1].y)<0.008:
            pyautogui.click()
            pyautogui.sleep(1)




    cv2.imshow('Eyemouse',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):

        break

cam.release()
cv2.destroyAllWindows()

def stop_tracking():
    global tracking
    tracking = False

if __name__ == "__main__":
    start_tracking()
