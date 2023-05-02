import wave
import numpy as np
import matplotlib.pyplot as plt

audio_file = "ASax-E4.wav"

# Open WAV file
with wave.open(audio_file, 'rb') as wav_file:
    # Get properties of WAV file
    params = wav_file.getparams()
    num_channels, sample_width, frame_rate, num_frames = params[:4]

    # Read data from WAV file
    raw_data = wav_file.readframes(num_frames)

    # Convert raw data to NumPy array (data = amplitude)
    if sample_width == 1:
        data = np.frombuffer(raw_data, dtype=np.uint8) 
        data = (data - 128) / 128.0
    elif sample_width == 2:
        data = np.frombuffer(raw_data, dtype=np.int16)
        data = data / 32768.0

    # Reshape NumPy array to match number of channels
    data = data.reshape(-1, num_channels)

# Create time array
time = np.arange(0, num_frames) * (1.0 / frame_rate)

# Plot sound wave
plt.plot(time, data)
plt.title("Alto Sax E Amplitude")
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()
