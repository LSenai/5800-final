import matplotlib.pyplot as plt
import numpy as np
from fft import fft
from preprocess_wav import preprocess_wav

audio_file = "ASax-E4.wav"
# audio_file = "Violin-A#4.wav"
sample_rate = 44100

# Preprocess the wave file and get the scaled audio data
scaled_audio_data = preprocess_wav(audio_file)

# Convert the scaled audio data to a list of complex numbers
complex_audio_data = [complex(x, 0) for x in scaled_audio_data]

# Compute the FFT of the complex audio data
fft_result = fft(complex_audio_data)

# Compute the magnitude of the FFT output
mag = [np.sqrt(x.real**2 + x.imag**2) for x in fft_result]

# Get the frequency resolution
freq_res = sample_rate / len(mag)

# Create an array of frequencies
freqs = np.arange(0, len(mag)) * freq_res

# Plot the magnitude of the FFT as a function of frequency
plt.plot(freqs, mag)
plt.title("Alto Sax E")
#plt.title("Violin A#")
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.show()

