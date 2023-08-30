#\\read the txt file D:\Obtain3D\TrackPYSample\coordinates.txt
import os

import matplotlib.pyplot as plt
import pandas as pd

os.chdir("D:\Obtain3D/0408")

#\\The data is seperated by tab. There is header. The columns are number, x, y, z.
data = pd.pandas.read_csv('coordinates.txt',header=None,sep='\t', skiprows=1)

#\\rename the columns as x, y, z
data.columns = ['#', 'x', 'y', 'z', 'whatever']

#\\sort the data by z
data = data.sort_values(by=['z'])

#\\reset the index
data = data.reset_index(drop=True)

#\\make the first column as from 1 to the number of particles
data['#'] = range(1, len(data) + 1)

#\\plot the distribution in z direction as a dot plot. The x axis is the number of the particle. The y axis is the z coordinate of the particle. Label plot.
plt.plot(data['#'], data['z'], 'o')
plt.xlabel('Loop Number')
plt.ylabel('Z Coordinate')
plt.title('Distribution of Loop in Z Direction ML 0408')
plt.show()


