# fractal_renderer.py
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import time

class FractalRenderer:
    def __init__(self, defaults):
        self.defaults = defaults
        self.frame = 0
        self.last_render_time = 0

    def render_field(self, resonance_enabled=True):
        fig, ax = plt.subplots(figsize=(6, 6))
        ax.axis("off")
        ax.set_title("ψ-Field Visualization", color="white", fontsize=14)
        st.pyplot(fig)
        return fig

    def update(self, psi_field):
        # Add ripple animation
        t = time.time()
        shimmer = 0.2 * np.sin(t * 2) + 0.8
        wave_x = np.sin(np.linspace(0, np.pi * 4, psi_field.field.shape[0]))
        wave_y = np.cos(np.linspace(0, np.pi * 4, psi_field.field.shape[1]))
        ripple = np.outer(wave_x, wave_y)
        self.data = np.clip(psi_field.field * shimmer + ripple * 0.1, 0, 1)
        self.frame += 1

    def draw(self, canvas):
        if hasattr(self, "data"):
            cmap_list = ["inferno", "plasma", "magma", "cividis"]
            cmap = cmap_list[self.frame % len(cmap_list)]
            fig, ax = plt.subplots(figsize=(6, 6))
            ax.imshow(self.data, cmap=cmap, interpolation="bilinear")
            ax.axis("off")
            st.pyplot(fig)
