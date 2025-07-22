# pdf_generator.py
import requests
from bs4 import BeautifulSoup
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import io

# 🛠 Define pages to scrape
BASE_URL = "https://www.shadowmarket.ai"
paths = ["/", "/about/", "/services/"]
texts = []

for p in paths:
    r = requests.get(BASE_URL + p)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    # Extract visible text
    for tag in soup.select("script, style, noscript"):
        tag.decompose()
    text = soup.get_text(separator="\n")
    texts.append(f"--- {p} ---\n" + text.strip())

# 🖨 Create PDF
buffer = io.BytesIO()
c = canvas.Canvas(buffer, pagesize=letter)
width, height = letter
y = height - 40

for page in texts:
    for line in page.splitlines():
        if y < 40:
            c.showPage()
            y = height - 40
        c.drawString(40, y, line[:80])
        y -= 12
c.save()

with open("shadowmarket_content.pdf", "wb") as f:
    f.write(buffer.getvalue())

print("Created shadowmarket_content.pdf")

# 👣 Floating Footer
from muthu_footer import add_footer
add_footer()
