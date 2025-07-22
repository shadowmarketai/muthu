import streamlit as st
from PIL import Image, ImageDraw, ImageFont
import qrcode
import io

# 🌟 App Config
st.set_page_config(page_title="🎖️ Pro Name Badge Generator", layout="centered")
st.title("🎖️ Pro Name Badge Generator")
st.caption("✨ Create stunning badges with templates, borders, and logos!")

# 📥 Separate Name Inputs
st.subheader("✍️ Enter Your Name:")
first_name = st.text_input("First Name (Required):")
middle_name = st.text_input("Middle Name (Optional):")
last_name = st.text_input("Last Name (Required):")

# 🎨 Badge Style Selection
styles = {
    "🎨 Last, First": lambda f, m, l: f"{l}, {f} {m}".strip(),
    "✒️ Initials": lambda f, m, l: f"{f[0].upper()}.{m[0].upper() + '.' if m else ''}{l[0].upper()}",
    "🔡 Uppercase": lambda f, m, l: f"{f.upper()} {m.upper()} {l.upper()}".strip(),
    "🔠 Lowercase": lambda f, m, l: f"{f.lower()} {m.lower()} {l.lower()}".strip(),
    "👤 First Last": lambda f, m, l: f"{f} {m} {l}".strip()
}
selected_style = st.selectbox("Choose Badge Style:", list(styles.keys()))

# 🖼️ Template Options
template = st.selectbox(
    "Select Badge Template:",
    ["🟥 Rectangular", "⭕ Rounded", "🌈 Gradient Background"]
)

# 🎨 Customization Options
bg_color = st.color_picker("Pick Badge Background Color 🎨", "#4CAF50")
text_color = st.color_picker("Pick Text Color 🖌️", "#FFFFFF")
font_size = st.slider("Select Font Size", min_value=20, max_value=80, value=40)

# 🖼️ Upload Logo
logo_file = st.file_uploader("Upload Logo (PNG/JPG)", type=["png", "jpg", "jpeg"])

# 🔲 QR Code Option
add_qr = st.checkbox("Add QR Code to Badge?")
qr_content = ""
if add_qr:
    qr_content = st.text_input("Enter text or URL for QR Code:", f"{first_name} {last_name}")

# 🖋️ Font Loader
def get_font(size):
    try:
        return ImageFont.truetype("arial.ttf", size)  # Windows
    except:
        return ImageFont.load_default()  # Fallback

# 🏷️ Generate Badge
if first_name.strip() and last_name.strip():
    # Build badge text
    badge_text = styles[selected_style](first_name.strip(), middle_name.strip(), last_name.strip())

    # 🎨 Create Badge Image
    img = Image.new("RGB", (600, 300), color=bg_color)
    draw = ImageDraw.Draw(img)
    font = get_font(font_size)

    # 🖌️ Apply Template
    if template == "⭕ Rounded":
        draw.rounded_rectangle([10, 10, 590, 290], radius=50, fill=bg_color, outline="white", width=8)
    elif template == "🌈 Gradient Background":
        for y in range(300):
            gradient_color = (int(bg_color[1:3], 16) + y * 2) % 256
            draw.line([(0, y), (600, y)], fill=(gradient_color, 100, 200), width=1)

    # 🖋️ Center Text (using textbbox for Pillow 10+)
    bbox = draw.textbbox((0, 0), badge_text, font=font)
    w = bbox[2] - bbox[0]
    h = bbox[3] - bbox[1]
    draw.text(((600 - w) / 2, (300 - h) / 2), badge_text, fill=text_color, font=font)

    # 🖼️ Add Logo (Optional)
    if logo_file is not None:
        logo = Image.open(logo_file).convert("RGBA")
        logo.thumbnail((100, 100))
        img.paste(logo, (30, 30), logo)

    # 🔲 Add QR Code (Optional)
    if add_qr and qr_content.strip():
        qr = qrcode.QRCode(box_size=3, border=1)
        qr.add_data(qr_content)
        qr.make(fit=True)
        qr_img = qr.make_image(fill="black", back_color="white")
        qr_img = qr_img.resize((100, 100))
        img.paste(qr_img, (480, 180))  # Place QR bottom-right

    # 🖼️ Display Badge
    st.subheader("🎉 Your Name Badge:")
    st.image(img)

    # 📥 Download Badge
    buf = io.BytesIO()
    img.save(buf, format="PNG")
    byte_im = buf.getvalue()
    st.download_button(
        label="📥 Download Badge as PNG",
        data=byte_im,
        file_name="name_badge.png",
        mime="image/png"
    )
else:
    st.info("👆 Please enter **First** and **Last Name** to generate your badge.")

# 🔄 Reset Button
if st.button("🔄 Reset"):
    st.session_state.clear()
    st.rerun()

# 👣 Floating Footer
try:
    from muthu_footer import add_footer
    add_footer()
except:
    st.caption("Made with ❤️ by Muthu")
    