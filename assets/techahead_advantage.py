import streamlit as st

def techahead_advantage():
    # Page Title and Description
    st.title("TechAhead Advantage")
    st.write("At TechAhead, we help you build robust, cost-effective applications that scale with your business. Here’s how we do it!")
    
    # Advantage 1: Good Architecture Content
    st.header("1. Good Architecture")
    st.subheader("1.1. Design for reliability")
    st.write("We ensure your applications are designed to be reliable. This means setting up systems that can handle failures without affecting your users. For example, we implemented a multi-zone setup for an online store, ensuring that even if one server goes down, another takes over instantly.")
    
    # Microservices
    st.subheader("1.2. Breaking down services")
    st.write("We use a microservices approach to break down your application into smaller, manageable pieces. This makes it easier to update and scale parts of your application independently. For instance, we created separate services for user management, payments, and inventory for a retail app, improving both performance and scalability.")
    
    # Infrastructure as Code
    st.subheader("1.3. Automated Infrastucture")
    st.write("By using tools to manage infrastructure through code, we ensure that your setup is consistent and repeatable. This means faster deployment times and fewer errors. For example, we used infrastructure-as-code to deploy identical environments for development, testing, and production for a client’s software project.")
    
    # Flexible Design
    st.subheader("1.4. Felxible Design")
    st.write("We design your system to be flexible and adaptable. By reducing dependencies between components, we make it easier to modify and scale your system. For instance, we used API-based communication between services in a logistics platform, allowing easy updates and enhancements.")
    
    st.divider()
    
    # Advantage 2: Cost Effectiveness
    st.header("2. Cost Effectiveness")
    
    # Scalability
    st.subheader("2.1. Right Sizing")
    st.write("We continually review your resource usage to ensure you’re not overpaying for capacity you don’t need. For example, we helped a client downsize their database instances during off-peak hours, significantly reducing costs without impacting performance.")
    
    # Cost Savings
    st.subheader("2.2. Savings with reserved instances")
    st.write("For predictable workloads, we recommend committing to Reserved Instances, which offer significant savings. We helped a client save 30% on their EC2 costs by switching to Reserved Instances for their steady-state applications.")
    
    
    st.subheader("2.3. Efficient storage solutions")
    st.write("We implement lifecycle policies to move data to more cost-effective storage options over time. For example, we set up automated policies to transition old data to Amazon Glacier for a legal firm, reducing their storage costs by 60%.")
    
    st.divider()
    
    st.header("3. Scaling with the product")
    
    st.subheader("3.1. Automatic Scaling")
    st.write("We set up auto-scaling to automatically adjust resources based on demand. This ensures your application performs well during traffic spikes without overspending during quieter periods. For instance, we configured auto-scaling for a client’s mobile app, ensuring seamless performance during a major marketing campaign.")
    
    