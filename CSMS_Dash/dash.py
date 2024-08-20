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
def ChargerInfo():
    st.markdown(
        f"""
            <div class="Grid">
            <div class="gridtitle">Charger</div>
            
            <div class="gridtitle">Meter Values</div>
            
            <div>WallBox</div>
            
            <div>95KW</div>
            
            <div>Flower</div>
            
            <div>100KW</div>
            
    
            </div>
            
            <style>
            .stApp{{
                 background-image: url("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWHAv7yfaejyXBt__hdkQmeWY6lt3Rn51OVGzDX3xsageZfhaeX8lUj36R5XW6acKMeMYoCo2jONj-qc1yrPuNFtSJnEyqtNq59zYwv_h1mXvkc83_49MoExZfzHTkVKmbhWF_pCJUwzFyr4Luh0ljsRwM_Qb2PuFIQQRzV_-22pb5IbQsMXbYkYdLp9WJ/s16000/Screen%20Shot%202024-08-20%20at%2012.39.43%20PM.png");
                background-size: cover;  
               background-color: rgba(255, 255, 255, 0.8); 
              
                       
            
            }}
            
            .Grid{{
            display:grid;
            grid-template-columns: auto auto;
            
            text-align: center;
            color:rgba(255, 255, 255, 0.8);
            font-family: Arial;
            
            }}
            .gridtitle{{
            font-size: 25px;
            font-weight: bold;
            color: rgb(211, 33, 40);
            margin-bottom: 8px;
            }}
            
            </style>
            """,
        unsafe_allow_html=True
    )



def search_menu():
    st.text_input(" ", placeholder="Search")

def Receipt():
    st.markdown(
        f"""
                <div class="Grid">
                <div class="gridtitle">Transaction ID</div>
                <div class="gridtitle">Dates</div>
                <div class="gridtitle">Meter Value</div>
                <div class="gridtitle">Price</div>
                <div class="gridtitle">Duration</div>


                <div>201</div>
                <div>28-8-24</div>
                <div>90KM</div>
                <div>$50</div>
                <div>1 Hour</div>
                <div>202</div>
                <div>28-8-24</div>
                <div>65KM</div>
                <div>$30</div>
                <div>45 Minutes</div>
                


                </div>

                <style>
                .stApp{{
                     background-image: url("https://mir-s3-cdn-cf.behance.net/project_modules/max_3840/70fde993027339.5e5a54de6362e.jpg");
                    background-size: cover;  
                   background-color: rgba(255, 255, 255, 0.8); 



                }}

                .Grid{{
                display:grid;
                grid-template-columns: auto auto auto auto auto ;

                text-align: center;
                color:rgba(255, 255, 255, 0.8);
                font-family: Arial;

                }}
                .gridtitle{{
                font-size: 25px;
                font-weight: bold;
                color: rgb(211, 33, 40);
                margin-bottom: 8px;
                }}

                </style>
                """,
        unsafe_allow_html=True
    )


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
    "Chargers": ChargerInfo,
    "Transactions": Receipt,
}
go_to = functions.get(page)
if go_to :
    go_to()





