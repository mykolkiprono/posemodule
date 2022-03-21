import cv2 as cv
import mediapipe as mp 
import time


class posedector():
	def __init__(self, mode = False, upper_body = False,smoothness = True, detection_confidence = 0.5, tracking_confidence = 0.5):
		self.mode = mode
		self.upper_body = upper_body
		self.moothness = smoothness
		self.tracking_confidence = tracking_confidence
		self.detection_confidence = detection_confidence


		self.mpPose = mp.solutions.pose
		self.pose = mpPose.Pose(self.mode, self.upper_body,self.smoothness,self.detection_confidence,self.tracking_confidence)
		self.mpdraw = mp.solutions.drawing_utils

	def find_pose(self, image, draw = True):
		image_rgb = cv.cvtColor(frame, cv.COLOR_BGR2RGB)
		results = self.pose.process(image_rgb)    

	    if results.pose_landmarks == True:
	    	if draw:
				self.mpdraw.draw_landmarks(frame, results.pose_landmarks, self.mpPose.POSE_CONNECTIONS)

	return image
	
	

def main():
	video = cv.VideoCapture(0)

	ptime = 0

	while True:
	is_true, frame = video.read()
	img = detector.findpos(frame)

	ctime  = time.time()
	fps = 1/(ctime-ptime)
	ptime = ctime

	cv.putText(frame, str(int(fps)), (70,50), cv.FONT_HERSHEY_PLAIN, 3, (0,255,0), 3)
	cv.imshow('frame', img)

	if cv.waitKey(1) & 0xFF == ord('q'):
		break



if __name__ == '__main__':
	main()