import streamlit as st
import fitz  # PyMuPDF

st.set_page_config(page_title="Face Detection Using Computer Vision", layout="wide")

st.title("Face Detection Using Computer Vision by GeekAI")

# PDF file options
pdf_files = {
    "1. Face Detection Report": "1.pdf",
    "2. Receipt Segmentation Workflow": "2.pdf",
    "3. Resume Analyzer Report": "3.pdf"
}

# Select box to choose file
selected_option = st.selectbox("Choose a report to view:", list(pdf_files.keys()))

# Extract text function
def extract_text_from_pdf(file_path):
    with fitz.open(file_path) as doc:
        text = ""
        for page in doc:
            text += page.get_text()
        return text

# Display PDF content
selected_file_path = pdf_files[selected_option]

if os.path.exists(selected_file_path):
    st.success(f"Showing content from: {selected_option}")
    pdf_text = extract_text_from_pdf(selected_file_path)
    st.markdown("### 📄 Extracted Report Content")
    st.text_area("Text Output", pdf_text, height=600)
else:
    st.error(f"File not found: {selected_file_path}. Please make sure it exists in the app directory.")
