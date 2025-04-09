import streamlit as st
import paho.mqtt.client as mqtt
import time  # Import time for periodic updates

st.set_page_config(
    page_title="133 Parking",
    page_icon="🚗",
    layout="centered",  # Center the content
)

# Global variable to store detection status
DETECTION = False

# MQTT callback functions
def on_connect(client, userdata, flags, reason_code, properties=None):
    if reason_code == 0:
        client.subscribe("pico1/distance")  # Subscribe to the topic
        print("Connected and subscribed to pico1/distance")
    else:
        print(f"Failed to connect, reason code: {reason_code}")

def on_message(client, userdata, message):
    global DETECTION
    payload = message.payload.decode("utf-8").strip()  # Decode and strip whitespace
    print(f"Received message: {payload} on topic {message.topic}")
    
    # Update DETECTION based on the payload
    if payload == "1":
        DETECTION = True
    elif payload == "0":
        DETECTION = False
    else:
        print(f"Unexpected payload: {payload}")  # Debug: Handle unexpected payloads

# Initialize MQTT client
mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_message = on_message
mqttc.username_pw_set("admin", "admin")
mqttc.connect("192.168.0.53")  # Connect to the MQTT broker
mqttc.loop_start()  # Start the MQTT loop in a separate thread

# Add a top banner for the title
st.markdown(
    """
    <div style="background-color:#383838;padding:10px;border-radius:5px;">
        <h1 style="color:white;text-align:center;">Apartment 133<br>Parking Spot Status</h1>
    </div>
    """,
    unsafe_allow_html=True,
)

# Create placeholders for dynamic updates
status_placeholder = st.empty()
image_placeholder = st.empty()

# Add the "About" section below the parking images (static content)
st.markdown("---")  # Add a horizontal line for separation
st.title("About This Project")
st.markdown(
    """
    This project is a **real-time parking spot monitoring system** designed for Apartment 133. 
    It uses an MQTT-based communication protocol to detect whether a parking spot is **occupied** or **available** 
    and displays the status on a Streamlit web application.

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

# Periodically update the status using Streamlit's rerun mechanism
while True:
    with status_placeholder.container():
        if DETECTION:
            # Display "Occupied" status with a car image
            image_placeholder.image("./src/car_occupied.png", use_container_width=True)  # Replace with your car image
            st.markdown(
                "<h2 style='text-align: center; color: red;'>Occupied</h2>",
                unsafe_allow_html=True,
            )
        else:
            # Display "Available" status with an empty parking spot image
            image_placeholder.image("./src/parking_available.png", use_container_width=True)  # Replace with your parking spot image
            st.markdown(
                "<h2 style='text-align: center; color: green;'>Available</h2>",
                unsafe_allow_html=True,
            )
    time.sleep(1)  # Add a delay to avoid excessive CPU usage