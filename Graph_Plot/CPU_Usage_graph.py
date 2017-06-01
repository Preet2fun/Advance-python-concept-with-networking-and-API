import matplotlib.pyplot as plt
import numpy as np
import psutil
from matplotlib import animation

fig = plt.figure()
ax = plt.axes(xlim=(0, 100), ylim=(0,100))


def animate(i):
    xar = []
    yar = []
    x = np.linspace(i,i+1)
    y = psutil.cpu_percent(interval=1)
    xar.append(x)
    yar.append(y)
    plt.plot(xar, yar, 'ro')


anim = animation.FuncAnimation(fig, animate, frames=200, interval=100, blit=False)
#anim = animation.FuncAnimation(fig, animate,interval=1000)
plt.show()



'''

import numpy as np
import psutil
import matplotlib.pyplot as plt
#from matplotlib import pyplot as plt
from matplotlib import animation

# First set up the figure, the axis, and the plot element we want to animate
fig = plt.figure()
ax = plt.axes(xlim=(0, 100), ylim=(0,100))
line, = ax.plot([], [], lw=2)

# initialization function: plot the background of each frame
#def init():
#    line.set_data([], [])
#    return line,

# animation function.  This is called sequentially
def animate(i):
    xar = []
    yar = []
    x = np.linspace(i,i+1)
    y = psutil.cpu_percent(interval=1)
    xar.append(x)
    yar.append(y)
    #line.set_data(xar, yar)
    #print x
    print y
    #return line,
    #ax1.clear()
    #ax.plot(xar,yar)
    ax.plot(xar, yar, 'ro')

# call the animator.  blit=True means only re-draw the parts that have changed.
#anim = animation.FuncAnimation(fig, animate, init_func=init,frames=200, interval=1000, blit=False)
anim = animation.FuncAnimation(fig, animate,interval=1000)
# save the animation as an mp4.  This requires ffmpeg or mencoder to be
# installed.  The extra_args ensure that the x264 codec is used, so that
# the video can be embedded in html5.  You may need to adjust this for
# your system: for more information, see
# http://matplotlib.sourceforge.net/api/animation_api.html
#anim.save('basic_animation.mp4', fps=30, extra_args=['-vcodec', 'libx264'])

plt.show()

'''