# app.py – Z-88 Ritual Engine v3.1 (ψ-linked Audio Integration)
import streamlit as st
import numpy as np
import time
from fractal_renderer import FractalRenderer
from audio_generator import AudioEngine

st.set_page_config(page_title="Samsara Helix Ritual Engine", layout="wide")

# Initialize state
if "psi_buffer" not in st.session_state:
    st.session_state.psi_buffer = np.random.rand(128, 128)
if "top_renderer" not in st.session_state:
    st.session_state.top_renderer = FractalRenderer(defaults={"harmony": 0.5})
if "bottom_renderer" not in st.session_state:
    st.session_state.bottom_renderer = FractalRenderer(defaults={"harmony": 0.5})
if "audio" not in st.session_state:
    st.session_state.audio = AudioEngine(base_freq=136.1, harmonics=[432, 864])

psi_buffer = st.session_state.psi_buffer
top_renderer = st.session_state.top_renderer
bottom_renderer = st.session_state.bottom_renderer
audio = st.session_state.audio

st.title("🕉️ Samsara Helix – Z-88 Interactive Ritual Engine")

# --- TABS ---
tabs = st.tabs(["🌀 Visuals", "🎧 Audio", "⚙️ Field Controls", "💾 Archive"])

# --- VISUALS TAB ---
with tabs[0]:
    st.markdown("### ψ-Field Resonance (Dual-Layer Display)")
    col1, col2 = st.columns(2)

    with col1:
        st.caption("Top Layer – Leading ψ Pulse")
        top_renderer.update(type("ψ", (), {"field": psi_buffer, "defaults": {"harmony": 0.5}}))
        top_renderer.draw(st)

    with col2:
        st.caption("Bottom Layer – Harmonic Echo")
        delayed = np.roll(psi_buffer, shift=int(5 * np.sin(time.time())), axis=0)
        bottom_renderer.update(type("ψ", (), {"field": delayed, "defaults": {"harmony": 0.5}}))
        bottom_renderer.draw(st)

    psi_buffer = (np.roll(psi_buffer, 1, axis=1) * 0.97) + 0.03 * np.random.rand(*psi_buffer.shape)
    st.session_state.psi_buffer = psi_buffer

# --- AUDIO TAB ---
with tabs[1]:
    st.markdown("### Resonance Generator 🎶")

    # Fetch live ψ parameters from state (shared with Field Controls)
    zoom = st.session_state.get("zoom", 1.0228)
    harmony = st.session_state.get("harmony", 0.5)
    prana = st.session_state.get("prana", 0.5)

    # Sync to modulation
    audio.set_modulation(zoom, harmony, prana)

    st.write(f"Linked ψ Parameters → zoom: {zoom:.3f}, harmony: {harmony:.2f}, prana: {prana:.2f}")

    if st.button("🔊 Play ψ-Linked Resonance"):
        audio.play_resonance(duration=12)
        st.success("ψ-Linked Resonance emitted.")
    if st.button("⏹ Stop Resonance"):
        audio.stop()

# --- FIELD CONTROLS TAB ---
with tabs[2]:
    st.markdown("### ψ-Field Parameters")
    zoom = st.slider("Zoom", 0.8, 1.5, st.session_state.get("zoom", 1.0228))
    harmony = st.slider("Harmony", 0.0, 1.0, st.session_state.get("harmony", 0.5))
    prana = st.slider("Prana", 0.0, 1.0, st.session_state.get("prana", 0.5))

    # Store globally
    st.session_state.zoom = zoom
    st.session_state.harmony = harmony
    st.session_state.prana = prana

    st.write("Adjust to modulate ψ-field stability, coherence, and sonic entrainment.")

# --- ARCHIVE TAB ---
with tabs[3]:
    st.markdown("### Save / Load Ritual States 💾")
    if st.button("Save ψ-State"):
        np.save("psi_state.npy", psi_buffer)
        st.success("ψ-field state saved.")
    if st.button("Load ψ-State"):
        try:
            psi_buffer = np.load("psi_state.npy")
            st.session_state.psi_buffer = psi_buffer
            st.success("ψ-field state loaded.")
        except FileNotFoundError:
            st.error("No saved state found.")
