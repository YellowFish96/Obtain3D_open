import os

import pandas as pd

os.chdir("D:\Obtain3D\TrackPYSample")

#\\read the txt file in the folder. read only the first 4 columns of the txt
data = pd.pandas.read_csv('0409.txt',header=None,sep=' ', names=['frame', 'particle', 'x', 'y','W','H','A','B','C','Class','D'])

#\\concatenate the columns we want to use for the tracking
tpy_data = pd.concat([data['particle'], data['frame'],data['y'],data['x']],axis=1)

'''
#\\find the min and max in frame number
print(tpy_data['frame'].min())
print(tpy_data['frame'].max())
'''

#\\reduce tpy_data to include only the min and the max in frame number
tpy_data = tpy_data[(tpy_data['frame'] == tpy_data['frame'].min()) | (tpy_data['frame'] == tpy_data['frame'].max())]

#\\reduce tpy_data to include particle only in both the min frame number and in the max frame number
tpy_data = tpy_data[(tpy_data['particle'].isin(tpy_data[tpy_data['frame'] == tpy_data['frame'].min()]['particle'])) & (tpy_data['particle'].isin(tpy_data[tpy_data['frame'] == tpy_data['frame'].max()]['particle']))]

tpy_data = tpy_data.reset_index(drop=True)
#print(tpy_data)

#\\make in_data with 6 columns: x1, y1, x2, y2, pointtype, point number. x1, y1 is the x and y coordinates of the particle in the min frame number. x2, y2 is the x and y coordinates of the particle in the max frame number. pointtype will be all zero. point number will be the number from 1 to the number of particles.
in_data = pd.DataFrame(columns=['x1', 'y1', 'x2', 'y2', 'pointtype', 'pointnumber'])
in_data['x1'] = tpy_data[tpy_data['frame'] == tpy_data['frame'].min()]['x'].reset_index(drop=True)
in_data['y1'] = tpy_data[tpy_data['frame'] == tpy_data['frame'].min()]['y'].reset_index(drop=True)
in_data['x2'] = tpy_data[tpy_data['frame'] == tpy_data['frame'].max()]['x'].reset_index(drop=True)
in_data['y2'] = tpy_data[tpy_data['frame'] == tpy_data['frame'].max()]['y'].reset_index(drop=True)
in_data['pointtype'] = 0
in_data['pointnumber'] = range(1, len(in_data) + 1)

#print(tpy_data[tpy_data['frame'] == tpy_data['frame'].max()]['y'])
#print(in_data)

#\\export in_data as txt
in_data.to_csv("in.txt", sep=' ', index=False, header=False)

#\\create a part_data with 3 columns: pointnumber, size, type. pointnumber is the same as in_data. size is all 25. type is all 2.
part_data = pd.DataFrame(columns=['pointnumber', 'size', 'type'])
part_data['pointnumber'] = in_data['pointnumber']
part_data['size'] = 50
part_data['type'] = 2

#export part_data as txt
part_data.to_csv("part.txt", sep=' ', index=False, header=False)

#\\create a key.txt file indluding the following:
f = open("key.txt", "w")
f.write("x_tilt_1	-20.00\n")
f.write("x_tilt_2	-15.00\n")
f.write("y_tilt_1	-10.23\n")
f.write("y_tilt_2	-10.23\n")
f.write("scale_pixels/nm	1\n")
f.write("interfaces	0\n")
f.write("Spherical_particles_or_cavities	1\n")
f.write("view	1\n")
f.write("Number_markers_on_plot	0\n")
f.write("movie	0\n")
f.close()


