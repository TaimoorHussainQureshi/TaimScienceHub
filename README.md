
# PDF Assistant

## Description
This application, built using Streamlit, leverages the capabilities of GPT-3.5 to interactively answer questions based on the contents of a PDF document. Users can upload a PDF, and the application extracts its text, which can then be used as context for asking questions.

## Requirements
- Python 3.x
- Streamlit
- PyPDF2
- OpenAI API Key

## Installation
To set up this application, follow these steps:
1. Clone this repository to your local machine.
2. Install the required Python packages using `pip`:
   ```
   pip install streamlit PyPDF2 openai
   ```
3. You'll need an API key from OpenAI. Sign up at [OpenAI's website](https://openai.com/) and get your API key.

## Configuration
1. After obtaining the OpenAI API key, create a `secrets.toml` file in your project directory.
2. Add the following content to the `secrets.toml` file, replacing `your_api_key` with your actual API key:
   ```
   api_key = "your_api_key"
   ```

## Running the Application
To run the application, execute the following command in your project directory:
```
streamlit run app.py
```

## Usage
After starting the application:
1. Upload a PDF file using the provided interface.
2. Once the PDF is uploaded, it will be processed to extract the text.
3. Enter a question in the text box provided.
4. The application will use the extracted text as context to provide answers using OpenAI's GPT-3.5 model.
