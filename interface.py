import streamlit as st
import requests
st.title("Your personal AI Assistant💜")
st.subheader("What i can do for you")
st.markdown("""
1. Answer questions on various topics
2. Arrange outings
3. read emails
4. Manage Tasks and to do list
5. Take quick notes 
6. Track your expenses and budget 

""")
st.subheader("Chat with you assistant")

if "messages" not in st.session_state:
    st.session_state.messages =[]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):   
        st.markdown(message["content"]) 

user_msg = st.chat_input()
if user_msg:
    with st.chat_message("user"):
        st.markdown(user_msg)
        st.session_state.messages.append({"role": "user", "content": user_msg})
        response = requests.post(
            "https://squeegee-repulsion-browsing.ngrok-free.dev/webhook-test/75d82094-071a-42cb-bcf0-97a76871ab2a",
        
            json ={"message": user_msg})
        print(response.text)

        data = response.json()
        if isinstance(data, list):
            ai_response = data[0].get("json", {}).get("output", "No output found")
        else:
             ai_response = data.get("output", "No output found")    
        with st.chat_message("assistant"):
            st.markdown(ai_response)
            st.session_state.messages.append({"role": "assistant" , "content": ai_response})

