import streamlit as st
import pandas as pd
import plotly.express as px
import os
import warnings

warnings.filterwarnings('ignore')


def app():
    st.write('Expense Tracker Dashboard')
    st.title(":chart_with_upwards_trend: Expense Tracker")
    # Input fields for income and expenses
    income = st.number_input('Enter your income:', min_value=0.0)
    expenses = st.number_input('Enter your total expenses:', min_value=0.0)

    # Calculate savings
    savings = income - expenses

    # Display income, expenses, and savings
    st.write(f"Total Income: Rs.{income}")
    st.write(f"Total Expenses: Rs.{expenses}")
    st.write(f"Savings: Rs.{savings}")

    # Visualization: Line chart to show expenses breakdown
    if expenses > 0:
        expense_categories = st.multiselect('Select expense categories:', ['Food', 'Transportation', 'Housing', 'Entertainment', 'Utilities', 'Others'])
        if expense_categories:
            # Ask user for amounts spent in selected categories
            amounts_spent = {}
            for category in expense_categories:
                amount = st.number_input(f'How much did you spend on {category}?', min_value=0.0, max_value=expenses, key=category)
                amounts_spent[category] = amount

            # Categories with non-zero amounts spent
            selected_categories = [category for category, amount in amounts_spent.items() if amount > 0]

            if selected_categories:
                # Generate expenses data based on selected categories and amounts spent
                expenses_data = pd.DataFrame({
                    'Category': selected_categories,
                    'Amount Spent': [amounts_spent[category] for category in selected_categories]
                })

                # Plot expenses breakdown as a bar chart
                fig_expenses = px.bar(expenses_data, x='Category', y='Amount Spent', title='Expenses Breakdown')
                st.plotly_chart(fig_expenses)

                # Line chart to show spending pattern
                fig_spending_pattern = px.line(expenses_data, x='Category', y='Amount Spent', title='Spending Pattern')
                st.plotly_chart(fig_spending_pattern)
            else:
                st.warning('Please enter amounts spent for selected categories.')
        else:
            st.warning('Please select at least one expense category.')