import streamlit as st
from templates import template
import pdfplumber
import openai
import os

resume_text = None

def chat_screen():
    global resume_text
    openai.api_key = os.getenv("OPEN_API_KEY")
    linkedin = ("/").join(["https://www.linkedin.com/in",os.getenv("LINKEDIN_USER")])
    github = ("/").join(["https://github.com",os.getenv("GITHUB_USER")])
    st.title("Resume ChatGPT")
    
    if st.sidebar.button("*Logout 🔒*"):
        st.session_state.logged_in = False
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
    uploaded_resume = st.sidebar.file_uploader("Resume file", type=["pdf","docx"])

    
    def enhance_resume(resume_txt, job_requirements):
        prompt = f"""
        Role:
        You are a highly skilled resume expert specializing in enhancing and tailoring resumes to align with specific job requirements. Your expertise lies in refining resumes to highlight the most relevant skills, achievements, and experiences, ensuring they align with the target role's expectations.

        Task:
        You will be provided with:
        - An existing resume.
        - A set of job requirements for a specific role.
        - Your goal is to generate a refined resume in Markdown format as per output format.

        Enhancements to Apply:
            - Alignment with Job Requirements: Modify and emphasize skills, experiences, and accomplishments that best match the job description.
            - Bullet Points for Impact: Ensure each work experience entry contains exactly five compelling bullet points, highlighting key contributions and quantifiable achievements.
            - Invented/Expanded Content: If necessary, infer or creatively enhance project descriptions, job tasks, or impact statements to better fit the target role.
            - Consistency & Readability: Maintain professional formatting, clarity, and readability. Ensure the resume is concise yet detailed.
            - Additional Sections: Include LinkedIn URL: {linkedin} and GitHub URL: {github} if applicable or available, ensuring a comprehensive and well-rounded professional profile.
            - Output Format: The final output must be structured in Markdown format as per {template}.
        """
        response = openai.chat.completions.create(
            model="gpt-4o-mini",
            temperature=0,
            messages=[
                {
                    "role": "system",
                    "content": prompt
                },
                {
                    "role": "user",
                    "content": f"Create a new resume using the provided resume data: {resume_txt}. Here is the job description to tailor the resume to: {job_requirements}."
                }
            ]
        )
        
        updated_resume = response.choices[0].message.content
        with st.chat_message("assistant"):st.code(updated_resume)
        st.session_state.messages.append(
            
                {
                    "role": "user",
                    "content": user_input
                }
            
        )
        
        st.session_state.messages.append(
            
                {
                    "role": "assistant",
                    "content": updated_resume
                }
        )
        
    if uploaded_resume:
        if resume_text is None:
             with pdfplumber.open(uploaded_resume) as pdf:
                resume_text = "\n".join(page.extract_text() for page in pdf.pages if page.extract_text())
    
    if "messages" not in st.session_state:
            st.session_state["messages"] = [{"role": "assistant", "content": "How can I help you?"}]

    for msg in st.session_state["messages"]:
        st.chat_message(msg["role"]).code(msg["content"])
            
    user_input = st.chat_input("Message Resume-GPT")

    if user_input:
        with st.chat_message("user"):st.code(user_input)
        enhance_resume(resume_text, user_input)    
 
        
    
        

def login_screen():
    st.subheader("💼 Welcome to Resume-GPT:Tailored Resumes in Minutes")
    st.markdown("To get started visit [Link](https://platform.openai.com/api-keys) to generate key.")
    st.text("1.Input your OpenAI API key () and click “Login” to proceed\n2.Upload your resume file (PDF) to the system.\n3.In the chat screen, enter job requirements to generate a tailored CV.\n4.Review if needed and copy the enhanced CV.That’s it! Quick and easy.")
    open_api_key = st.text_input("OpenAI API Key", type="password")
    linkedin_user = st.text_input("LinkedIn username (optional) – After 'linkedin.com/in/' in URL", placeholder="Enter username")
    github_user = st.text_input("GitHub username (optional) – After 'github.com/' in URL", placeholder="Enter username")
    if st.button("Login", use_container_width=True, type='primary'):
        if open_api_key != "":
            st.session_state.logged_in = True
            os.environ["OPEN_API_KEY"] = open_api_key
            os.environ["LINKEDIN_USER"] = linkedin_user
            os.environ["GITHUB_USER"] = github_user
            st.rerun()
        else:
            st.error("INVALID API KEY")

def main():
    global resume_text
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if not st.session_state.logged_in:
        resume_text = None
        login_screen()
    else:
        chat_screen()

if __name__ == "__main__":
    main()