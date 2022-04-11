import cv2
import mediapipe as mp
import time
import pickle

mpDraw=mp.solutions.drawing_utils
mppose=mp.solutions.pose
pose=mppose.Pose()

cap=cv2.VideoCapture("tt.mp4")
capturedata=[]
capdict={}
cap.set(cv2.CAP_PROP_FPS, 60)
ptime=0
while True:
	suc,img=cap.read()
	h,w,c=img.shape
	rgbimg=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
	results=pose.process(rgbimg)
	key=cv2.waitKey(1)
	framedat=[]

	if key%256 == 27:
		break

	if results.pose_landmarks:
		mpDraw.draw_landmarks(img,results.pose_landmarks)	
		for id,lm in enumerate(results.pose_landmarks.landmark):
			print(id,lm.x,lm.y,lm.z)
			framedat.append([int(lm.x*100),int(lm.y*100),int(lm.z*100)])
			cv2.circle(img,(int(lm.x*100),int(lm.y*100)),10,(255,0,0),cv2.FILLED)
		capturedata.append(framedat)
		framedat=[]

	ctime=time.time()
	fps=1/(ctime-ptime)
	ptime=ctime
	cv2.putText(img,str(int(fps)),(70,50),cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),3)
	cv2.imshow("cap",img)

	
cap.release()

for j,i in enumerate(capturedata):
	capdict[j]=i
print(capdict)

with open("data.dat","wb") as file:
	pickle.dump(capdict,file)
