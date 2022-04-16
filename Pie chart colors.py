import matplotlib.pyplot as plt
import numpy as np
y = np.array([35, 25, 25, 15])
mylabels = [“Python”, “C”, “C++”, “Java”]
mycolors = [“Red”, “pink”, “blue”, “Purple”]
plt.pie(y, labels = mylabels, colors = mycolors)
plt.show()
