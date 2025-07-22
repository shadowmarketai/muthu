import streamlit as st
import pandas as pd

st.set_page_config(page_title="Cinespa Home Automation Configurator", layout="centered")

st.title("🏠 Luxury Home Automation by Cinespa")
st.subheader("Configure your perfect lifestyle automation")

# Step 1: Select Preferences
st.markdown("### Step 1: Select your lifestyle preferences")

lighting = st.checkbox("Mood Lighting")
climate = st.checkbox("Climate Control")
audio = st.checkbox("Multi-room Audio")
security = st.checkbox("Smart Security")
theatre = st.checkbox("Elite Home Theatre")
blinds = st.checkbox("Automated Blinds")

# Step 2: Display Recommendations
st.markdown("### Step 2: Your Recommended Automation Package")

solutions = []

if lighting:
    solutions.append({
        "Category": "Lighting Automation",
        "Solution": "Scene-based lighting using ABB or Control4",
        "Benefits": "Elegant transitions, energy savings, wow-factor ambience"
    })

if climate:
    solutions.append({
        "Category": "Climate Control",
        "Solution": "Smart HVAC zoning + intelligent learning",
        "Benefits": "Personalized comfort with efficient energy usage"
    })

if audio:
    solutions.append({
        "Category": "Multi-room Audio",
        "Solution": "Genelec audio integrated with iPad control",
        "Benefits": "Seamless, studio-quality audio across rooms"
    })

if security:
    solutions.append({
        "Category": "Smart Security",
        "Solution": "Door cameras, fingerprint locks, motion alerts",
        "Benefits": "24x7 safety with mobile control"
    })

if theatre:
    solutions.append({
        "Category": "Home Theatre",
        "Solution": "Next-gen cinema experience with Control4/ABB integration",
        "Benefits": "Immersive audio-visual experience at one touch"
    })

if blinds:
    solutions.append({
        "Category": "Automated Shading",
        "Solution": "Motorized blinds with geofencing",
        "Benefits": "Daylight optimization, privacy, and aesthetics"
    })

if solutions:
    df = pd.DataFrame(solutions)
    st.dataframe(df, use_container_width=True)
else:
    st.info("☝️ Please select at least one lifestyle preference to get recommendations.")