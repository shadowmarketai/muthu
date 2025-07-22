# web_rag_chatbot.py

import os
import streamlit as st
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# App Config
st.set_page_config(page_title="🌐 Web Scraper + PDF + RAG Chatbot", layout="wide")
st.title("🌐 Web Scraper + PDF Generator + RAG Chatbot")
st.write("Enter a website URL, generate a PDF, and chat with the content!")

# Input URL
url = st.text_input("🌍 Enter your website URL", value="https://www.shadowmarket.ai")

# Function to scrape website
def scrape_website(base_url, paths):
    all_text = ""
    for path in paths:
        full_url = base_url + path
        st.info(f"📥 Scraping: {full_url}")
        try:
            res = requests.get(full_url)
            soup = BeautifulSoup(res.text, "html.parser")
            for tag in soup.select("script, style, noscript"):
                tag.decompose()
            text = soup.get_text(separator="\n")
            all_text += f"\n\n--- {full_url} ---\n\n" + text.strip()
        except Exception as e:
            st.error(f"Failed to scrape {full_url}: {e}")
    return all_text

# Function to generate PDF
def generate_pdf(text, filename="website_content.pdf"):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    y = height - 40
    for line in text.splitlines():
        if y < 40:
            c.showPage()
            y = height - 40
        c.drawString(40, y, line[:80])  # truncate line length
        y -= 12
    c.save()

# Button to scrape and generate PDF
if st.button("📄 Scrape Website & Generate PDF"):
    with st.spinner("Scraping website and generating PDF..."):
        # Define paths to scrape
        paths = ["/", "/about/", "/services/"]  # Customize for your site
        site_text = scrape_website(url, paths)
        
        if site_text.strip():
            # Save PDF
            generate_pdf(site_text, "website_content.pdf")
            st.success("✅ PDF created successfully!")
            # Offer download
            with open("website_content.pdf", "rb") as f:
                st.download_button(
                    label="📥 Download Website PDF",
                    data=f,
                    file_name="website_content.pdf",
                    mime="application/pdf"
                )
        else:
            st.error("❌ No content found to generate PDF.")

# Build RAG chatbot
if os.path.exists("website_content.pdf"):
    st.markdown("---")
    st.subheader("💬 Chat with Website Content")
    
    # Process the PDF for RAG
    try:
        # Read PDF text
        import PyPDF2
        with open("website_content.pdf", "rb") as pdf_file:
            reader = PyPDF2.PdfReader(pdf_file)
            raw_text = ""
            for page in reader.pages:
                raw_text += page.extract_text() or ""
        
        # Text splitting
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(raw_text)

        # Embedding and vector store
        embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
        vectorstore = FAISS.from_texts(chunks, embedding=embeddings)

        # Chat model and chain
        retriever = vectorstore.as_retriever()
        chat_model = ChatOpenAI(temperature=0, openai_api_key=OPENAI_API_KEY, model_name="gpt-3.5-turbo")
        qa_chain = ConversationalRetrievalChain.from_llm(llm=chat_model, retriever=retriever)

        # User question
        user_q = st.text_input("🤔 Ask a question about the website:")
        if user_q:
            with st.spinner("Thinking..."):
                response = qa_chain.run({"question": user_q, "chat_history": []})
                st.write(f"**🤖 Answer:** {response}")

    except Exception as e:
        st.error(f"Error in chatbot setup: {e}")

else:
    st.info("👆 Scrape the website and generate a PDF to enable the chatbot.")

# 👣 Footer
st.caption("🚀 Made with ❤️ using Streamlit")

from muthu_footer import add_footer
add_footer()

