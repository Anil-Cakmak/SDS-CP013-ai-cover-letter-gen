import streamlit as st
import google.generativeai as genai
import os

# Display instructions to the user
st.title("AI-Powered Cover Letter Generator")
st.write("Fill in the details below to generate a customized, professional cover letter.")

# Create input fields
textbox_company = st.text_input("Enter Company Name:")
textbox_job = st.text_input("Enter Job Title:")
textbox_resume = st.text_area("Enter Your Resume Summary:")
textbox_jobDescription = st.text_area("Enter Your Job Description:")


# Generate cover letter
if st.button("Generate Cover Letter"):
    if not textbox_company or not textbox_job or not textbox_resume:
        st.warning("Please fill in all fields before generating a cover letter.")
    else:
        with st.spinner("Generating your cover letter..."):
            try:
             
             # Configure API key (ensure it's the correct one)
                genai.configure(api_key='AIzaSyB4-JmJqX_k62xPLT9iavhYlPCRFcqI4dE')

                model = genai.GenerativeModel('models/gemini-pro')
                chat = model.start_chat()
         
                prompt = f"""
                You are an expert in professional writing. Create a compelling and customized cover letter for the position of {textbox_job} at {textbox_company}.
                Highlight relevant skills, achievements, and experiences. Ensure it maintains a professional tone and aligns with the job's requirements.

                Here is the resume content:
                {textbox_resume.strip()}

                Here is the Job Description:
                {textbox_job.strip()}
                Generate a cover letter that is engaging, concise, and tailored for the role.
                """
                response = chat.send_message(prompt)
        
               

                # Display the result
                st.subheader("Generated Cover Letter")
                st.write(response.text.strip())
            except Exception as e:
                st.error(f"Error generating cover letter: {e}")




