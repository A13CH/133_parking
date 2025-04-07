import streamlit as st

st.set_page_config(
    page_title="About - 103 Parking",
    page_icon="ℹ️",
    layout="centered",
)

# Add a title for the About page
st.title("About This Project")

# Add a description of the project
st.markdown(
    """
    This project is a **real-time parking spot monitoring system** designed for Apartment 103. 
    It uses an MQTT-based communication system to detect whether a parking spot is **occupied** or **available** 
    and displays the status on a modern, mobile-friendly web interface.

    ### Features:
    - Real-time updates using MQTT.
    - A clean and responsive user interface built with Streamlit.
    - Visual indicators (images and text) for parking spot status.
    - Designed for mobile and desktop devices.

    ### How It Works:
    - A sensor publishes data to an MQTT topic (`pico1/distance`).
    - The web app subscribes to the topic and updates the parking spot status dynamically.
    - The status is displayed as either **Occupied** or **Available**, along with corresponding images.

    ### GitHub Repository:
    You can find the source code for this project on GitHub:
    [GitHub Repository](https://github.com/your-username/your-repo-name)
    """,
    unsafe_allow_html=True,
)

# Add a footer or additional information
st.markdown(
    """
    ---
    Created using [Streamlit](https://streamlit.io/) and [Paho MQTT](https://www.eclipse.org/paho/).
    """
)