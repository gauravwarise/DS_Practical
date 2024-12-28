import imageio
import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import os
sDataBaseDir='C:/Users/GAURAV/Desktop/Resume/05-DS/05-DS/9999-Data/temp' 
f=0
for file in os.listdir(sDataBaseDir):
    if file.endswith(".jpg"):
        f += 1
sInputFileName=os.path.join(sDataBaseDir, file) 
InputData = imageio.imread(sInputFileName, mode='RGBA') 
ProcessRawData=InputData.flatten() 
y=InputData.shape[2] + 2 
x=int(ProcessRawData.shape[0]/y)
ProcessFrameData=pd.DataFrame(np.reshape(ProcessRawData, (x, y))) 
ProcessFrameData['Frame']=file 
plt.imshow(InputData) 
plt.show()
ProcessData = []
if f == 1:
    ProcessData=ProcessFrameData 
else:
    ProcessData=ProcessData.append(ProcessFrameData)  
if f > 0:
    # ProcessData = pd.DataFrame(ProcessFrameData)
    print(ProcessData)
    sColumns= ['XAxis','YAxis','Red', 'Green', 'Blue','Alpha','FrameName'] 
    ProcessData.columns=sColumns 
    ProcessFrameData.index.names =['ID'] 
    print('Rows: ',ProcessData.shape[0]) 
    print('Columns :',ProcessData.shape[1])
ProcessData.to_csv('C:/VKHCG/05-DS/9999-Data/HORUS-Movie-Frame.csv' , index = False) 
print('Processed ; ', f,' frames')
