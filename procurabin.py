import matplotlib.pyplot as plt
import numpy as np
forca = np.array([2,3,6,8,20,])
aceleracao = np.array([2,3,4,5,6])

plt.scatter(forca, aceleracao)
plt.title("Força x Aceleração")
plt.xlabel("Força (N)")
plt.ylabel("Aceleração (m/s²)")
plt.grid(True)
plt.show()