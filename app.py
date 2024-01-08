import streamlit as st
from PyPDF2 import PdfReader
import openai

# Authenticate OpenAI with your API key 


openai.api_key = st.secrets["api_key"]


def extract_text_from_pdf(uploaded_file):
    pdf_reader = PdfReader(uploaded_file)
    text = ''
    for page in pdf_reader.pages:
        text += page.extract_text()
    return text


def ask_question(context, question):
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"You are reading a document about:\n\n{context}\n\nQuestion: {question}"},
            {"role": "user", "content": question}
        ],
    )
    answer = completion['choices'][0]['message']['content']
    return answer


def main():
    st.title("PDF CHAT BOT")

    st.write("Upload a PDF file")
    uploaded_file = st.file_uploader("Choose a PDF file", type="pdf")

    if uploaded_file is not None:
        file_contents = uploaded_file.read()
        st.write("File uploaded successfully!")

        
        pdf_info = PdfReader(uploaded_file)
        

        
        text = extract_text_from_pdf(uploaded_file)
        

        
        question = st.text_input("Ask a question about the PDF")

        if st.button("Get Answer"):
            if question:
                
                answer = ask_question(text, question)
                st.write("### Answer:")
                st.write(answer)
            else:
                st.write("Please enter a question.")

if __name__ == "__main__":
    main()
