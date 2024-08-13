import os

import streamlit as st
from streamlit_navigation_bar import st_navbar


pages = ["Chargers", "Transactions", "Meter Vaules", "Support", "Search"]
dir=os.path.dirname(os.path.abspath(__file__))
logo_path=os.path.join(dir, "MB-star_n_web.svg")
styles = {
    "nav": {
        "background-color": "rgba(22, 22, 23, 80%)",
    },
    "div": {
        "max-width": "50rem",
    },
    "span": {
        "border-radius": "0.5rem",
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
st.write(page)

