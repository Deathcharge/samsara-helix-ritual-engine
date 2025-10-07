# audio_generator.py
import numpy as np
import streamlit as st

class AudioEngine:
    def __init__(self, defaults):
        self.frequency = defaults.get("base_frequency", 136.1)
        self.harmonic_multiplier = defaults.get("harmonic_multiplier", 432.0)
        self.enabled = defaults.get("resonance", True)

    def update(self, psi_field):
        if not self.enabled:
            return

        avg_value = np.mean(psi_field.field)
        freq_mod = self.frequency + avg_value * 10
        harmonic = self.harmonic_multiplier / self.frequency

        # Display resonance info in sidebar (instead of playing sound)
        st.sidebar.markdown("---")
        st.sidebar.metric("Resonant Frequency", f"{freq_mod:.2f} Hz")
        st.sidebar.metric("Harmonic Ratio", f"{harmonic:.3f}")
