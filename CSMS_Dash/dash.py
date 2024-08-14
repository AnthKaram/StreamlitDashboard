import os

import streamlit as st
from streamlit_navigation_bar import st_navbar

pages = ["Chargers", "Transactions", "Meter Vaules", "Support", "\u2315"]
dir=os.path.dirname(os.path.abspath(__file__))
logo_path=os.path.join(dir, "MB-star_n_web.svg")

styles = {
    "nav": {
        "background-color":"rgb(0,0,0)"
    },
    "div": {
        "max-width": "35rem",
    },
    "span": {
        "border-radius": "0.9rem",
        "font-size":"15px",
        "color": "rgba(255, 255, 255, 0.8)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
        "transition": "color, 0.2s",
    },
    "active": {
        "color":"white",
    },
    "hover": {
        "color":"white",
    },
}

page = st_navbar(pages,
                 logo_path=logo_path,
                 styles=styles)

def add_bg_from_local():
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://www.motortrend.com/uploads/2021/12/2021-Mercedes-AMG-G63-27.jpg?w=512&width=512&q=75&format=webp");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local()
