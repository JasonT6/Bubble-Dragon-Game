from configparser import Interpolation
import cv2
import numpy as np
import json


testImage = cv2.imread("image1.png")



height = 240

width = 320
array = []

success = True


if success:
    frame = cv2.resize(testImage,(width, height),fx = 0, fy = 0, interpolation = cv2.INTER_AREA)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

frame = np.array(frame).tolist()

with open('outputArray.json', 'w') as f:
    json.dump(frame, f)

outputstring = ''

# print("{")
outputstring += "{"
count3 = 0
for i in range(len(frame)):
    count2 = 0
    # print("{")
    outputstring += "{"
    
    for j in range(len(frame[i])):
        count = 0
        # print("{")
        # outputstring += "{"
        # for k in range(len(frame[i][j])):
        for k in range(1):
            # print(frame[i][j][k])
            frame[i][j][0] = int((frame[i][j][0]/255)*31)
            red = frame[i][j][0] << 11
            frame[i][j][1] = int((frame[i][j][1]/255)*63)
            green = frame[i][j][1] << 5
            frame[i][j][2] = int((frame[i][j][2]/255)*31)
            blue = frame[i][j][2]
            color = red | green | blue

            outputstring += str(color)
            count += 1
            # if count < 3:
            #     print(",")
            #     outputstring += ","
        # print("}")
        # outputstring += "}"
        count2 += 1
        if count2 < width:
            # print(",")
            outputstring += ","
            
    # print("}")
    outputstring += "}"
    
    count3 += 1
    if count3 < height:
        # print(",")
        outputstring += ","
    outputstring += "\n"

# print("}")
outputstring += "}"
outputstring += ";"

print(outputstring)