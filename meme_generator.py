import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

# 🎨 Page Config
st.set_page_config(page_title="😂 Meme Generator", layout="centered")

st.title("😂 Meme Generator")
st.caption("✨ *Upload an image or pick a template & create hilarious memes instantly!*")

# 🖼️ Meme Templates
templates = {
    "Distracted Boyfriend": "https://i.imgur.com/JRhljIc.jpg",
    "Drake Hotline Bling": "https://i.imgur.com/Vw7YlyJ.jpg",
    "Success Kid": "https://i.imgur.com/u8TdrG0.jpg",
    "Grumpy Cat": "https://i.imgur.com/O6jWGBm.jpg"
}

# 📸 Image Selection
option = st.radio("Choose an image source:", ["📂 Upload your own", "🎨 Pick a template"])

if option == "📂 Upload your own":
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])
    if uploaded_file:
        img = Image.open(uploaded_file)
else:
    template_choice = st.selectbox("Choose a meme template", list(templates.keys()))
    response = requests.get(templates[template_choice])
    img = Image.open(BytesIO(response.content))

# 📝 Add Meme Text
st.markdown("### ✍️ Add Your Meme Text")
top_text = st.text_input("Top Text", value="When AI writes your memes")
bottom_text = st.text_input("Bottom Text", value="But it’s actually funny 😆")

# 🎨 Create Meme
if st.button("🎉 Generate Meme"):
    draw = ImageDraw.Draw(img)
    image_width, image_height = img.size

    # Font
    font_url = "https://github.com/google/fonts/raw/main/apache/impact/Impact.ttf"
    font_response = requests.get(font_url)
    font = ImageFont.truetype(BytesIO(font_response.content), size=int(image_height/10))

    # Outline Text Function
    def draw_text_with_outline(text, position):
        x, y = position
        for offset in [-2, -1, 0, 1, 2]:
            draw.text((x+offset, y), text, font=font, fill="black")
            draw.text((x, y+offset), text, font=font, fill="black")
        draw.text(position, text, font=font, fill="white")

    # Draw Top Text
    top_text = top_text.upper()
    text_width, text_height = draw.textsize(top_text, font=font)
    draw_text_with_outline(top_text, ((image_width-text_width)/2, 10))

    # Draw Bottom Text
    bottom_text = bottom_text.upper()
    text_width, text_height = draw.textsize(bottom_text, font=font)
    draw_text_with_outline(bottom_text, ((image_width-text_width)/2, image_height-text_height-20))

    # Display Meme
    st.image(img, caption="🎉 Your Meme", use_column_width=True)

    # Save Meme
    img.save("generated_meme.png")
    with open("generated_meme.png", "rb") as file:
        st.download_button("📥 Download Meme", file, file_name="meme.png", mime="image/png")

# 👣 Footer
from muthu_footer import add_footer
add_footer()
