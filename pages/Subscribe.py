import streamlit as st
import requests
import json

st.set_page_config(
    page_title="Subscribe",
    page_icon="👋",
)

st.write("# Subscribe to Whatsapp Group")

st.sidebar.success("Powered by Innovation Foundry.")
st.write("Subscription: Rs.100/month")
group_id= st.text_input("Enter Group ID")
member = st.text_input("Enter your 11-digit phone number (947XXXXXXXX)")


submit = st.button("Subscribe")

if submit:
    url2 = "https://gate.whapi.cloud/groups/"+group_id+"/participants"

    print(url2)

    payload2 = { "participants": [member] }
    headers2 = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer ab9fNNPC51r8pbwW8FUuRaNv3x1SaGsK"
    }

    response = requests.post(url2, json=payload2, headers=headers2)
    print(response.text)
    st.write("Congratulations! you have added to the group.")
    