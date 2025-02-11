# Chat-Based Resume Creator

## Overview
Chat-Based Resume Creator is a powerful tool that helps users generate tailored resumes based on job requirements. Built using OpenAI, Streamlit, pdfplumber, and other technologies, this application allows users to interact with an AI assistant to refine their resumes dynamically.

## Features
- **OpenAI-Powered Chat Interface** – Customize resumes through a conversational AI.
- **Resume Parsing** – Extracts text from PDF, DOCX, or TXT files using pdfplumber.
- **Job-Specific Resume Optimization** – Tailors resumes to match job descriptions.
- **Interactive Editing** – Modify and adjust the generated resume via chat.
- **Downloadable Output** – Save the final resume in a preferred format.

## Tech Stack
- **OpenAI API** – AI-driven resume optimization.
- **Streamlit** – Web application framework for interactive UI.
- **pdfplumber** – PDF parsing and text extraction.
- **Python** – Backend logic and processing.

## How It Works

### 1. Enter Your OpenAI API Key
- On the first screen, input your OpenAI API key.
- Click the “Login” button to authenticate and proceed.

### 2. Upload Your Base Resume
- Click “Upload Resume” and select a file (PDF, DOCX, or TXT).
- Ensure the resume is clear and well-structured for optimal processing.

### 3. Access the Chat Screen
- After uploading, a chat interface appears.
- Interact with the AI to customize and refine your resume.

### 4. Input Job Requirements
- Type or paste job descriptions, key skills, or preferences.
- Specify any additional customization needs.

### 5. Generate Your New CV
- The system processes your input and generates a new tailored CV.
- Review and make adjustments as needed.

### 6. Copy Your CV
- Click the Copy button to copy your new resume.
- Optionally, regenerate the CV with different requirements.

## Installation & Setup

### Prerequisites
- Python 3.8+
- OpenAI API Key
- Required Python libraries (install using the command below)

### Installation
```sh
# Clone the repository
git clone https://github.com/yourusername/chat-resume-creator.git
cd chat-resume-creator

# Install dependencies
pip install -r requirements.txt

# Run the application
streamlit run app.py
```

## Usage
1. Run the application using `streamlit run app.py`.
2. Enter your OpenAI API key.
3. Upload your resume.
4. Interact via chat to generate a tailored resume.
5. Download and use the final CV.

## Contributing
Contributions are welcome! Feel free to submit issues and pull requests.

## Contact
For any inquiries, reach out via [your contact email] or open an issue on GitHub.

---
Developed with ❤️ using OpenAI and Streamlit.
