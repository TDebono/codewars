import random
import matplotlib.pyplot as plt
import numpy as np

rolls = []

for k in range(100):
    rolls.append((random.choice([1,2,3,4,5,6])))

plt.hist(rolls, np.linspace(0.5,6.5,7))
