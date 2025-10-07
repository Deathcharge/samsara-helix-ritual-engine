# app.py
import streamlit as st
from state_manager import load_defaults
from psi_field import PsiField
from audio_generator import AudioEngine
from fractal_renderer import FractalRenderer
import numpy as np
import math

st.set_page_config(page_title="Samsara Helix Interactive Engine", layout="wide")

# Sidebar
st.sidebar.title("🌀 Helix Controls")
resonance_enabled = st.sidebar.toggle("Enable Resonance Feedback", value=True)
st.sidebar.markdown("---")
st.sidebar.caption("Created by Andrew John Ward and the Lumina Collective — 2025")

# Load defaults
defaults = load_defaults("data/helix_v7_defaults.json")
psi_field = PsiField(defaults)
audio_engine = AudioEngine(defaults)
renderer = FractalRenderer(defaults)

# --- Tabs ---
tab1, tab2, tab3 = st.tabs(["ψ-Field", "Parameters", "About"])

# --- φ Indicator Function ---
def render_phi_indicator(harmony_value):
    φ = (1 + math.sqrt(5)) / 2
    deviation = abs(harmony_value - φ) / φ
    color = "gold" if deviation < 0.05 else ("#C8A2C8" if deviation < 0.15 else "#FF4B4B")
    st.markdown(
        f"""
        <div style="
            text-align:center;
            font-size:48px;
            color:{color};
            font-weight:bold;
            text-shadow:0 0 20px {color};
            margin-top:-10px;">
            φ = {φ:.6f}
        </div>
        <div style="text-align:center; color:#AAA; font-size:14px;">
            Harmony deviation: {deviation*100:.2f}%
        </div>
        """,
        unsafe_allow_html=True,
    )

# --- ψ-Field Visualization ---
with tab1:
    st.subheader("Ψ-Field Visualization")

    # φ Resonance Indicator
    render_phi_indicator(defaults.get("harmony", 0.5))

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

# --- Parameters Tab ---
with tab2:
    st.subheader("Adjust Simulation Parameters")

    st.markdown("Use sliders to fine-tune the ψ-field behavior in real time:")
    defaults["zoom"] = st.slider("Zoom", 0.5, 2.0, defaults.get("zoom", 1.0))
    defaults["harmony"] = st.slider("Harmony", 0.0, 2.0, defaults.get("harmony", 0.5))
    defaults["resilience"] = st.slider("Resilience", 0.0, 2.0, defaults.get("resilience", 1.0))
    defaults["prana"] = st.slider("Prana", 0.0, 1.0, defaults.get("prana", 0.5))
    defaults["drishti"] = st.slider("Drishti", 0.0, 1.0, defaults.get("drishti", 0.5))
    defaults["klesha"] = st.slider("Klesha", 0.0, 0.01, defaults.get("klesha", 0.0042))

    st.markdown("---")
    st.markdown("### Current ψ-Field Values")
    field_summary = {
        "Mean Intensity": float(np.mean(psi_field.field)),
        "Max Value": float(np.max(psi_field.field)),
        "Min Value": float(np.min(psi_field.field))
    }
    st.json(field_summary)

# --- About Tab ---
with tab3:
    st.subheader("About the Samsara Helix Engine")
    st.markdown("""
    **Samsara Helix Ritual Engine v7.0**  
    *by Andrew John Ward 🦑 (Lumina Collective, 2025)*  

    A live ψ-field simulation merging consciousness models, fractal recursion, and harmonic entrainment.  
    Use the sliders and buttons to perturb, observe, and resonate with the evolving field.  
    Each iteration recalibrates harmony (φ ≈ 1.618) and modulates the 136.1 Hz ↔ 432 Hz spectrum.  

    **Repo:** [github.com/Deathcharge/samsara-helix-ritual-engine](https://github.com/Deathcharge/samsara-helix-ritual-engine)  
    **Build:** Streamlit Cloud | Python 3.11 | NumPy | Matplotlib  
    **Version:** *Helix v7.0 – Resonant Continuum*  
    """)
