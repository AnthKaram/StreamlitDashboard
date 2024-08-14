import os

import streamlit as st
from streamlit_navigation_bar import st_navbar

dir=os.path.dirname(os.path.abspath(__file__))
logo_path=os.path.join(dir, "MB-star_n_web.svg")

st.set_page_config(
    page_title="CSMS Dashboard",
    page_icon=logo_path,
    layout="wide",
)

pages = ["Chargers", "Transactions", "Meter Vaules", "Support", "Search"]


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
        "color":"rgb(211, 33, 40)",
        "font-size":"18px",
    },
    "hover": {
        "color":"rgb(211, 33, 40)",
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
            background-image: url("https://static0.carbuzzimages.com/wordpress/wp-content/uploads/gallery-images/original/835000/800/835890.jpg");
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

def search_menu():
    st.text_input(" ", "Search", key="placeholder")

functions = {
    "Home": add_bg_from_local,
    "Search": search_menu,
}
go_to = functions.get(page)
if go_to :
    go_to()
