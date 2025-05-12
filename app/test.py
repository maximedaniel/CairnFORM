import numpy as np
import seaborn as sns
sns.set()
data = [2.83, 2.11, 1.47, 1.10, 1.13, 1.48, 2.06, 2.72 ,3.28 ,3.61 ,3.66 ,3.44]
d_min = np.min(data)
d_max = np.max(data)
data = (np.array(data) - d_min) / (d_max-d_min)
data = data * 200
print(data)
print(sns.palpot(sns.color_palette("Blues", len(data))))

