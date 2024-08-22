import os

import streamlit as st
from streamlit_navigation_bar import st_navbar
import pandas as pd

dir=os.path.dirname(os.path.abspath(__file__))
logo_path=os.path.join(dir, "MB-star_n_web.svg")	#Mercedes Logo

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
        "font-size":"15px",
        "color": "rgba(255, 255, 255, 0.8)",
        "margin": "0 0.125rem",
        "padding": "0.4375rem 0.625rem",
        "transition": "color, 0.4s",
    },
    "active": {
        "color":"rgb(211, 33, 40)",
        "font-size":"16.5px",
        "font-weight":"normal",
    },
    "hover": {
        "color":"rgb(211, 33, 40)",
    },
}

page = st_navbar(pages,
                 logo_path=logo_path,
                 styles=styles)
                 
st.markdown(f"""
	<style>.stApp{{font-family: Arial;}}</style>
""", unsafe_allow_html=True)

def add_bg_from_local():
    html_string ="<blockquote style=\"font-size: 32px;\"><b> <i> THE BEST OR NOTHING </i></b> </blockquote>"
    st.markdown(html_string, unsafe_allow_html=True)
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("https://static0.carbuzzimages.com/wordpress/wp-content/uploads/gallery-images/original/835000/800/835890.jpg");
            background-color: rgb(0,0,0);
            background-size: cover;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
    
def ChargerTab():
    st.markdown(
        f"""
            <div class="Grid">
            
            <div class="gridtitle">Charger</div>
            <div class="gridtitle">Meter Values</div>
 
            <div>WallBox</div>
            <div>95 kW</div>
            
            <div>Borgwarner</div>
            <div>100 kW</div>
            
    
            </div>
            
            
            <style>
            .stApp{{
                
                background-image: url("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjiwC-Tif0OCHlPtEHcVmpRC8QC70R35LMlH5lMN7AkKYaOtZuhYRsSDdF6SGUTPjn2CirvgpsOEdxOxMu7Dfol6Ql-vcEpuElYYZCd-giSKrwrnpNGIpWvE-CmGY7BbYKyzrxjw1yioCUbHx74Wi0UOH_vcYEsqDYcw3v9c-tb_k-yITj8B4oTrae1tibL/s16000/victor-sutty-Sv0AxtA8YxI-unsplash.jpg");
              	background-color: rgba(0,0,0); 
                background-size: cover;
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
                color: rgb(181,186,189);
                margin-bottom: 8px;
            }}
            
            </style>
            """,
            
        unsafe_allow_html=True
    )


def SearchTab():
    sheet_id= "1LXxC94iQ0-M_MT32Cr4pa9WFvfwC0jsG0tua_H0xz00"
    sheet_name="EVCharger"
    url= f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    df=pd.read_csv(url,dtype=str)
    Txt_search=st.text_input(" ", placeholder="Search by Transaction Date, Transaction ID, and Charger Name", value="")
    m1= df["Chargers"].str.contains(Txt_search)
    m2= df["TransactionID"].str.contains(Txt_search)
    m3= df["TransactionDate"].str.contains(Txt_search)
    df_search=df[m1 | m2 | m3]
    df_search = df.loc[:, ~df_search.columns.str.contains('^Unnamed','Chargers')]
    #df_search = df_search.drop(['Chargers','price'],axis=1) remove columns
    if Txt_search:
        st.write(df_search)







def TransactionsTab():
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
                <div>90 kW</div>
                <div>$50</div>
                <div>1 Hour</div>
                
                <div>202</div>
                <div>28-8-24</div>
                <div>65 kW</div>
                <div>$30</div>
                <div>45 Minutes</div>
                
                </div>

                <style>
                .stApp{{
                   background-image: url("https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJTxnU-BU_zSA-ko8K56pKh1_WseIFpYsaZzQwqeGzVTz1rSRqGF1KhU88zJPDO0oGj0anBUKtQ4XlDYS8h_y-3z_BuHnuktxIPFOapoFWtkinJ4rkpg9KRJqeHN8HeHm74L_nf3wy6FYrEC3yYSvungEyYqjtjXhjB6gdvEy46_t0zH0OrdV3Vgk0oNFP/s16000/70fde993027339.5e5a54de6362e.jpg");
                   background-color: rgba(0,0,0); 
                   background-size: cover;



                }}

                .Grid{{
                		display:grid;
                		grid-template-columns: auto auto auto auto auto ;

                		text-align: center;
                		color:rgba(255, 255, 255, 0.8);
                	}}
                
                .gridtitle{{
                		font-size: 25px;
               		font-weight: bold;
                		color: rgb(181,186,189);
                		margin-bottom: 8px;
                }}

                </style>
                """,
        unsafe_allow_html=True
    )


def SupportTab():
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
    "Search": SearchTab,
    "Support": SupportTab,
    "Chargers": ChargerTab,
    "Transactions": TransactionsTab,
}
go_to = functions.get(page)
if go_to :
    go_to()





