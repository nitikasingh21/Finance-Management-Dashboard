import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import pandas as pd
import os
import csv
import warnings
warnings.filterwarnings('ignore')
def app():
    st.write('Analytics')
    st.title(":chart_with_upwards_trend: Expense Tracker")
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

    data_df = pd.DataFrame()

    fl = st.file_uploader(":file_folder: Upload your data", type=(["csv", "txt", "xlsx", "xls"]))
    if fl is not None:
        filename = fl.name
        st.write(filename)
        data_df = pd.read_csv(filename, encoding="ISO-8859-1")
    else:
        os.chdir(r"D:\College\Projects\Minor")
        data_df = pd.read_csv("Financial_Survey", encoding="ISO-8859-1")

    
    if not data_df.empty:
        # Example: Age Group Analysis - Bar Chart
        st.subheader('Age Group Analysis')
        age_groups = data_df['Age'].value_counts().reset_index()
        age_groups.columns = ['Age', 'Count']
        fig_age_groups = px.bar(age_groups, x='Age', y='Count', title='Distribution by Age Group')
        st.plotly_chart(fig_age_groups)

        # Example: Gender Analysis - Pie Chart
        st.subheader('Gender Analysis')
        gender_counts = data_df['Gender'].value_counts().reset_index()
        gender_counts.columns = ['Gender', 'Count']
        fig_gender = px.pie(gender_counts, values='Count', names='Gender', title='Gender Distribution')
        st.plotly_chart(fig_gender)

        # Example: Financial Literacy Analysis - Bar Chart
        st.subheader('Financial Literacy Analysis')
        financial_literacy = data_df['Financial Literacy Level'].value_counts().reset_index()
        financial_literacy.columns = ['Financial Literacy Level', 'Count']
        fig_financial_literacy = px.bar(financial_literacy, x='Financial Literacy Level', y='Count', title='Financial Literacy Levels')
        st.plotly_chart(fig_financial_literacy)

        # Example: Budgeting Habits Analysis - Pie Chart
        st.subheader('Budgeting Habits Analysis')
        budgeting_habits = data_df['Budgeting Habit'].value_counts().reset_index()
        budgeting_habits.columns = ['Budgeting Habit', 'Count']
        fig_budgeting_habits = px.pie(budgeting_habits, values='Count', names='Budgeting Habit', title='Budgeting Habit')
        st.plotly_chart(fig_budgeting_habits)

        # Example: Applications for Budget Tracking - Pie Chart
        st.subheader('Applications for Budget Tracking')
        tool_usage_counts = data_df['What tools do you use ?'].value_counts().reset_index()
        tool_usage_counts.columns = ['Tool', 'Count']
        st.markdown("##")
        fig_tool_usage = px.pie(tool_usage_counts, values='Count', names='Tool')
        st.plotly_chart(fig_tool_usage)