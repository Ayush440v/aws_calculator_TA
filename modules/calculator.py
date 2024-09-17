import streamlit as st
from services.cost_calculator import calculate_costs
from utils.user_inputs import get_user_inputs
from utils.service_explanations import service_explanations
import pandas as pd
import plotly.express as px

def aws_calulator():
    
    st.title("AWS Costing Calculator")
    st.write("An easy to use tool to estimate the monthly costs of using AWS services for your application.")

    # User inputs
    industry, features, total_users, monthly_active_users, concurrent_users, storage, streaming, media_processing, usage_type = get_user_inputs()

    # Calculate costs
    if st.button("Calculate Costs"):
        costs, total_cost, ec2_instance, rds_instance = calculate_costs(features, total_users, monthly_active_users, concurrent_users, storage, streaming, media_processing, usage_type)
        st.divider()
        st.header("Your expected monthly AWS costs are as follows:")
        st.subheader(f"Total Monthly Cost: ${total_cost:.2f}")

        st.subheader("Cost Breakdown")

        # Display cost breakdown in a table
        cost_df = pd.DataFrame(costs.items(), columns=['Service', 'Cost'])
        st.dataframe(cost_df, hide_index=True, use_container_width=True)
        
        st.subheader("Compute and Database Instance Sizes Used")
        st.write(f"EC2 Instance: {ec2_instance}")
        st.write(f"RDS Instance: {rds_instance}")
        
        st.subheader("Cost Breakdown Chart")
        fig = px.pie(cost_df, values='Cost', names='Service', title='Cost Breakdown')
        st.plotly_chart(fig)