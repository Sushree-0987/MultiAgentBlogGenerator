from typing import TypedDict
from langgraph.graph import StateGraph, START, END

from agents import (
    planner_agent,
    research_agent,
    writer_agent,
    seo_agent,
    grammar_agent
)


class BlogState(TypedDict):
    topic: str
    outline: str
    research: str
    blog: str
    seo_blog: str
    grammar_blog: str

def planner_node(state: BlogState):
    outline = planner_agent(state["topic"])
    return {
        "outline": outline
    }


def research_node(state: BlogState):
    research = research_agent(state["topic"])
    return {
        "research": research
    }


def writer_node(state: BlogState):
    blog = writer_agent(
        state["topic"],
        state["outline"],
        state["research"]
    )
    return {
        "blog": blog
    }

def seo_node(state: BlogState):
    seo_blog = seo_agent(state["blog"])

    return {
        "seo_blog": seo_blog
    }

def grammar_node(state: BlogState):

    grammar_blog = grammar_agent(state["seo_blog"])

    return {
        "grammar_blog": grammar_blog
    }


graph = StateGraph(BlogState)

graph.add_node("planner", planner_node)
graph.add_node("research", research_node)
graph.add_node("writer", writer_node)
graph.add_node("seo", seo_node)
graph.add_node("grammar", grammar_node)

graph.add_edge(START, "planner")
graph.add_edge("planner", "research")
graph.add_edge("research", "writer")
graph.add_edge("writer", "seo")
graph.add_edge("seo", "grammar")
graph.add_edge("grammar", END)

app = graph.compile()