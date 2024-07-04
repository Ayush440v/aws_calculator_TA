import streamlit as st
from assets.industry_features import industry_feature_options

def get_user_inputs():
    st.header("Select the Type of Application You Want to Build")
    
    industry = st.selectbox(
        "Choose the industry of your application",
        ["Social Media", "E-Commerce", "Media Streaming", "Healthcare", "Fintech", "On-Demand Services"]
    )
    
    features = st.multiselect(
        "Select features for your application",
        industry_feature_options[industry]
    )

    st.header("Define Your User Metrics")

    total_users = st.number_input("Total Users", min_value=1, value=1000, step=100)
    monthly_active_users = st.number_input("Monthly Active Users", min_value=1, value=500, step=50)
    concurrent_users = st.number_input("Concurrent Users", min_value=1, value=50, step=5)

    storage = 0
    streaming = 0
    media_processing = 0

    if "Storage" in features:
        storage = st.number_input("Storage (in GB)", min_value=1, value=100, step=10)

    if "Video Streaming" in features:
        streaming = st.number_input("Streaming (in hours)", min_value=1, value=10, step=1)

    if "Media Processing" in features:
        media_processing = st.number_input("Media Processing (in hours)", min_value=1, value=10, step=1)

    return industry, features, total_users, monthly_active_users, concurrent_users, storage, streaming, media_processing
