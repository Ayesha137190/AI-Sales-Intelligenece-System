import streamlit as st

def login():

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:

        st.title("🔐 AI Sales Intelligence")

        username = st.text_input("Username")

        password = st.text_input(
            "Password",
            type="password"
        )

        if st.button("Login"):

            if (
                username == "ayesha"
                and password == "15052004"
            ):

                st.session_state.logged_in = True
                st.rerun()

            else:
                st.error("Invalid Credentials")

        return False

    return True