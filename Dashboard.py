import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import os

def app():
    st.write('Dashboard')
    st.title(":chart_with_upwards_trend: Dashboard")
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

    data_df = pd.DataFrame()

    fl = st.file_uploader(":file_folder: Upload your data", type=(["csv", "txt", "xlsx", "xls"]))
    if fl is not None:
        filename = fl.name
        st.write(filename)
        df = pd.read_csv(filename, encoding="ISO-8859-1")
    else:
        os.chdir(r"D:\College\Projects\Minor")
        df = pd.read_csv("Expenses", encoding="ISO-8859-1")

    # Strip spaces from column names
    df.columns = df.columns.str.strip()
    
    categories = ['Rent', 'Groceries', 'Stationary', 'Transportation', 'Food']
    selected_category = st.selectbox('Select Expense Category', categories)
    
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

    if selected_category == 'Rent':
        rent_columns = [f'Rent_{month}' for month in months]
        if all(column in df.columns for column in rent_columns):
            st.write(df[rent_columns])
            fig, ax = plt.subplots()
            ax.plot(months, df[rent_columns].values[0])
            ax.set_title('Rent Expenditure Over Months')
            ax.set_xlabel('Month')
            ax.set_ylabel('Amount')
            ax.set_xticklabels(months, rotation=45)
            st.pyplot(fig)

    elif selected_category == 'Groceries':
        groceries_columns = [f'Groceries_{month}' for month in months]
        if all(column in df.columns for column in groceries_columns):
            st.write(df[groceries_columns])
            fig, ax = plt.subplots()
            ax.plot(months, df[groceries_columns].values[0])
            ax.set_title('Groceries Expenditure Over Months')
            ax.set_xlabel('Month')
            ax.set_ylabel('Amount')
            ax.set_xticklabels(months, rotation=45)
            st.pyplot(fig)

    elif selected_category == 'Stationary':
        stationary_columns = [f'Stationary_{month}' for month in months]
        if all(column in df.columns for column in stationary_columns):
            st.write(df[stationary_columns])
            fig, ax = plt.subplots()
            ax.plot(months, df[stationary_columns].values[0])
            ax.set_title('Stationary Expenditure Over Months')
            ax.set_xlabel('Month')
            ax.set_ylabel('Amount')
            ax.set_xticklabels(months, rotation=45)
            st.pyplot(fig)

    elif selected_category == 'Transportation':
        transportation_columns = [f'Transportation_{month}' for month in months]
        if all(column in df.columns for column in transportation_columns):
            st.write(df[transportation_columns])
            fig, ax = plt.subplots()
            ax.plot(months, df[transportation_columns].values[0])
            ax.set_title('Transportation Expenditure Over Months')
            ax.set_xlabel('Month')
            ax.set_ylabel('Amount')
            ax.set_xticklabels(months, rotation=45)
            st.pyplot(fig)

    elif selected_category == 'Food':
        food_columns = [f'Food_{month}' for month in months]
        if all(column in df.columns for column in food_columns):
            st.write(df[food_columns])
            fig, ax = plt.subplots()
            ax.plot(months, df[food_columns].values[0])
            ax.set_title('Food Expenditure Over Months')
            ax.set_xlabel('Month')
            ax.set_ylabel('Amount')
            ax.set_xticklabels(months, rotation=45)
            st.pyplot(fig)












# import pandas as pd
# import matplotlib.pyplot as plt
# import streamlit as st
# import os

# def app():
#     st.write('Dashboard')
#     st.title(":chart_with_upwards_trend: Dashboard")
#     st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)

#     data_df = pd.DataFrame()

#     fl = st.file_uploader(":file_folder: Upload your data", type=(["csv", "txt", "xlsx", "xls"]))
#     if fl is not None:
#         filename = fl.name
#         st.write(filename)
#         df = pd.read_csv(filename, encoding="ISO-8859-1")
#     else:
#         os.chdir(r"D:\College\Projects\Minor")
#         df = pd.read_csv("Expenses", encoding="ISO-8859-1")

#     # Strip spaces from column names
#     df.columns = df.columns.str.strip()
    
#     categories = ['Rent', 'Groceries', 'Stationary', 'Transportation', 'Food']
#     selected_category = st.selectbox('Select Expense Category', categories)
    
#     months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

#     if selected_category == 'Rent':
#         rent_columns = [f'Rent_{month}' for month in months]
#         if all(column in df.columns for column in rent_columns):
#             st.write(df[rent_columns])
#         else:
#             st.write("Error: Rent columns not found in the dataset.")

#     elif selected_category == 'Groceries':
#         groceries_columns = [f'Groceries_{month}' for month in months]
#         if all(column in df.columns for column in groceries_columns):
#             st.write(df[groceries_columns])
#         else:
#             st.write("Error: Groceries columns not found in the dataset.")

#     elif selected_category == 'Stationary':
#         Stationary_columns = [f'Stationary_{month}' for month in months]
#         print("Stationary columns:", Stationary_columns)
#         print("All columns in DataFrame:", df.columns.tolist())
#         if all(column in df.columns for column in Stationary_columns):
#             st.write(df[Stationary_columns])
#         else:
#             st.write("Error: Stationary columns not found in the dataset.")

#     # elif selected_category == 'Stationary':
#     #     stationary_columns = [f'Stationary_{month}' for month in months]
#     #     if all(column in df.columns for column in stationary_columns):
#     #         st.write(df[stationary_columns])
#     #     else:
#     #         st.write("Error: Stationary columns not found in the dataset.")

#     elif selected_category == 'Transportation':
#         transportation_columns = [f'Transportation_{month}' for month in months]
#         if all(column in df.columns for column in transportation_columns):
#             st.write(df[transportation_columns])
#         else:
#             st.write("Error: Transportation columns not found in the dataset.")

#     elif selected_category == 'Food':
#         food_columns = [f'Food_{month}' for month in months]
#         if all(column in df.columns for column in food_columns):
#             st.write(df[food_columns])
#         else:
#             st.write("Error: Food columns not found in the dataset.")
  
