# app.py – Z-88 Ritual Engine v3.0 (Tabbed Layout)
import streamlit as st
import numpy as np
import time
from fractal_renderer import FractalRenderer
from audio_generator import AudioEngine

st.set_page_config(page_title="Samsara Helix Ritual Engine", layout="wide")

# Initialize shared states
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

# --- TAB NAVIGATION ---
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

    # evolve field buffer
    psi_buffer = (np.roll(psi_buffer, 1, axis=1) * 0.97) + 0.03 * np.random.rand(*psi_buffer.shape)
    st.session_state.psi_buffer = psi_buffer

# --- AUDIO TAB ---
with tabs[1]:
    st.markdown("### Resonance Generator 🎶")
    if st.button("🔊 Play Resonance"):
        audio.play_resonance(duration=15)
        st.success("Resonance pulse emitted.")
    if st.button("⏹ Stop Resonance"):
        audio.stop()
    st.write("Frequency Controls")
    base = st.slider("Base Frequency (Hz)", 100.0, 600.0, 136.1, step=0.1)
    audio.base_freq = base
    st.session_state.audio = audio

# --- FIELD CONTROLS TAB ---
with tabs[2]:
    st.markdown("### ψ-Field Parameters")
    zoom = st.slider("Zoom", 0.8, 1.5, 1.0228)
    harmony = st.slider("Harmony", 0.0, 1.0, 0.5)
    prana = st.slider("Prana", 0.0, 1.0, 0.5)
    st.write("Adjust to modulate ψ-field stability and coherence.")
    top_renderer.defaults.update({"harmony": harmony})
    bottom_renderer.defaults.update({"harmony": harmony})

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
            st.error("No saved state found.")            color:{color};
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
