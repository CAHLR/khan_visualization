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

    max_x = max(data[:,0]) + 5
    max_y = max(data[:,1]) + 5
    min_x = min(data[:,0]) - 5
    min_y = min(data[:,1]) - 5

    x = [d_x[0] for d_x in data]
    y = [d_y[1] for d_y in data]

    move_to_x = x[1:]
    move_to_y = y[1:]

    diff_x = []
    for ind_x in range(len(move_to_x)):
        diff_x.append(move_to_x[ind_x] - x[ind_x])

    diff_y = []
    for ind_y in range(len(move_to_y)):
        diff_y.append(move_to_y[ind_y] - y[ind_y])

    inc_x = [val / numframes for val in diff_x]
    inc_y = [val / numframes for val in diff_y]

    mov = []
    for timestep in range(0,99):
        initial = []
        indices = []
        for student in range(timestep, len(x), 100):
            initial.append([x[student], y[student]])
            indices.append(student)
        mov.append(initial)
        for step in range(numframes):
            intp_inner = []
            points = mov[timestep * 101 + step]
            for index, [x_val, y_val] in enumerate(points):
                intp_inner.append([x_val + inc_x[indices[index]], y_val + inc_y[indices[index]]])
            mov.append(intp_inner)

#     # print len(mov)
#     # print numframes * num_students * timesteps

    start_x = [x[index] for index in range(0,len(x), 100)]
    start_y = [y[index] for index in range(0,len(y), 100)]

    fig.suptitle('Timestep ' + str(1))

    scat = plt.scatter(start_x, start_y, c=c, s=100)

    ani = animation.FuncAnimation(fig, update_plot, frames=xrange((numframes * timesteps)-1),
                                  fargs=(mov, scat), interval=1, repeat=False)

    plt.axis([min_x, max_x, min_y, max_y])
    plt.show()

#     # Set up formatting for the movie files, very low quality
#     # plt.rcParams['animation.ffmpeg_path'] = '/usr/local/bin/ffmpeg'
#     # mywriter = animation.FFMpegWriter(bitrate=600)
#     # ani.save('animation.mp4', writer=mywriter, fps=15)

def update_plot(i, mov, scat):
    scat.set_offsets(mov[i])
    if i % 101 == 0 and i != 0:
        fig.suptitle('Timestep ' + str((i//101) + 1))
        time.sleep(1)
    return scat,

main()
