import re
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.utils import simpleSplit

def generate_pdf(report_text, filename="report.pdf"):
    """
    Generates a professionally formatted PDF report with proper Markdown-style formatting.

    :param report_text: Text content for the PDF
    :param filename: Name of the PDF file
    :return: Path to the generated PDF file
    """
    c = canvas.Canvas(filename, pagesize=letter)
    
    # Page setup
    width, height = letter
    left_margin = 50
    top_margin = height - 50
    y_position = top_margin

    # Title
    c.setFont("Helvetica-Bold", 16)
    c.drawString(left_margin, y_position, "AI Generated Report")
    y_position -= 30  # Space below title

    # Process each line
    for line in report_text.split("\n"):
        line = line.strip()

        # Handle Headers
        if line.startswith("# "):  # H1
            c.setFont("Helvetica-Bold", 16)
            line = line.replace("# ", "")
        elif line.startswith("## "):  # H2
            c.setFont("Helvetica-Bold", 14)
            line = line.replace("## ", "")
        elif line.startswith("### "):  # H3
            c.setFont("Helvetica-Bold", 12)
            line = line.replace("### ", "")
        else:
            c.setFont("Helvetica", 12)

        # Handle Bold (**bold**)
        line = re.sub(r"\*\*(.*?)\*\*", r"\1", line)  # Remove ** but keep text

        # Handle Lists (- item, • item, 1. item)
        if re.match(r"^\d+\.\s", line):  # Ordered list (1. item)
            line = "  " + line  # Indent for ordered lists
        elif line.startswith("- ") or line.startswith("• "):  # Unordered list (- item, • item)
            line = "• " + line[2:]  # Convert to bullet points

        # Handle text wrapping
        wrapped_lines = simpleSplit(line, "Helvetica", 12, width - 100)
        for wrapped_line in wrapped_lines:
            c.drawString(left_margin, y_position, wrapped_line)
            y_position -= 18  # Line spacing

            # Handle page breaks
            if y_position < 50:  
                c.showPage()  # Create new page
                y_position = top_margin

    c.save()
    return filename
