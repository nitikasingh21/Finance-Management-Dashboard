import streamlit as st
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

cred = credentials.Certificate('personal-finance-tracker-122c9-b652780caaa6.json')
firebase_admin.initialize_app(cred)

def app():
    st.title('Welcome to Your Finance Tracker Dashboard 📈')

    if 'username' not in st.session_state:
        st.session_state.username = ''
    if 'useremail' not in st.session_state:
        st.session_state.useremail = ''
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False
    if 'page' not in st.session_state:
        st.session_state.page = ''

    def f():
        try:
            user = auth.get_user_by_email(email)
            print(user.uid)
            st.session_state.username = user.uid
            st.session_state.useremail = user.email
            st.session_state.logged_in = True
            st.session_state.page = 'ExpenseTracker'
            global username
            Usernm = (user.uid)
            st.session_state.signout = True
        except:
            st.warning('Login Failed')

    def t():
        st.session_state.signout = False
        st.session_state.username = ''
        st.session_state.logged_in = False
        st.session_state.page = ''

    if not st.session_state.logged_in:
        choice = st.selectbox('Login/ Signup', ['Login', 'Sign up'])
        email = st.text_input('Email Address', key="email_input")
        password = st.text_input('Password', type='password', key="password_input")

        if choice == 'Login':
            st.button('Login', on_click=f)
        else:
            username = st.text_input('Enter your username')

            if st.button('Create my account'):
                user = auth.create_user(email=email, password=password, uid=username)
                st.success('Account created successfully :)')
                st.markdown('Please Login using your email and password')
                st.balloons()

    if st.session_state.signout:
        st.text('Username: ' + st.session_state.username)
        st.button('Sign Out', on_click=t)

    if st.session_state.logged_in and st.session_state.page == 'ExpenseTracker':
        import ExpenseTracker
        ExpenseTracker.app()