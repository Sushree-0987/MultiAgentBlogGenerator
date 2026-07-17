import streamlit as st
from workflow import app
from pdf_generator import create_pdf

st.set_page_config(
    page_title="Multi-Agent Blog Generator",
    page_icon="📝",
    layout="wide"
)

st.title("📝 Multi-Agent Blog Generator")
st.write("Generate high-quality blogs using AI Agents.")

topic = st.text_input("Enter Blog Topic")

if st.button("🚀 Generate Blog"):

    if topic.strip() == "":
        st.warning("Please enter a blog topic.")

    else:
        with st.spinner("Generating blog... Please wait..."):

            result = app.invoke({
                "topic": topic
            })

        st.success("✅ Blog Generated Successfully!")

        st.subheader("📄 Generated Blog")

        # Display Final Grammar + SEO Blog
        st.markdown(result["grammar_blog"])

        # Create PDF
        pdf_file = create_pdf(result["grammar_blog"])

        # Download TXT
        st.download_button(
            label="📥 Download TXT",
            data=result["grammar_blog"],
            file_name="generated_blog.txt",
            mime="text/plain"
        )

        # Download PDF
        with open(pdf_file, "rb") as file:
            st.download_button(
                label="📄 Download PDF",
                data=file,
                file_name="generated_blog.pdf",
                mime="application/pdf"
            )