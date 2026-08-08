import streamlit as st

a = st.number_input("숫자를 입력하세요")

if st.button("계산"):
    st.write(a ** 2)