# fractal_renderer.py
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

class FractalRenderer:
    def __init__(self, defaults):
        self.defaults = defaults

    def render_field(self, resonance_enabled=True):
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.axis("off")
        ax.set_title("ψ-Field Visualization", color="white", fontsize=14)
        st.pyplot(fig)
        return fig

    def update(self, psi_field):
        self.data = psi_field.field

    def draw(self, canvas):
        if hasattr(self, "data"):
            fig, ax = plt.subplots(figsize=(6, 6))
            ax.imshow(self.data, cmap="inferno", interpolation="nearest")
            ax.axis("off")
            st.pyplot(fig)
