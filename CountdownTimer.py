import streamlit as st
import time

# 🎨 Page Configuration
st.set_page_config(page_title="⏱️ Digital Countdown Timer", layout="centered")

# 🎨 Custom CSS for digital display
st.markdown("""
    <style>
    .digital-timer {
        font-family: 'Courier New', Courier, monospace;
        font-size: 80px;
        color: #39FF14;
        background: #000;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        box-shadow: 0 0 20px #39FF14;
    }
    .buttons {
        display: flex;
        justify-content: center;
        gap: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# 🕒 App Title
st.title("⏱️ **Digital Countdown Timer**")
st.caption("✨ *Looks like a real timer with Start / Pause / Reset buttons!*")

# 🕹️ State Initialization
if "time_left" not in st.session_state:
    st.session_state.time_left = 10
if "running" not in st.session_state:
    st.session_state.running = False

# 🎛️ Input for timer
if not st.session_state.running:
    start_time = st.number_input("Set countdown time (seconds):", min_value=1, max_value=3600, value=10, step=1)
    st.session_state.time_left = start_time

# 🖥️ Display Timer
st.markdown(f"<div class='digital-timer'>{st.session_state.time_left:02d}</div>", unsafe_allow_html=True)

# 🚀 Buttons
col1, col2, col3 = st.columns(3)

# ▶ Start Button
if col1.button("▶ Start"):
    st.session_state.running = True

# ⏸ Pause Button
if col2.button("⏸ Pause"):
    st.session_state.running = False

# 🔄 Reset Button
if col3.button("🔄 Reset"):
    st.session_state.running = False
    st.session_state.time_left = start_time

# ⏳ Countdown Logic
if st.session_state.running and st.session_state.time_left > 0:
    time.sleep(1)
    st.session_state.time_left -= 1
    st.rerun()  # ✅ Fixed: use st.rerun() instead of st.experimental_rerun()

# 🎉 Timer Complete
if st.session_state.time_left == 0 and st.session_state.running:
    st.session_state.running = False
    st.success("🎉 **Time's up! BOOM 💥**")
    st.balloons()

# 👣 Floating Footer
from muthu_footer import add_footer
add_footer()

