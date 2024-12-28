import os 
import shutil 
import cv2
sInputFileName = 'C:/Users/GAURAV/Desktop/Resume/05-DS/05-DS/9999-Data/dog.mp4'
sDataBaseDir = 'C:/Users/GAURAV/Desktop/Resume/05-DS/05-DS/9999-Data/temp'
if os.path.exists(sDataBaseDir):
    shutil.rmtree(sDataBaseDir)
if not os.path.exists(sDataBaseDir):
    os.makedirs(sDataBaseDir)
vidcap = cv2.VideoCapture(sInputFileName)
if not vidcap.isOpened():
    print('Error: Could not open video file')
    exit()
count = 0
while True:
    success, image = vidcap.read()
    if not success:
        break 
    sFrame = sDataBaseDir + '/dog-frame-' + str(format(count, '04d')) + '.jpg'
    print('Extracted: ', sFrame)
    cv2.imwrite(sFrame, image)
    if os.path.getsize(sFrame) == 0:
        os.remove(sFrame)
        print('Removed: ', sFrame)
        continue
    count += 1
    if cv2.waitKey(10) == 27:
        break
print('Generated: ', count, ' Frames')
print('=====================================================')
print('Movie to Frames HORUS - Done')
print('=====================================================')
