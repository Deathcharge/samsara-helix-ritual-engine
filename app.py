# app.py
import streamlit as st
from state_manager import load_defaults
from psi_field import PsiField
from audio_generator import AudioEngine
from fractal_renderer import FractalRenderer

st.set_page_config(page_title="Samsara Helix Interactive Engine", layout="wide")
st.sidebar.title("🌀 Helix Controls")
resonance_enabled = st.sidebar.toggle("Enable Resonance Feedback", value=True)
st.sidebar.markdown("---")
st.sidebar.caption("Created by Andrew John Ward and the Lumina Collective — 2025")

defaults = load_defaults("data/helix_v7_defaults.json")
psi_field = PsiField(defaults)
audio_engine = AudioEngine(defaults)
renderer = FractalRenderer(defaults)

if "initialized" not in st.session_state:
    st.markdown("<h3 style='text-align:center;'>Initializing ψ‑Field…</h3>", unsafe_allow_html=True)
    st.session_state.initialized = True
    st.stop()

canvas = renderer.render_field(resonance_enabled=resonance_enabled)

col1, col2 = st.columns(2)
if col1.button("Surprise Me! 🎁"):
    psi_field.random_perturbation()
if col2.button("Reset Canvas"):
    psi_field.reset()

psi_field.update()
renderer.update(psi_field)
audio_engine.update(psi_field)
renderer.draw(canvas)
