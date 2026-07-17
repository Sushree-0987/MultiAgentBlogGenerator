from workflow import app
from agents import editor_agent

topic = input("Enter Blog Topic: ")

result = app.invoke({
    "topic": topic
})

blog = result["grammar_blog"]

print("\n================ GENERATED BLOG ================\n")
print(blog)

approval = input("\nDo you approve this blog? (yes/no): ").lower()

if approval == "yes":
    print("\n================ FINAL BLOG ================\n")
    print(blog)

else:
    feedback = input("\nWhat changes do you want?\n")

    updated_blog = editor_agent(blog, feedback)

    print("\n================ UPDATED BLOG ================\n")
    print(updated_blog)