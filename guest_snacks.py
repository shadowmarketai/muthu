import streamlit as st

# 🎨 Add background gradient and animations with custom CSS
st.markdown("""
    <style>
    /* Background gradient */
    body {
        background: linear-gradient(135deg, #fceabb, #f8b500);
        color: #333333;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    /* Animated button */
    .stButton button {
        background: linear-gradient(90deg, #ff9966, #ff5e62);
        color: white;
        font-weight: bold;
        border: none;
        border-radius: 10px;
        padding: 0.5em 1em;
        transition: all 0.3s ease;
    }
    .stButton button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 15px rgba(0,0,0,0.2);
    }
    /* Animated header */
    .stApp h1 {
        animation: fadeSlideDown 1.2s ease-out forwards;
        opacity: 0;
    }
    @keyframes fadeSlideDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0px);
        }
    }
    </style>
""", unsafe_allow_html=True)

# 🌟 App title and introduction
st.title("🍹 **Welcome, Guest! Let’s Plan Your Perfect Snack**")
st.caption("🌸 _Tell us what you’d love today, and we’ll make it special._ ✨")

# 👤 Name input
name = st.text_input("👤 **What’s your name?**")

# ☕ Beverage Selection
st.subheader("🥤 **Pick Your Favorite Drink**")
beverage = st.selectbox("👉 Choose a beverage:", ["None", "Coffee ☕", "Tea 🍵"])

beverage_type = ""
beverage_sugar = ""
juice = "None"
juice_sugar = ""

# ☕ Coffee / Tea Options
if beverage == "Coffee ☕":
    beverage_type = st.selectbox("☕ **Which coffee do you prefer?**", ["Black Coffee", "Milk Coffee", "Cappuccino"])
    beverage_sugar = st.radio("🍬 **How do you like your coffee?**", ["With Sugar", "Without Sugar"])

elif beverage == "Tea 🍵":
    beverage_type = st.selectbox("🍵 **Pick your tea style**", ["Green Tea", "Masala Tea", "Milk Tea"])
    beverage_sugar = st.radio("🍬 **Sugar in Tea?**", ["With Sugar", "Without Sugar"])

# 🍹 Juice Options
if beverage == "None":
    st.subheader("🍹 **Or Maybe a Refreshing Juice?**")
    juice = st.selectbox("🍊 Choose a juice:", ["None", "Lemon 🍋", "Pomegranate ❤️", "Watermelon 🍉"])
    juice_sugar = st.radio("🍬 **Sugar in Juice?**", ["With Sugar", "Without Sugar"])

# 🥪 Snacks Selection
st.subheader("🍴 **Pick a Snack to Enjoy**")
snack = st.selectbox("👉 Choose a snack:", ["None", "Samosa 🥟", "Grilled Sandwich 🥪", "Pastry 🍰"])

# 🎉 Submit Button
if st.button("🎉 Confirm My Order"):
    st.success("✅ _Awesome! We’ve recorded your preferences._ 🌟")

    st.markdown("## 📝 **Your Guest Summary**")
    st.markdown(f"👤 **Name:** `{name if name else 'Guest'}`")

    if beverage != "None":
        st.markdown(f"☕ **Beverage:** {beverage} (*{beverage_type}, {beverage_sugar}*)")
    else:
        st.markdown(f"🍹 **Juice:** {juice} (*{juice_sugar}*)")

    st.markdown(f"🍴 **Snack:** {snack}")

    st.balloons()
    st.info("✨ _Sit back and relax while we prepare your treats!_ 🍪☕")

# Floating footer
from muthu_footer import add_footer
add_footer()
