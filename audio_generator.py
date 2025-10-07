# audio_generator.py
import numpy as np
import sounddevice as sd

class AudioEngine:
    def __init__(self, defaults):
        self.frequency = 136.1

    def update(self, psi_field):
        avg_value = np.mean(psi_field.field)
        freq_mod = self.frequency + avg_value * 10
        tone = np.sin(2 * np.pi * np.linspace(0, 1, 44100) * freq_mod)
        sd.play(tone, 44100, blocking=False)
