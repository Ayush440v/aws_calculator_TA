from utils.service_mappings import feature_to_service_mapping

def calculate_costs(features, total_users, monthly_active_users, concurrent_users, storage, streaming, media_processing):
    costs = {}
    
    # Apply cost calculations based on the feature-service mapping
    for feature in features:
        services = feature_to_service_mapping.get(feature, [])
        for service in services:
            if service == "Cognito":
                costs[service] = costs.get(service, 0) + 0.005 * monthly_active_users
            elif service == "RDS":
                costs[service] = costs.get(service, 0) + 0.02 * concurrent_users + 0.01 * total_users
            elif service == "S3":
                costs[service] = costs.get(service, 0) + 0.023 * storage
            elif service == "EC2":
                costs[service] = costs.get(service, 0) + 0.1 * concurrent_users
            elif service == "MediaLive":
                costs[service] = costs.get(service, 0) + 0.5 * streaming
            elif service == "MediaConvert":
                costs[service] = costs.get(service, 0) + 0.3 * media_processing

    total_cost = sum(costs.values())
    return costs, total_cost
