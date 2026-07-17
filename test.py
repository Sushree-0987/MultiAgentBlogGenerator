from agents import (
    planner_agent,
    research_agent,
    writer_agent
)

topic = input("Enter blog topic: ")

print("\n========== PLANNER AGENT ==========\n")
outline = planner_agent(topic)
print(outline)

print("\n========== RESEARCH AGENT ==========\n")
research = research_agent(topic)
print(research)

print("\n========== WRITER AGENT ==========\n")
blog = writer_agent(
    topic,
    outline,
    research
)

print(blog)