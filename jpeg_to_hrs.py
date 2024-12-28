import pandas as pd
import matplotlib.pyplot as plt 
import numpy as np
import imageio

sInputFileName='C:/Users/GAURAV/Desktop/Resume/05-DS/05-DS/9999-Data/Angus.jpg' 
InputData = imageio.imread(sInputFileName, mode='RGBA')
ProcessRawData=InputData.flatten() 
y=InputData.shape[2] + 2 
x=int(ProcessRawData.shape[0]/y)
ProcessData=pd.DataFrame(np.reshape(ProcessRawData, (x, y))) 
sColumns= ['XAxis','YAxis','Red', 'Green', 'Blue','Alpha'] 
ProcessData.columns=sColumns
ProcessData.index.names =['ID'] 
plt.imshow(InputData) 
plt.show()
OutputData=ProcessData 
sOutputFileName='C:/VKHCG/05-DS/9999-Data/HORUS-Picture.csv' 
OutputData.to_csv(sOutputFileName, index = False) 
print('=====================================================')
print('Picture to HORUS - Done') 
print('=====================================================')
