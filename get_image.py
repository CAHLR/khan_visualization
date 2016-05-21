import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
import time

c = [[0.0,0.0,0.0,0.5]]
fig = plt.figure(figsize=(10,10))

def main():
    numframes = 100
    num_students = 682
    timesteps = 100

    data = np.loadtxt('data_file_path_here')

    ##### In order to save #####

    x = [d_x[0] for d_x in data]
    y = [d_y[1] for d_y in data]

    tstep = 0 # Gets the 0 timestep
    start_x = [x[index] for index in range(tstep, len(x), 100)] 
    start_y = [y[index] for index in range(tstep, len(y), 100)]
    scat = plt.scatter(start_x, start_y, c=c, s=100)
    fig.savefig('output_name.png')

main()
