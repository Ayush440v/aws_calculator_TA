import streamlit as st
from assets.industry_features import industry_feature_options

def get_user_inputs():
    st.divider()
    st.header("Project Specifications")
    
    industry = st.selectbox(
        "Choose the industry of your Project",
        ["Social Media", "E-Commerce", "Media Streaming", "Healthcare", "Fintech", "On-Demand Services", "IoT", "Real-Estate", "Education", "Travel", "ERP"]
    )
    
    features = st.multiselect(
        "Select features for your Project (You can only select one)",
        industry_feature_options[industry]
    )

    st.header("Define Your User Metrics")

    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_users = st.number_input("Total Users", min_value=1, value=1000, step=100)
    
    with col2:
        monthly_active_users = st.number_input("Monthly Active Users", min_value=1, value=500, step=50)
    
    with col3:
        concurrent_users = st.number_input("Concurrent Users", min_value=1, value=50, step=5)

    st.header("Specify Your Usage Type")
    
    ccol1, ccol2 = st.columns(2)
    
    with ccol1:
        usage_type = st.selectbox("Select usage type for your application", ["Low", "Medium", "High"])

    storage = 0
    streaming = 0
    media_processing = 0
    
    with ccol2:

        if "Image Post" in features or "Video Post" in features:
            storage = st.number_input("Storage (in GB)", min_value=1, value=100, step=10)

        if "Live Streaming" in features:
            streaming = st.number_input("Streaming (in hours)", min_value=1, value=10, step=1)

        if "Media Processing" in features:
            media_processing = st.number_input("Media Processing (in hours)", min_value=1, value=10, step=1)

    return industry, features, total_users, monthly_active_users, concurrent_users, storage, streaming, media_processing, usage_type
