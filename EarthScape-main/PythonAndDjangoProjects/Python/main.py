
import pandas as pd
import plotly.express as px
import io
import base64
import streamlit as st
import requests  # To handle requests to Django backend
import smtplib

import time
# Set the page configuration
st.set_page_config(
    page_title="EarthScape Climate Agency Futuristic Data Analysis Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize session state variables for login
if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
    st.session_state["email"] = None
    st.session_state["name"] = None

# Define the Django login URL
DJANGO_LOGIN_URL = "http://127.0.0.1:8000/"  # Replace with your Django login page URL

# Redirect to Django login page if not logged in
if not st.session_state["logged_in"]:
    # Extract query parameters to check if email and name exist
    query_params = st.query_params
    email = query_params.get("email", [None])  # Extract the first value or None
    name = query_params.get("name", [None])  # Extract the first value or None

    # Debugging: Print the extracted query parameters
    # st.write(f"Extracted email: {email}")
    # st.write(f"Extracted name: {name}")

    if email and name and "@" in email:  # Validate that email exists and is valid
        # Save login details in session state
        st.session_state["email"] = email
        st.session_state["name"] = name
        st.session_state["logged_in"] = True

        # Reload the page to reflect the updated session state
        st.markdown(
            """
            <script>
                window.location.reload();
            </script>
            """,
            unsafe_allow_html=True,
        )
    else:
        # If query parameters are invalid or missing, redirect to login
        st.error("Unauthorized access. Redirecting to login...")
        st.markdown(f"<meta http-equiv='refresh' content='0; url={DJANGO_LOGIN_URL}' />", unsafe_allow_html=True)
        st.stop()

# Ensure 'name' is defined in session state
if "name" not in st.session_state:
    st.session_state["name"] = "Guest"  # Default to 'Guest' if 'name' is not set

name = st.session_state["name"]  # Retrieve the name from session state




# Load the image and encode it
with open("images/EarthScape (6).png", "rb") as image_file:
    encoded_logo = base64.b64encode(image_file.read()).decode()
# Page Configuration with Custom Layout


# Custom CSS for futuristic look
st.markdown("""
    <style>
        body {
            background-color: #f0f8ff; /* Light blue background */
            color: #333; /* Dark text for readability */
        }

        .navbar {
            background-color: rgb(37, 40, 42);
            padding: 1rem;
            text-align: center;
            margin-top: -103px;
            height: 65px;
        }

        .navbar a {
            color: white;
            padding: 10px 20px;
            text-decoration: none;
            font-size: 18px;
        }

        .navbar a:hover {
            background-color: #3949ab;
            border-radius: 5px;
        }

     .hero {
            position: relative;
            color: white;
            padding: 6rem 0;
            height: 600px;
            text-align: center;
            margin-top: -47px;
            z-index: 1; /* Ensures content is above the background */
        }

        .hero::before {
            content: "";
            position: absolute;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background-image: url('https://cdn.sanity.io/images/tlr8oxjg/production/2d8450596e26adafc8e47e88a65bce42104b732a-1456x816.png?w=3840&q=100&fit=clip&auto=format');
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
            opacity: 0.5; /* Adjust this value to reduce opacity (0.0 - 1.0) */
            z-index: -1; /* Ensures the background is behind the content */
        }

        .hero h1 {
            font-size: 3rem;
            color: #ffff;
            margin-top:60px;
        }

        .hero p {
            font-size: 1.5rem;
            margin-bottom: 2rem;
        }

        .btn {
            background-color: #42a5f5;
            color: white;
            padding: 10px 20px;
            border: none;
            border-radius: 5px;
            font-size: 1rem;
            text-decoration: none;
            margin-right: 10px;
        }

        .btn:hover {
            background-color: #1e88e5;
        }

        footer {
            background-color: rgb(37, 40, 42); /* Dark blue for a polished look */
            color: #ffffff; /* White text for contrast */
            position:fixed;
            bottom:0;
            width:97.6%;
            color:white;
            text-align:center;
            padding:20px;
            font-size:1rem;
        }

        footer a {
            color: #42a5f5; /* Light blue for links */
            text-decoration: none;
        }

        footer a:hover {
            color: #1e88e5; /* Darker blue on hover */
        }

        footer .social-icons {
            margin-top: 1rem;
        }

        footer .social-icons a {
            color: #ffffff;
            margin: 0 10px;
            font-size: 1.5rem;
        }

        footer .social-icons a:hover {
            color: #1e88e5;
        }

        .main-content {
            padding: 2rem;
        }

        .section-header {
            # color: #1a237e;
            # color:black;
            margin-bottom: 1rem;
        }

        .container, .card, .section {
            background-color: rgb(38, 39, 48); /* White background for content areas */
            border: 1px solid #e0e0e0; /* Light gray borders for separation */
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1); /* Soft shadow for depth */
            margin-bottom: 2rem;
            padding: 1.5rem;
        }

        h1, h2, h3, p {
            color: #ffffb; /* Dark blue text */
        }

        .btn-primary {
            background-color: #42a5f5; /* Light blue */
            color: white;
            border: none;
        }

        .btn-primary:hover {
            background-color: #1e88e5; /* Slightly darker blue on hover */
        }

        .st-emotion-cache-h4xjwg {
            position: fixed;
            top: 0px;
            left: 0px;
            right: 0px;
            height: 3.75rem;
            background: rgb(14, 17, 23);
            outline: none;
            z-index: 999990;
            display: none;
        }

        .st-emotion-cache-nok2kl a {
            color: #ffff;
        }

        .st-emotion-cache-1jicfl2 {
            width: 100%;
            padding: 6rem 1rem 10rem;
            min-width: auto;
            max-width: initial;
            background-color: black;
        }
        
        @media (max-width: 768px) {
        .navbar {
            flex-direction: column; /* Stack the navbar links */
            padding: 0.5rem; /* Reduce padding */
        }

        .navbar a {
            font-size: 16px; /* Smaller font size for links */
            padding: 8px; /* Adjust padding for smaller buttons */
        }

        .hero {
            padding: 4rem 1rem; /* Reduce padding */
            height: auto; /* Allow height to be auto */
        }

        .hero h1 {
            font-size: 2rem; /* Smaller font size for heading */
        }

        .hero p {
            font-size: 1rem; /* Smaller font size for paragraphs */
        }

        .container, .card, .section {
            padding: 1rem; /* Reduce padding for content areas */
        }



        .section-header {
            font-size: 1.5rem; /* Smaller font size for section headers */
        }

        .btn {
            font-size: 0.9rem; /* Smaller font size for buttons */
            padding: 8px; /* Adjust padding for buttons */
        }
    }
   
    /* Media query for smaller screens */
    @media (max-width: 768px) { /* Adjust the max-width as needed */
        .hero {
            margin-top: 10px; /* Increase top margin */
        }
    }
     /* Media query for smaller screens */
    @media (max-width: 768px) { /* Adjust the max-width as needed */
        footer {
            width: 90%; /* Change width to 90% */
        }
    }
    </style>
    
""", unsafe_allow_html=True)

# Navigation Bar

# Load the image and encode it
with open("images/EarthScape (6).png", "rb") as image_file:
    encoded_logo = base64.b64encode(image_file.read()).decode()

if "logged_in" not in st.session_state:
    st.session_state["logged_in"] = False
if "name" not in st.session_state:
    st.session_state["name"] = "Guest"

# Check if the user has logged out
if st.session_state.get("logged_in") is False:
    st.write("You are logged out.")


if "logged_in" in st.session_state and not st.session_state["logged_in"]:
    st.session_state.clear()  # Clear all session state variables

# Fetch the name dynamically from session state or default to 'User'
name = st.session_state.get('name', 'User')

# Define the HTML with the name dynamically inserted
navbar_html = f"""
<style>
.navbar {{
    padding: 10px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    background-color: #333;
}}

.navbar a {{
    color: white;
    text-decoration: none;
    margin-right: 15px;
}}

.dropdown {{
    position: relative;
    display: inline-block;
}}

/* Dropdown button styling */
.dropdown > button {{
    background-color: #333;
    color: white;
    border: none;
    cursor: pointer;
    padding: 10px 15px;
    font-size: 16px;
    border-radius: 5px;
}}

/* Hide dropdown content by default */
.dropdown-content {{
    display: none;
    position: absolute;
    background-color: #f9f9f9;
    box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
    z-index: 1;
    border-radius: 5px;
    width: 150px;
}}

/* Show dropdown content when button is focused */
.dropdown > button:focus + .dropdown-content {{
    display: block;
}}

/* Keep dropdown open when clicking inside */
.dropdown-content:hover {{
    display: block;
}}

.dropdown-content a, .dropdown-content button {{
    color: black;
    padding: 10px 15px;
    text-decoration: none;
    display: block;
    background: none;
    border: none;
    text-align: left;
    cursor: pointer;
}}

.dropdown-content a:hover, .dropdown-content button:hover {{
    background-color: #333;
    width: 80px !important;
    color:white !important;
    border-radius:5px !important;;
    
}}

.logout-button {{
    background-color: red;
    color: white;
    border: none;
    width: 100%;
    text-align: left;
    z-index: -2;
}}
 .navbar img {{
        height: 130px; /* Default height */
        margin-right: 15px;
    }}
    
    @media (max-width: 768px) {{
        .navbar img {{
            margin-top:-40px;
            margin-left:-36px;
        }}
    }}
</style>

<div class="">
   <div class="container navbar">
    <div class="row">
        <div class="col-md-12">
        <img src="data:image/jpeg;base64,{encoded_logo}" alt="Logo">
        <a href="#home">Home</a>
        <a href="#data-input">Data Input</a>
        <a href="#visualizations">Visualizations</a>
        <a href="#search-data">Search Data</a>
        <a href="#about">About</a>
    <!-- Dropdown menu -->
<div class="dropdown">
    <button>{name} &#9662;</button>
    <div class="dropdown-content" style="width:80px; z-index: 2;">
        <form method="get" action="http://127.0.0.1:8000/logout/" >
            <button type="submit" style="width:20px;" class="logout-button">Logout</button>
        </form>
    </div>
</div>
        </div>
    </div>
   </div>


</div>
"""

# Render the navbar in Streamlit
st.markdown(navbar_html, unsafe_allow_html=True)

# DJANGO_NAVBAR_URL = "http://127.0.0.1:8000/navbar/"
# response = requests.get(DJANGO_NAVBAR_URL)

# if response.status_code == 200:
#     navbar_html = response.text
#     st.markdown(navbar_html, unsafe_allow_html=True)
# else:
#     st.error("Failed to load navbar.")

# Use query parameter to handle logout logic
query_params = st.query_params

if "logout" in query_params:
    # Clear session state on logout
    st.session_state["logged_in"] = False
    st.session_state["name"] = "Guest"

    # Notify Django backend to log out the user
    response = requests.post("http://127.0.0.1:8000/logout/")  # Replace with your Django logout endpoint
    if response.status_code == 200:
        # Redirect to Django login page
        st.markdown(
            """
            <script>
                window.location.href = "http://127.0.0.1:8000/login/";
            </script>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.error("Logout failed. Please try again.")
        

        
# ================================
# Home Section
# ================================
st.markdown("<div id='home'></div>", unsafe_allow_html=True)
st.markdown("""
<div class="hero">
    <h1>Data Analysis Dashboard</h1>
    <p>Welcome to EarthScape Climate Agency, a data-driven solution designed to protect and optimize the environment.</p>
    <p>Our advanced tools allow you to analyze environmental data, generate predictive models, and visualize insights in real-time.</p>
</div>
""", unsafe_allow_html=True)




# ================================
# Data Input Section
# ================================
st.markdown("<div id='data-input'></div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<h2 class='section-header'>Data Input</h2>", unsafe_allow_html=True)
st.markdown("""<div class="main-content">Upload or Enter Your Data to Start Analyzing!</div>""", unsafe_allow_html=True)

# Use two columns for upload options
col1, col2 = st.columns(2)

with col1:
    st.write("**Option 1: Upload a CSV or Excel file**")
    uploaded_file = st.file_uploader("Choose your CSV or Excel file", type=["csv", "xlsx"])

    # Default file path
    default_file_path = "data/Cleaned_EarthScape_Dataset_All (1).xlsx"

# Handle File Upload
if uploaded_file:
    file_extension = uploaded_file.name.split('.')[-1]
    try:
        if file_extension == 'csv':
            st.session_state.df = pd.read_csv(uploaded_file)
        elif file_extension in ['xlsx']:
            st.session_state.df = pd.read_excel(uploaded_file)
        st.success(f"File '{uploaded_file.name}' uploaded successfully!")

        # Show the DataFrame after uploading
        st.markdown("Data Loaded from Uploaded File:")
        st.dataframe(st.session_state.df.style.background_gradient(cmap='Blues').set_properties(**{'color': '#FAFAFA'}))

    except Exception as e:
        st.error(f"Error processing the file: {e}")
else:
    # Load the default file if no upload
    try:
        st.session_state.df = pd.read_excel(default_file_path)
        st.markdown("Data Loaded from Default File:")
        st.dataframe(st.session_state.df.style.background_gradient(cmap='Blues').set_properties(**{'color': '#FAFAFA'}))
    except FileNotFoundError:
        st.error(f"Default file not found at '{default_file_path}'. Please check the path.")
    except Exception as e:
        st.error(f"Error loading default file: {e}")

with col2:
    st.write("**Option 2: Enter your data manually (CSV format)**")
    st.write("**Example format:** `Name, Age, Salary`")
    st.code("Name, Age, Salary\nJohn, 30, 50000\nAnna, 25, 60000\nTom, 35, 70000", language="text")
    
    manual_data = st.text_area("Enter your data below:", height=150)
    
    if manual_data:
        try:
            st.session_state.df = pd.read_csv(io.StringIO(manual_data))
            st.success("Manual data entered successfully!")
        except Exception as e:
            st.error(f"Error processing manual data: {e}")

# ================================
# Search Data Section
# ================================
st.markdown("<div id='search-data'></div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<h2 class='section-header'>Search by Column</h2>", unsafe_allow_html=True)

filtered_df = st.session_state.df

# First select box for columns (if data is available)
if st.session_state.df is not None:
    column_names = ["Select a column..."] + st.session_state.df.columns.tolist()
    selected_column = st.selectbox("Select a column to search:", column_names, index=0)

    # Second select box for data in the selected column, ignoring null values
    if selected_column != "Select a column...":
        column_data = st.session_state.df[selected_column].dropna().unique().tolist()  # Exclude NaN values
        column_data = ["Select a value..."] + column_data  # Add placeholder
        selected_data = st.selectbox(f"Select a value from column '{selected_column}':", column_data, index=0)

        if selected_data != "Select a value...":
            # Filter data based on the selected column and value
            filtered_df = st.session_state.df[st.session_state.df[selected_column] == selected_data]
            st.markdown(f"Filtered Data for {selected_column}: '{selected_data}'")
            st.dataframe(filtered_df.style.background_gradient(cmap='Blues').set_properties(**{'color': '#FAFAFA'}))
# ================================
# Visualizations Section
# ================================
st.markdown("<div id='visualizations'></div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<h2 class='section-header'>Data Visualizations</h2>", unsafe_allow_html=True)

# Check if data is available
if filtered_df is not None and not filtered_df.empty:
    st.markdown("### Create Visualizations from Your Filtered Data")

    # Pie Chart
    st.markdown("#### Pie Chart")
    categorical_columns = filtered_df.select_dtypes(include='object').columns
    if len(categorical_columns) > 0:
        selected_column_pie = st.selectbox("Select a categorical column for Pie Chart:", categorical_columns)
        if selected_column_pie:
            fig_pie = px.pie(filtered_df, names=selected_column_pie)
            st.plotly_chart(fig_pie)
    else:
        st.warning("No categorical columns available for Pie Chart")

    # Bar Chart
    st.markdown("#### Bar Chart")
    numeric_columns = filtered_df.select_dtypes(include='number').columns
    if len(numeric_columns) > 0:
        selected_column_bar_x = st.selectbox("Select X-axis for Bar Chart:", numeric_columns)
        selected_column_bar_y = st.selectbox("Select Y-axis for Bar Chart:", numeric_columns, index=1)
        if selected_column_bar_x and selected_column_bar_y:
            fig_bar = px.bar(filtered_df, x=selected_column_bar_x, y=selected_column_bar_y)
            st.plotly_chart(fig_bar)
    else:
        st.warning("No numeric columns available for Bar Chart")

    # Scatter Plot
    st.markdown("#### Scatter Plot")
    if len(numeric_columns) > 1:
        selected_column_scatter_x = st.selectbox("Select X-axis for Scatter Plot:", numeric_columns)
        selected_column_scatter_y = st.selectbox("Select Y-axis for Scatter Plot:", numeric_columns, index=1)
        if selected_column_scatter_x and selected_column_scatter_y:
            fig_scatter = px.scatter(filtered_df, x=selected_column_scatter_x, y=selected_column_scatter_y)
            st.plotly_chart(fig_scatter)
else:
    st.warning("Please upload or enter data first to create visualizations.")

# ================================
# Real-Time Data Visualization Section
# ================================
# Simulating batch data for visualization
batch_data = pd.DataFrame({
    "timestamp": pd.date_range(start="2024-01-01", periods=10, freq="D"),
    "value": [i for i in range(10, 20)]
})

# Initialize session state variables
if "real_time_data" not in st.session_state:
    st.session_state.real_time_data = pd.DataFrame({"timestamp": [], "value": []})
if "start_visualization" not in st.session_state:
    st.session_state.start_visualization = False  # Tracks if visualization is active
if "visualization_active" not in st.session_state:
    st.session_state.visualization_active = False  # Ensures loop runs only once per session

# Real-Time Visualization Section
st.markdown("<div id='real-time-visualization'></div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<h2 class='section-header'>Real-Time Data Visualization</h2>", unsafe_allow_html=True)

# Buttons to control real-time updates
col1, col2 = st.columns([1, 1])
with col1:
    if st.button("Start Real-Time Visualization", key="start_button"):
        if not st.session_state.start_visualization:
            st.session_state.start_visualization = True
            st.session_state.visualization_active = True  # Activate the visualization loop
            st.session_state.real_time_data = pd.DataFrame({"timestamp": [], "value": []})  # Reset data
with col2:
    if st.button("Stop Real-Time Visualization", key="stop_button"):
        st.session_state.start_visualization = False
        st.session_state.visualization_active = False  # Deactivate the visualization loop

# Placeholder for dynamic updates
placeholder = st.empty()

# Run the real-time visualization only once per session
if st.session_state.start_visualization and st.session_state.visualization_active:
    st.write("This section dynamically updates real-time data and combines it with existing batch data.")
    for i in range(20):  # Simulate 20 real-time updates
        # Check if the stop button was pressed
        if not st.session_state.start_visualization:
            st.session_state.visualization_active = False
            break  # Stop the loop if visualization is deactivated

        # Add new real-time data
        new_data = pd.DataFrame({
            "timestamp": [pd.Timestamp.now()],
            "value": [20 + i]  # Simulated dynamic values
        })
        st.session_state.real_time_data = pd.concat(
            [st.session_state.real_time_data, new_data],
            ignore_index=True
        )

        # Combine real-time and batch data
        combined_data = pd.concat([batch_data, st.session_state.real_time_data])

        # Update visualization dynamically
        with placeholder.container():
            st.line_chart(combined_data.set_index("timestamp"))

        time.sleep(1)  # Delay to simulate real-time updates

    st.session_state.visualization_active = False  # Mark visualization loop as completed

# ================================
# Report Generation Section
# ================================
st.markdown("<div id='report-generation'></div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<h2 class='section-header'>Generate Report</h2>", unsafe_allow_html=True)

# Combine batch data and real-time data for report generation
combined_data = pd.concat([batch_data, st.session_state.real_time_data], ignore_index=True)

if not combined_data.empty:
    st.write("Click the button below to download your combined data as a CSV or Excel file.")

    # Button to generate report as CSV
    csv = combined_data.to_csv(index=False)
    st.download_button(
        label="Download Report as CSV",
        data=csv,
        file_name="combined_data.csv",
        mime="text/csv"
    )

    # Button to generate report as Excel
    excel_file = io.BytesIO()
    with pd.ExcelWriter(excel_file, engine='xlsxwriter') as writer:
        combined_data.to_excel(writer, index=False, sheet_name='Combined Data')
    excel_file.seek(0)
    
    st.download_button(
        label="Download Report as Excel",
        data=excel_file,
        file_name="combined_data.xlsx",
        mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
    )

else:
    st.warning("No data available to generate a report. Please start real-time visualization or upload data.")



# ====================================
# Notifications and Alerts Section
# ====================================
st.markdown("---")
st.markdown("<h2>Notifications and Alerts</h2>", unsafe_allow_html=True)

# Simulated real-time data
real_time_data = pd.DataFrame({
    "timestamp": pd.date_range(start="2024-01-01", periods=10, freq="D"),
    "temperature": [35, 36, 38, 40, 42, 43, 39, 37, 36, 35],
    "humidity": [60, 62, 64, 66, 68, 72, 75, 80, 82, 78]
})

# Define thresholds
threshold_temperature = st.slider("Set Temperature Threshold", 30, 50, 40)
threshold_humidity = st.slider("Set Humidity Threshold", 50, 100, 75)

# Function to send email notifications
def send_email_alert(subject, message, recipient_email):
    sender_email = "muhammadanasz786@gmail.com"  # Replace with your email
    password = "irbwoslkkzqusujl"  # Replace with your email app password
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(sender_email, password)
        # Encode the email message in UTF-8
        email_message = f"Subject: {subject}\n\n{message}".encode("utf-8")
        server.sendmail(sender_email, recipient_email, email_message)
        server.quit()
        st.success("Alert sent successfully!")
    except Exception as e:
        st.error(f"Failed to send alert: {e}")

# Real-time Monitoring Section
st.markdown("### Real-Time Monitoring")
if "current_index" not in st.session_state:
    st.session_state.current_index = 0

# Start/Stop buttons for monitoring
start_monitoring = st.button("Start Monitoring")
stop_monitoring = st.button("Stop Monitoring")

placeholder = st.empty()

# Real-time updates logic
if start_monitoring:
    st.session_state.current_index = 0  # Reset monitoring index
    while st.session_state.current_index < len(real_time_data):
        current_row = real_time_data.iloc[st.session_state.current_index]

        # Check thresholds
        recipient_email = st.session_state.get("email")
        if current_row["temperature"] > threshold_temperature and recipient_email:
            st.warning(f"⚠️ High Temperature Alert: {current_row['temperature']}°C at {current_row['timestamp']}")
            send_email_alert(
                subject="High Temperature Alert",
                message=f"Temperature exceeded the threshold: {current_row['temperature']}°C on {current_row['timestamp']}.",
                recipient_email=recipient_email
            )

        if current_row["humidity"] > threshold_humidity and recipient_email:
            st.warning(f"⚠️ High Humidity Alert: {current_row['humidity']}% at {current_row['timestamp']}")
            send_email_alert(
                subject="High Humidity Alert",
                message=f"Humidity exceeded the threshold: {current_row['humidity']}% on {current_row['timestamp']}.",
                recipient_email=recipient_email
            )

        # Update visualization
        with placeholder.container():
            st.dataframe(real_time_data.iloc[:st.session_state.current_index + 1])

        # Increment index and simulate delay
        st.session_state.current_index += 1
        time.sleep(1)

        # Stop monitoring if the button is pressed
        if stop_monitoring:
            st.info("Monitoring stopped.")
            st.stop()

# ================================
# About Section
# ================================
st.markdown("<div id='about'></div>", unsafe_allow_html=True)
st.markdown("---")
st.markdown("<h2 class='section-header'>About This Project</h2>", unsafe_allow_html=True)
st.markdown("""
    <div class="main-content">
        <p>EarthScape Climate Agency is a futuristic data analysis dashboard aimed at providing comprehensive insights into environmental data. 
        The application allows users to upload data in CSV or Excel formats, visualize it through various graphical representations, 
        and conduct insightful analysis.</p>

        <p>Key Features:</p>
        <ul>
            <li>Upload and process CSV/Excel files for immediate analysis.</li>
            <li>Visualize data through interactive charts (Pie, Bar, and Scatter plots).</li>
            <li>Search and filter data dynamically using specific columns and values.</li>
            <li>Real-Time Data Visualization with dynamic updates and simulations.</li>
            <li>Set thresholds for temperature and humidity monitoring with real-time alerts.</li>
            <li>Email notifications for threshold breaches, ensuring timely actions.</li>
            <li>Generate and download reports in CSV or Excel format.</li>
            <li>Manually input data in a structured format for quick analysis.</li>
            <li>Accessible and user-friendly interface with responsive design.</li>
            <li>Customizable layout with advanced visualization options.</li>
            <li>Feedback and support system to address user issues effectively.</li>
        </ul>

        <p>Our mission is to promote environmental awareness and provide tools for better decision-making based on data.</p>

    </div>
""", unsafe_allow_html=True)

# Feedback Section
st.markdown("---")
st.markdown("<h2>Feedback and Support</h2>", unsafe_allow_html=True)

with st.form("feedback_form"):
    user_name = st.text_input("Your Name")
    email = st.text_input("Your Email")
    feedback = st.text_area("Provide Your Feedback or Report an Issue:")
    submitted = st.form_submit_button("Submit Feedback")

    if submitted:
        if feedback.strip():
            with st.spinner("Sending your feedback..."):
                subject = "New Feedback from EarthScape Climate Agency Dashboard"
                recipient_email = "admin@example.com"
                message = f"Name: {user_name}\nEmail: {email}\n\nFeedback:\n{feedback}"
                send_email_alert(subject, message, recipient_email)
        else:
            st.error("Feedback cannot be empty.")


# Footer Section
st.markdown("""
<footer>
    <div>
        © 2024 EarthScape Climate Agency Futuristic Data Analysis Dashboard. All rights reserved.
    </div>
</footer>
""", unsafe_allow_html=True)
