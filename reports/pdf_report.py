from reportlab.platypus import (
    SimpleDocTemplate,
    Paragraph
)

from reportlab.lib.styles import (
    getSampleStyleSheet
)

def create_report():

    file_name = "sales_report.pdf"

    doc = SimpleDocTemplate(
        file_name
    )

    styles = getSampleStyleSheet()

    story = []

    story.append(
        Paragraph(
            "AI Sales Intelligence Report",
            styles["Title"]
        )
    )

    story.append(
        Paragraph(
            "Generated Successfully",
            styles["Normal"]
        )
    )

    doc.build(story)

    return file_name