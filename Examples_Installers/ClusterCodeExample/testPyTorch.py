import torch
import numpy as np
import os



# Output Test
data = np.random.rand(2000, 20)
data[:,19] = np.random.randint(0, 2, 2000, dtype=int)

# Change to your output folder:
OutDir='/export/home/debora/Epilepsy/Results/' 
np.savez(os.path.join(OutDir,'data.npy'),data=data)

print("Hi cluster!")

# Cuda Test
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
n, d = data.shape
x_i = data[:, :d-1]
y_i = data[:, -1].reshape((n, 1))
x_i = torch.from_numpy(x_i).to(device)
y_i = torch.from_numpy(y_i).to(device)
x_i = x_i**2
y_i = y_i + x_i[:,3]


print("Hello pytorch!")


