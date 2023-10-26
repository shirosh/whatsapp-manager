import streamlit as st
import requests
import json

st.set_page_config(
    page_title="Create Whatsapp Group",
    page_icon="👋",
)


st.sidebar.success("Powered by Innovation Foundry")
st.title("Create your Whatsapp Group")
st.write("Here, you can answer to some questions in this form.")

group_name= st.text_input("Put a name for your group")
admin = st.text_input("Who will be the admin. Enter your 11-digit phone number (947XXXXXXXX)", )



submit = st.button("Create")

if submit:
    #create group
    url = "https://gate.whapi.cloud/groups"

    payload = {
        "subject": group_name,
        "participants": []

        
    }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer ab9fNNPC51r8pbwW8FUuRaNv3x1SaGsK"
    }

    response = requests.post(url, json=payload, headers=headers)
    print(response.text)
    data = json.loads(response.text)

    print(data['group_id'])
    #add admin as a member
    url2 = "https://gate.whapi.cloud/groups/"+data['group_id']+"/participants"

    print(url2)

    payload2 = { "participants": [admin] }
    headers2 = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer ab9fNNPC51r8pbwW8FUuRaNv3x1SaGsK"
    }

    response = requests.post(url2, json=payload2, headers=headers2)
    print(response.text)
    #make admin
    url = "https://gate.whapi.cloud/groups/"+data['group_id']+"/admins"

    payload = { "participants": [admin] }
    headers = {
        "accept": "application/json",
        "content-type": "application/json",
        "authorization": "Bearer ab9fNNPC51r8pbwW8FUuRaNv3x1SaGsK"
    }

    response = requests.patch(url, json=payload, headers=headers)

    print(response.text)
    st.write("Congratulations! "+data['group_id']+" is created successfully. (Please Copy given group id.)")


