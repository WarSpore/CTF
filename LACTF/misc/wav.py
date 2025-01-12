import numpy as np
from scipy.io.wavfile import read
import matplotlib.pyplot as plt

# Read the WAV file
filename = 'LACTF\Crypto\misc\misc_mixed-signals_message.wav'  # Update with the correct filename

try:
    sample_rate, signal = read(filename)
except Exception as e:
    print(f"Error reading the WAV file: {e}")
    raise  # Re-raise the exception to terminate the script

# Check the properties of the loaded signal
# Compute the DFT of the signal

newSignal = []
second = 33
for i in range(second):
    newSignal.append(signal[len(signal)//((second))*i:len(signal)//((second))*(i+1)])



frequencies = np.fft.fftfreq(len(signal), d=1/sample_rate)
fHat = np.fft.fft(signal)
print(sum(fHat))
# Plot the frequency spectrum
plt.figure(figsize=(18, 5))
plt.plot(frequencies, 2 * np.abs(fHat) / len(signal), "c-")
plt.xlabel('Frequency [Hz]', fontsize=20)
plt.ylabel('$2|\hat{f}_n|/N$', fontsize=22)
plt.rc('xtick', labelsize=13)
plt.rc('ytick', labelsize=15)
plt.xlim([0, 3000])  # Plot frequencies up to half of the sample rate
plt.ylim([0,100])
plt.title('Frequency Spectrum of the WAV File')
plt.show()

# Plot the frequency spectrum
# plt.figure(figsize=(18, 5))
# plt.plot(frequencies, 2 * np.abs(fHat) / len(signal), "c-")
# plt.xlabel('Frequency [Hz]', fontsize=20)
# plt.ylabel('$2|\hat{f}_n|/N$', fontsize=22)
# plt.rc('xtick', labelsize=13)
# plt.rc('ytick', labelsize=15)
# plt.xlim([0, 300 / 2])  # Plot frequencies up to half of the sample rate
# plt.ylim([0,30000])
# plt.title('Frequency Spectrum of the WAV File')
# plt.show()
