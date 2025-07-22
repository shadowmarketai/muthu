import os
import streamlit as st
from dotenv import load_dotenv
import PyPDF2
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.embeddings import OpenAIEmbeddings
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain

# Load environment variables
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY"),modelname="gpt-4.0-mini",temperature=0.2

# Streamlit App Config
st.set_page_config(page_title="📄 Multi-PDF RAG Chatbot", layout="wide")
st.title("📄 Chat with Multiple PDFs (RAG)")
st.write("Upload one or more PDFs and start chatting across them!")

# Session state for chat history and vectorstore
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

# PDF Upload
uploaded_files = st.file_uploader("Upload PDFs", type=["pdf"], accept_multiple_files=True)

if uploaded_files:
    all_text = ""

    # Combine text from all PDFs
    for uploaded_file in uploaded_files:
        pdf_reader = PyPDF2.PdfReader(uploaded_file)
        for page in pdf_reader.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                all_text += extracted_text

    st.success(f"✅ Extracted text from {len(uploaded_files)} PDF(s).")

    # Text splitting
    st.info("🔄 Splitting text into chunks...")
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(all_text)

    # Embeddings and VectorStore
    st.info("🔄 Generating embeddings and building vector store...")
    embeddings = OpenAIEmbeddings(openai_api_key=OPENAI_API_KEY)
    vectorstore = FAISS.from_texts(chunks, embedding=embeddings)
    st.session_state.vectorstore = vectorstore

    st.success("✅ Knowledge base created. You can now ask questions!")

# Chat Interface
if st.session_state.vectorstore:
    retriever = st.session_state.vectorstore.as_retriever()
    chat_model = ChatOpenAI(
        temperature=0,
        openai_api_key=OPENAI_API_KEY,
        model_name="gpt-3.5-turbo"
    )
    qa_chain = ConversationalRetrievalChain.from_llm(
        llm=chat_model,
        retriever=retriever
    )

    user_question = st.text_input("💬 Ask a question about your PDFs:")
    if user_question:
        with st.spinner("Thinking..."):
            result = qa_chain.run({
                "question": user_question,
                "chat_history": st.session_state.chat_history
            })
            st.session_state.chat_history.append((user_question, result))
            st.markdown(f"**🤖 Answer:** {result}")

    # Display chat history
    if st.session_state.chat_history:
        st.markdown("---")
        st.markdown("### 📝 Chat History")
        for i, (q, a) in enumerate(st.session_state.chat_history):
            st.markdown(f"**Q{i+1}:** {q}")
            st.markdown(f"**A{i+1}:** {a}")

else:
    st.info("👆 Upload one or more PDFs to get started.")

# 👣 Footer
st.caption("🚀 Made with ❤️ using Streamlit")

from muthu_footer import add_footer
add_footer()

