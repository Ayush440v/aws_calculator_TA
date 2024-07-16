feature_service_mapping = {
    "Login-Signup": ["Cognito"],
    "Profile Management": ["Lambda", "RDS"],
    "Image Post": ["S3", "Lambda", "RDS"],
    "Video Post": ["S3", "MediaLive", "Lambda", "RDS"],
    "Text Post": ["Lambda", "RDS"],
    "Live Streaming": ["MediaLive"],
    "Chat": ["Lambda", "DynamoDB"],
    "Comments": ["Lambda", "DynamoDB"],
    "Likes": ["Lambda", "DynamoDB"],
    "Sharing": ["Lambda"],
    "Notifications": ["SNS", "EC2"],
    "Search and Filters": ["Lambda", "ElasticSearch", "RDS"],
    "Product Listings": ["Lambda"],
    "Shopping Cart": ["Lambda", "RDS"],
    "Checkout": ["Lambda", "RDS"],
    "Payment Gateway": ["API Gateway", "Lambda", "RDS"],
    "Order Tracking": ["Lambda"],
    "User Reviews": ["Lambda","RDS"],
    "Wishlist": ["Lambda", "RDS"],
    "Appointment Scheduling": ["EC2", "RDS"],
    "Telemedicine": ["EC2", "RDS"],
    "EHR Integration": ["EC2", "RDS"],
    "Payment Processing": ["API Gateway", "Lambda", "RDS"],
    "Account Management": ["Lambda", "RDS"],
    "Investment Tracking": ["EC2", "RDS"],
    "Service Listings": ["Lambda"],
    "Booking System": ["EC2", "RDS"],
}

service_costs = {
    "Cognito": lambda users: 0.005 * users,
    "RDS": lambda total_users, concurrent_users: 0.02 * concurrent_users + 0.01 * total_users,
    "S3": lambda storage: 0.023 * storage,
    "EC2": lambda concurrent_users: 0.1 * concurrent_users,
    "MediaLive": lambda streaming: 0.5 * streaming,
    "MediaConvert": lambda media_processing: 0.3 * media_processing,
    "SNS": lambda notifications: 0.01 * notifications,
    "API Gateway": lambda total_users: 0.0035 * total_users,
    "Lambda": lambda requests: 0.00001667 * requests,
    "DynamoDB": lambda requests: 0.0065 * requests,
}

usage_requests_per_day = {
    "Low": 10,
    "Medium": 25,
    "High": 100
}

def calculate_costs(features, total_users, monthly_active_users, concurrent_users, storage, streaming, media_processing, usage_type):
    costs = {}
    for feature in features:
        services = feature_service_mapping.get(feature, [])
        for service in services:
            if service not in costs:
                costs[service] = 0
            if service == "Cognito":
                costs[service] += service_costs[service](monthly_active_users)
            elif service == "RDS":
                costs[service] += service_costs[service](total_users, concurrent_users)
            elif service == "S3":
                costs[service] += service_costs[service](storage)
            elif service == "EC2":
                costs[service] += service_costs[service](concurrent_users)
            elif service == "MediaLive":
                costs[service] += service_costs[service](streaming)
            elif service == "MediaConvert":
                costs[service] += service_costs[service](media_processing)
            elif service == "SNS":
                costs[service] += service_costs[service](monthly_active_users)  # Assuming notifications equal to monthly active users
            elif service == "API Gateway":
                costs[service] += service_costs[service](total_users)
            elif service == "DynamoDB":
                daily_requests = usage_requests_per_day.get(usage_type, 10)
                monthly_requests = daily_requests * 30
                costs[service] += service_costs[service](monthly_requests)
            elif service == "Lambda":
                daily_requests = usage_requests_per_day.get(usage_type, 10)
                monthly_requests = daily_requests * 30
                costs[service] += service_costs[service](monthly_requests)

    total_cost = sum(costs.values())
    return costs, total_cost
