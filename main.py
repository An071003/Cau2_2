import streamlit as st
import time
import webbrowser as wb
st.title('Đăng nhập')
username = st.text_input('Username', '')
password = st.text_input('Password', '', type='password')
if st.button('Đăng nhập'):
    if username == '21521804' and password == '21521804':
        st.success('Đăng nhập thành công')
        time.sleep(3)
        wb.open('http://www.uit.edu.vn/')
    else:
        st.error('Sai username hoặc password')
