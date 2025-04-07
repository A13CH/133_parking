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
    This project is a **real-time parking spot monitoring system** designed for Apartment 133. 
    It uses an MQTT-based communication protocol to detect whether a parking spot is **occupied** or **available** 
    and displays the status on a streamlit web application.

    ### Features:
    - Real-time updates using MQTT.
    - A clean and responsive user interface built with Streamlit.
    - Visual indicators (images and text) for parking spot status.

    ### How It Works:
    - Pi Pico W attached above the parking spot detects the distance to the ground.
    - If the distance is less than a certain threshold, the spot is considered **Occupied**.
    - The Pico W publishes this data to an MQTT topic (`pico1/distance`).
    - The web app subscribes to the topic and updates the parking spot status dynamically.
    - The status is displayed as either **Occupied** or **Available**, along with corresponding images.

    ### GitHub Repository:
    You can find the source code for this project on GitHub:
    [133_parking](https://github.com/A13CH/133_parking)

    ### Note:
    I purchased the wrong domain name for this project.
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