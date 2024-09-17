feature_service_mapping = {
    "Login-Signup": ["Cognito", "API Gateway"],  # Added API Gateway
    "Profile Management": ["Lambda", "RDS", "API Gateway"],  # Added API Gateway
    "Image Post": ["S3", "Lambda", "RDS", "API Gateway"],  # Added API Gateway
    "Video Post": ["S3", "MediaLive", "Lambda", "RDS", "API Gateway"],  # Added API Gateway
    "Text Post": ["Lambda", "RDS", "API Gateway"],  # Added API Gateway
    "Live Streaming": ["MediaLive", "API Gateway"],  # Added API Gateway
    "Chat": ["Lambda", "DynamoDB", "API Gateway"],  # Added API Gateway
    "Comments": ["Lambda", "DynamoDB", "API Gateway"],  # Added API Gateway
    "Likes": ["Lambda", "DynamoDB", "API Gateway"],  # Added API Gateway
    "Sharing": ["Lambda", "API Gateway"],  # Added API Gateway
    "Notifications": ["SNS", "API Gateway"],  # Added API Gateway
    "Search and Filters": ["Lambda", "RDS", "API Gateway"],  # Added API Gateway
    "Product Listings": ["Lambda", "API Gateway"],  # Added API Gateway
    "Shopping Cart": ["Lambda", "RDS", "API Gateway"],  # Added API Gateway
    "Checkout": ["Lambda", "RDS", "API Gateway"],  # Added API Gateway
    "Payment Gateway": ["API Gateway", "Lambda", "RDS"],  # Already present
    "Order Tracking": ["Lambda", "API Gateway"],  # Added API Gateway
    "User Reviews": ["Lambda", "RDS", "API Gateway"],  # Added API Gateway
    "Wishlist": ["Lambda", "RDS", "API Gateway"],  # Added API Gateway
    "Appointment Scheduling": ["EC2", "RDS", "API Gateway"],  # Added API Gateway
    "Telemedicine": ["EC2", "RDS", "API Gateway"],  # Added API Gateway
    "EHR Integration": ["EC2", "RDS", "API Gateway"],  # Added API Gateway
    "Payment Processing": ["API Gateway", "Lambda", "RDS"],  # Already present
    "Account Management": ["Lambda", "RDS", "API Gateway"],  # Added API Gateway
    "Investment Tracking": ["EC2", "RDS", "API Gateway"],  # Added API Gateway
    "Service Listings": ["Lambda", "API Gateway"],  # Added API Gateway
    "Booking System": ["EC2", "RDS", "API Gateway"],  # Added API Gateway
}

service_costs = {
    "Cognito": lambda users: 0.0055 * users,  # Updated to $0.0055 per user
    "RDS": lambda total_users, concurrent_users: 0.02 * concurrent_users + 0.01 * total_users,  # Needs further adjustment based on instance type
    "S3": lambda storage: 0.023 * storage,  # Correct
    "EC2": lambda concurrent_users: 0.1 * concurrent_users,  # Needs adjustment based on instance type
    "MediaLive": lambda streaming: 0.5 * streaming,  # Needs adjustment based on resolution
    "MediaConvert": lambda media_processing: 0.3 * media_processing,  # Needs adjustment based on tier
    "SNS": lambda notifications: 0.0000005 * notifications,  # Updated to $0.0000005 per notification
    "API Gateway": lambda total_users: 0.0000035 * total_users,  # Updated to $0.0000035 per request
    "Lambda": lambda requests: 0.0000002 * requests,  # Updated to $0.0000002 per request
    "DynamoDB": lambda requests: 0.00000125 * requests,  # Updated to $0.00000125 per request
    "ElasticSearch": lambda storage: 0.1 * storage,  # Needs adjustment based on instance type and storage
}

usage_requests_per_day = {
    "Low": 10,
    "Medium": 25,
    "High": 100
}

ec2_instance_mapping = {
    "t2.micro": 0.0116,
    "t2.small": 0.023,
    "t2.medium": 0.0464,
    "t2.large": 0.0928,
    "t2.xlarge": 0.1856,
    "t2.2xlarge": 0.3712,
    "m5.large": 0.096,
    "m5.xlarge": 0.192,
    "m5.2xlarge": 0.384,
    "m5.4xlarge": 0.768,
    "m5.8xlarge": 1.536,
    "m5.12xlarge": 2.304,
    "m5.16xlarge": 3.072,
    "m5.24xlarge": 4.608,
    "m5.metal": 5.52,
    "c5.large": 0.085,
    "c5.xlarge": 0.17,
    "c5.2xlarge": 0.34,
    "c5.4xlarge": 0.68,
    "c5.9xlarge": 1.53,
    "c5.18xlarge": 3.06
}

rds_instance_mapping = {
    "db.t2.micro": 0.017,
    "db.t2.small": 0.034,
    "db.t2.medium": 0.068,
    "db.t2.large": 0.136,
    "db.t2.xlarge": 0.272,
    "db.t2.2xlarge": 0.544,
    "db.m5.large": 0.115,
    "db.m5.xlarge": 0.23,
    "db.m5.2xlarge": 0.46,
    "db.m5.4xlarge": 0.92,
    "db.m5.12xlarge": 2.76,
    "db.m5.24xlarge": 5.52
}

def get_ec2_instance(concurrent_users):
    if concurrent_users <= 10:
        return "t2.micro"
    elif concurrent_users <= 25:
        return "t2.small"
    elif concurrent_users <= 50:
        return "t2.medium"
    elif concurrent_users <= 100:
        return "t2.large"
    elif concurrent_users <= 200:
        return "t2.xlarge"
    elif concurrent_users <= 500:
        return "t2.2xlarge"
    elif concurrent_users <= 1000:
        return "m5.large"
    elif concurrent_users <= 2000:
        return "m5.xlarge"
    elif concurrent_users <= 5000:
        return "m5.2xlarge"
    elif concurrent_users <= 10000:
        return "m5.4xlarge"
    elif concurrent_users <= 20000:
        return "m5.8xlarge"
    elif concurrent_users <= 50000:
        return "m5.12xlarge"
    elif concurrent_users <= 100000:
        return "m5.16xlarge"
    elif concurrent_users <= 200000:
        return "m5.24xlarge"
    elif concurrent_users <= 500000:
        return "c5.9xlarge"
    elif concurrent_users <= 1000000:
        return "c5.18xlarge"
    else:
        return "m5.metal"

def get_rds_instance(total_users):
    if total_users <= 100:
        return "db.t2.micro"
    elif total_users <= 500:
        return "db.t2.small"
    elif total_users <= 1000:
        return "db.t2.medium"
    elif total_users <= 5000:
        return "db.t2.large"
    elif total_users <= 10000:
        return "db.t2.xlarge"
    elif total_users <= 50000:
        return "db.t2.2xlarge"
    elif total_users <= 100000:
        return "db.m5.large"
    elif total_users <= 200000:
        return "db.m5.xlarge"
    elif total_users <= 500000:
        return "db.m5.2xlarge"
    elif total_users <= 1000000:
        return "db.m5.4xlarge"
    else:
        return "db.m5.24xlarge"

def calculate_costs(features, total_users, monthly_active_users, concurrent_users, storage, streaming, media_processing, usage_type):
    costs = {}
    include_ec2 = False
    
    # Check if EC2 should be included
    for feature in features:
        services = feature_service_mapping.get(feature, [])
        if "EC2" in services:
            include_ec2 = True
            break
    
    # Calculate EC2 and RDS instance sizes and costs
    if include_ec2:
        ec2_instance = get_ec2_instance(concurrent_users)
        costs["EC2"] = ec2_instance_mapping[ec2_instance] * 730  # Assuming 730 hours per month
    
    rds_instance = get_rds_instance(total_users)
    costs["RDS"] = rds_instance_mapping[rds_instance] * 730  # Assuming 730 hours per month
    
    for feature in features:
        services = feature_service_mapping.get(feature, [])
        for service in services:
            if service not in costs:
                costs[service] = 0
            if service == "Cognito":
                costs[service] += service_costs[service](monthly_active_users)
            elif service == "S3":
                costs[service] += service_costs[service](storage)
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
            elif service == "ElasticSearch":
                search_requests = int(monthly_requests * 0.2)
                costs[service] += service_costs[service](search_requests)

    total_cost = sum(costs.values())
    return costs, total_cost, ec2_instance if include_ec2 else None, rds_instance