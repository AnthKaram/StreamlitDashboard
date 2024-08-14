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
        "color":"rgb(247, 9, 38)",
    },
    "hover": {
        "color":"rgb(247, 9, 38)",
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
            background-image: url("https://www.mercedes-benz.com/content/dam/brandhub/assets/exclusive/private-lounges/amg-private-lounge/amg-private-lounge-2024/paul-ricard_03.cbv20240516093945.jpg/_jcr_content/renditions/mq3-original-aspect.jpeg");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

add_bg_from_local()
