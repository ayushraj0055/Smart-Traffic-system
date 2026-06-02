import streamlit as st
import networkx as nx
from ultralytics import YOLO
from PIL import Image
import tempfile

# ================= PAGE CONFIG =================
st.set_page_config(page_title="Smart Traffic AI", layout="wide")

st.title("🚦 Smart Traffic AI Dashboard")

# ================= LOAD YOLO MODEL =================
model = YOLO("yolov8n.pt")

# ================= SIDEBAR MENU =================
st.sidebar.title("Navigation")

menu = st.sidebar.radio(
    "Go to",
    ["Dashboard", "Accident Detection", "Traffic Prediction"]
)

# ================= DASHBOARD =================
if menu == "Dashboard":

    st.subheader("🚨 Accident Alert")
    st.error("Possible accident detected near Junction A")

    st.subheader("📈 Traffic Prediction")
    st.warning("Heavy congestion predicted in 15 minutes")

    st.subheader("🌧 Weather Analysis")
    st.info("Rain increased congestion probability by 35%")

    st.subheader("🛣 Emergency Route")
    st.success("Suggested Route: Road C → Road D")

# ================= ACCIDENT DETECTION =================
elif menu == "Accident Detection":

    st.subheader("📷 Upload Traffic Image")

    uploaded_file = st.file_uploader(
        "Choose Traffic Image",
        type=["jpg", "png", "jpeg"]
    )

    if uploaded_file is not None:

        # Load image
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Traffic Image")

        # Save to temp file
        temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".jpg")
        image.save(temp_file.name)

        # Run YOLO detection
        results = model(temp_file.name)

        # Plot result image
        result_image = results[0].plot()
        st.image(result_image, caption="YOLO Detection Result")

        # Vehicle count
        vehicle_count = len(results[0].boxes)

        st.subheader("🚗 Vehicle Count")
        st.write(f"Detected Vehicles: {vehicle_count}")

        # Weather simulation
        weather = "Rain"

        st.subheader("🌧 Weather Condition")
        st.write(weather)

        # Traffic prediction logic
        st.subheader("📈 Traffic Prediction")

        if vehicle_count > 15 or weather == "Rain":
            st.error("Heavy Congestion Predicted")

        elif vehicle_count > 8:
            st.warning("Moderate Traffic Predicted")

        else:
            st.success("Traffic Flow Normal")

    else:
        st.info("Please upload a traffic image to analyze.")

# ================= TRAFFIC PREDICTION =================
elif menu == "Traffic Prediction":

    st.subheader("📊 Smart Traffic Prediction System")

    st.write("This module predicts traffic based on YOLO detection and weather conditions.")

    st.info("Go to Accident Detection tab and upload an image to generate predictions.")

# ================= GNN ROUTE OPTIMIZATION =================
st.subheader("🧠 GNN Route Optimization (Graph-Based Simulation)")

# Create road network graph
G = nx.Graph()

G.add_edge("Road A", "Road B", weight=5)
G.add_edge("Road B", "Road C", weight=3)
G.add_edge("Road A", "Road D", weight=7)
G.add_edge("Road D", "Road C", weight=2)

# Compute shortest path
best_route = nx.shortest_path(
    G,
    source="Road A",
    target="Road C",
    weight="weight"
)

st.write("Optimal Emergency Route:")

st.success(" → ".join(best_route))