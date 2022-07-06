import numpy as np
import matplotlib.pyplot as plt
  
# creating a dataset
nrows, ncols = 60, 60
data = np.random.random((nrows,ncols))
# data is an 3d array  with 
# 10x12x10=1200 elements.
# reshape this 3d array in 2d
# array for plotting
data = data.reshape(nrows, ncols)
# creating a plot
pixel_plot = plt.figure(figsize=(60,60))

data1 = data.copy()
data2 = data.copy()
linedata = data.copy()
#import pdb; pdb.set_trace()
for r in range (nrows):
	for c in range(ncols):
		if r == c or r ==c-1 or r==c+1:
			linedata[r][c] = 0 #white is 0 
		else:
			linedata[r][c] = 1 #black is 1 

data = linedata.copy()

def anti_aliasing(nrows,ncols,data,th):
	for i in range(nrows):
		for j in range(ncols):
			avg1 = data[i][j]
			count1 = 1
			for k in [-1, 1]:
				for f in [1,-1]:
					row = i + k  #offset 
					col = f + j 
					if i>0 and i <nrows-1 and j>0 and j<ncols-1: #boundary checking 
						#Edge detection: when a black pixel neighbours a white pixel  
						if data[i][j] >th and ((data[i][j+1]<th or data[i][j-1]<th) or  (data[i+1][j]<th or data[i-1][j]<th)): 
							avg1 += data[row][col]
							count1 = count1 +1;
			avg1 = avg1 / count1
			data1[i][j] = avg1		
	return data1

new_data1 = anti_aliasing(nrows,ncols,data,0.9)
new_data2 = anti_aliasing(nrows,ncols,new_data1,0.6)
new_data3 = anti_aliasing(nrows,ncols,new_data2,0.3)

#print(data1==data2)

pixel_plot.add_subplot(2,2,1)	
plt.imshow(data,cmap="Greys", interpolation='nearest', origin='lower')

pixel_plot.add_subplot(2,2,2)	
plt.imshow(new_data1,cmap="Greys", interpolation='nearest', origin='lower')  

#pixel_plot.add_subplot(2,2,3)	
#plt.imshow(new_data2,cmap="Greys", interpolation='nearest', origin='lower')

#pixel_plot.add_subplot(2,2,4)	
#plt.imshow(new_data3,cmap="Greys", interpolation='nearest', origin='lower')
# show plot
plt.show()
