import numpy as np
import matplotlib.pyplot as plt

# Parameters for the normal distribution
mean = 32787.5  # Mean value (center of the distribution)
std_dev = 10000  # Standard deviation (controls the spread of the distribution)
n_samples = 256  # Number of samples to generate
distribution = []
labels = []
# Generate normal distribution data
for i in range(1000):

    if np.random.rand() < 0.5:
        data = np.random.normal(mean, std_dev, n_samples)
        # Clip the data to the range [0, 65575]
        data = np.clip(data, 0, 65575)
        distribution.append(data)
        labels.append(1)
    else:
        data = np.random.uniform(0, 65575, n_samples)
        data = np.clip(data, 0, 65575)
        distribution.append(data)
        labels.append(0)


with open ("S2G\Crypto\LULbashevsky\\test.csv","w") as fil:
    labelX = [f"x_{i}, " for i in range(n_samples)]
    fil.write(f"{''.join(labelX)}target\n")
    for i, (dis, label) in enumerate(zip(distribution, labels)):
        fil.write(f"{', '.join(str((x)) for x in dis) }, {label}\n")