import numpy as np
import matplotlib.pyplot as plt


x = np.linspace(-np.pi, np.pi, 256, endpoint=True)
c,s = np.cos(x), np.sin(x)

#plt.plot(x,c)
#plt.plot(x,s)
plt.subplot(111)
#plt.figure(figsize=(8,6), dpi=80)
plt.show()