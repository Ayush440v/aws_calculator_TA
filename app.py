import streamlit as st
from services.cost_calculator import calculate_costs
from utils.user_inputs import get_user_inputs
from utils.service_explanations import service_explanations
from database.db_operations import insert_costs, create_table
import pandas as pd
import plotly.express as px

# Initialize the database
create_table()

# Title of the application
st.set_page_config(page_title="AWS Cost Calculator")
st.title("AWS Costing Calculator")
st.write("This application helps you estimate the monthly costs of using AWS services for your application. Powered by TechAhead")

# User inputs
industry, features, total_users, monthly_active_users, concurrent_users, storage, streaming, media_processing, usage_type = get_user_inputs()

# Calculate costs
if st.button("Calculate Costs"):
    costs, total_cost = calculate_costs(features, total_users, monthly_active_users, concurrent_users, storage, streaming, media_processing, usage_type)
    st.divider()
    st.header("Your expected monthly AWS costs are as follows:")
    st.subheader(f"Total Monthly Cost: ${total_cost:.2f}")

    st.subheader("Cost Breakdown")

    # Display cost breakdown in a table
    cost_df = pd.DataFrame(costs.items(), columns=['Service', 'Cost'])
    st.dataframe(cost_df, hide_index=True, use_container_width=True)

    # Insert the results into the database
    insert_costs(features, total_users, monthly_active_users, concurrent_users, total_cost)

    # Plot pie chart for cost distribution
    pie_chart = px.pie(cost_df, names='Service', values='Cost', title='Cost Distribution')
    st.plotly_chart(pie_chart, use_container_width=True)