import streamlit as st
from streamlit.cli import main
import streamlit.components.v1 as components

def main():
    components.html("""
                    <p style='color: rgb(254, 118, 216);'>STRIPEテスト</p>
                    """)
    components.iframe("https://www.google.com/maps/embed?pb=!1m17!1m12!1m3!1d631.099041517944!2d139.61888001101022!3d35.70469404992166!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m2!1m1!1s0x6018edf7419f90b5%3A0xbcbf00c045a416d4!5e0!3m2!1sja!2sjp!4v1655197129469!5m2!1sja!2sjp" ,width=600 ,height=450)
    link = "[決済](https://buy.stripe.com/test_cN2dUs0YCdFe8FieUV)"
    st.markdown(link,unsafe_allow_html=True)


if __name__ == "__main__":
    main()