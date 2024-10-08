feature_to_service_mapping = {
    "Login-Signup": ["Cognito"],
    "Profile Management": ["RDS", "Lambda"],
    "Image Post": ["S3", "Lambda"],
    "Video Post": ["S3", "MediaLive", "MediaConvert"],
    "Text Post": ["RDS", "Lambda"],
    "Live Streaming": ["MediaLive"],
    "Chat": ["DynamoDB", "EC2"],
    "Comments": ["DynamoDB", "Lambda"],
    "Likes": ["DynamoDB", "Lambda"],
    "Sharing": ["S3", "Lambda"],
    "Notifications": ["RDS"],
    "Search and Filters": ["RDS", "ElasticSearch"],
    "Product Listings": ["RDS", "S3"],
    "Shopping Cart": ["RDS"],
    "Checkout": ["RDS", "S3"],
    "Payment Gateway": ["RDS"],
    "Order Tracking": ["RDS"],
    "User Reviews": ["RDS"],
    "Wishlist": ["RDS"],
    "Video Streaming": ["MediaLive"],
    "Media Processing": ["MediaConvert"],
    "Appointment Scheduling": ["RDS", "EC2"],
    "Telemedicine": ["EC2", "RDS"],
    "EHR Integration": ["RDS", "EC2"],
    "Payment Processing": ["RDS", "Lambda"],
    "Account Management": ["RDS", "Lambda"],
    "Investment Tracking": ["RDS", "EC2"],
    "Service Listings": ["RDS", "Lambda"],
    "Booking System": ["RDS", "Lambda"],
    "Order Tracking": ["RDS", "Lambda"],
    "User Reviews": ["RDS", "Lambda"],
}
