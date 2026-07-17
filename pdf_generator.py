from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet

def create_pdf(blog, filename="generated_blog.pdf"):
    doc = SimpleDocTemplate(filename)
    styles = getSampleStyleSheet()

    story = []

    for line in blog.split("\n"):
        story.append(Paragraph(line, styles["BodyText"]))

    doc.build(story)

    return filename