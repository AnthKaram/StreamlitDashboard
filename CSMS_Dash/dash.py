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

pages = ["Chargers", "Transactions", "Support", "Search"]


styles = {
    "nav": {
        "background-color":"rgb(0,0,0)"
    },
    "div": {
        "max-width": "25rem",
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
    html_string ="<blockquote style=\"font-size: 32px;\"><b> <i> THE BEST OR NOTHING </i></b> </blockquote>"
    st.markdown(html_string, unsafe_allow_html=True)
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
    st.text_input(" ", placeholder="Search")

def supportus():
    st.markdown("### Charging Support\n")

    st.markdown("**Welcome to our Charging Support Center!**\n")

    st.markdown(
        "We're here to ensure that your electric vehicle charging experience is smooth and hassle-free. Whether you're charging at home or on the go, our support team is ready to assist you with any questions or issues you may encounter.\n")

    st.markdown("**Common Topics:**\n")
    st.markdown(
        "- **Setting Up Your Charger:** Step-by-step guides to help you install and configure your home charging station.")
    st.markdown(
        "- **Troubleshooting:** Solutions for common charging problems, such as slow charging, connectivity issues, or power interruptions.")
    st.markdown(
        "- **Public Charging:** Tips on finding and using public charging stations, including information on network memberships and payment options.")
    st.markdown(
        "- **Billing and Payments:** Detailed explanations of our billing process, how to view your usage, and understanding your payment options.\n")

    st.markdown("**Contact Us:**\n")
    st.markdown("- **Phone:** (+961) 01 255 366")
    st.markdown("- **Address:** Mercedes-Benz Building, Dora Highway, Beirut")
    st.markdown(
        "Our support team is available Monday through Friday, 9 AM to 6 PM PST. Don’t hesitate to reach out if you need help—your satisfaction is our top priority!")


functions = {
    "Home": add_bg_from_local,
    "Search": search_menu,
    "Support": supportus,
}
go_to = functions.get(page)
if go_to :
    go_to()





