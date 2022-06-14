import streamlit as st
from streamlit.cli import main
import streamlit.components.v1 as components

def main():
    st.write("STRIPEテスト")
    components.iframe("https://buy.stripe.com/14k29ngkg9GT0tW3cc")
    # link = "[決済](https://buy.stripe.com/14k29ngkg9GT0tW3cc)"
    # st.markdown(link,unsafe_allow_html=True)



if __name__ == "__main__":
    main()