from dotenv import load_dotenv
import os

load_dotenv()

from langchain_groq import ChatGroq

llm = ChatGroq(
    model="openai/gpt-oss-20b",
    api_key=os.getenv("GROQ_API_KEY")
)

def planner_agent(topic):
    prompt = f"""
    You are a professional blog planner.

    Create a detailed outline for a blog on:
    {topic}

    Include:
    - Title
    - Introduction
    - Main Headings
    - Subheadings
    - Conclusion
    """

    response = llm.invoke(prompt)
    return response.content

def research_agent(topic):

    prompt = f"""
    You are a professional researcher.

    Research the following topic:

    {topic}

    Give:
    - Important facts
    - Latest trends
    - Advantages
    - Challenges
    - Real-world examples

    Write the research in simple points.
    """

    response = llm.invoke(prompt)

    return response.content

def writer_agent(topic, outline, research):

    prompt = f"""
    You are a professional blog writer.

    Topic:
    {topic}

    Blog Outline:
    {outline}

    Research:
    {research}

    Using the outline and research above,
    write a professional blog.

    Requirements:
    - Attractive title
    - Introduction
    - Detailed explanation
    - Use headings
    - Use simple English
    - Around 400–500 words
    - End with a conclusion
    """

    response = llm.invoke(prompt)

    return response.content

def seo_agent(blog):

    prompt = f"""
    You are an SEO Expert.

    Improve the following blog for SEO.

    Instructions:
    1. Add an SEO-friendly title.
    2. Write a Meta Description (2-3 lines).
    3. Add 8 SEO Keywords.
    4. Improve headings.
    5. Keep the content easy to read.

    Blog:
    {blog}
    """

    response = llm.invoke(prompt)

    return response.content

def grammar_agent(blog):

    prompt = f"""
    You are an English Grammar Expert.

    Improve the following blog.

    Instructions:
    - Correct grammar mistakes.
    - Improve sentence structure.
    - Improve readability.
    - Do NOT remove any information.
    - Keep the meaning the same.

    Blog:
    {blog}
    """

    response = llm.invoke(prompt)

    return response.content

def editor_agent(blog, feedback):

    prompt = f"""
    You are a professional blog editor.

    Here is the blog:

    {blog}

    The user requested these changes:

    {feedback}

    Rewrite the blog according to the user's feedback.

    Keep the blog professional and well-structured.
    """

    response = llm.invoke(prompt)

    return response.content