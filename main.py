import streamlit as st
from streamlit_option_menu import option_menu
import about, Dashboard, ExpenseTracker, Analytics, knowledgebytes, account
st.set_page_config(page_title= "Personal Finance Tracker"),
class MultiApp:
    def __init__(self):
        self.apps = []
    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        with st.sidebar:
             app = option_menu(
                menu_title='Menu',
                options=['Account', 'ExpenseTracker', 'Dashboard', 'Analytics', 'Knowledge Bytes','About'],
                icons=['person-circle', 'bi bi-graph-up', 'house-fill', 'bi bi-bar-chart-fill', 'trophy-fill','info-circle-fill'],
                menu_icon='chat-text-fill',
                default_index=0,
                styles={
                    "container": {"padding": "5!important","background-color":'black'},
        "icon": {"color": "white", "font-size": "23px"}, 
        "nav-link": {"color":"white","font-size": "20px", "text-align": "left", "margin":"0px", "--hover-color": "blue"},
        "nav-link-selected": {"background-color": "#02ab21"},})
        if app == "Account":
            account.app()
        if app == "ExpenseTracker":
            ExpenseTracker.app()
        if app == "Dashboard":
            Dashboard.app() 
        if app == "Analytics":
            Analytics.app()          
        if app == "Knowledge Bytes":
            knowledgebytes.app()
        if app == 'About':
            about.app()

if __name__ == "__main__":
    multi_app = MultiApp()
    multi_app.run()