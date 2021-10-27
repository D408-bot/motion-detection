import cv2, time, numpy as np, os, glob
cap = cv2.VideoCapture(0)



record_buffer = 0
record_buffer_max = 15
_, frame1 = cap.read()
frame2 = frame1
count = 0

threshold = 150000

while True:
    _, frame1 = cap.read()
    net_difference = 0.0
    sivo1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
    sivo2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)
    diff = cv2.subtract(sivo1, sivo2)

    w = np.size(diff, 0)
    h = np.size(diff, 1)

    for i in range(0, w):
        for j in range(0, h):
            if i % 3 == 0 & j % 3 == 0:
                r = diff[i, j]           
                
                net_difference += r

    cv2.imshow('kur', diff)
    frame1 = frame2
    _, frame2 = cap.read()

    if net_difference > threshold:
        record_buffer = record_buffer_max

    if record_buffer < 0 :
        None
    else:
        if count < 8 or count > 10000:
            None
        else:     
            cv2.imwrite("frame%d.jpg" % count, frame1)     
        
        count += 1
        
    record_buffer = -1
    if record_buffer < -100:
        record_buffer = -100
    

    key = cv2.waitKey(1)
    if key == ord('q'):
        break