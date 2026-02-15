import os
import io
from pypdf import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm

FOLDER = r"F:\Courcses\website\Learn-Physics-with-problems\docs\diff eqn"
OUTPUT_NAME = "Merged_With_File_Titles.pdf"

def make_title_page_pdf(title: str, subtitle: str = "") -> PdfReader:
    """
    Create a one-page PDF in memory with a centered title (and optional subtitle).
    Returns a PdfReader for that in-memory PDF.
    """
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    width, height = A4

    # Background (optional, comment out if you want pure white)
    # c.setFillGray(0.97)
    # c.rect(0, 0, width, height, fill=1, stroke=0)
    # c.setFillGray(0)

    # Title
    c.setFont("Helvetica-Bold", 24)
    c.drawCentredString(width / 2, height * 0.62, "Next file:")

    # Filename (wrapped manually into multiple lines if too long)
    c.setFont("Helvetica", 18)
    max_chars = 60  # simple wrap control
    lines = []
    t = title.strip()
    while len(t) > max_chars:
        cut = t.rfind(" ", 0, max_chars)
        if cut == -1:
            cut = max_chars
        lines.append(t[:cut].strip())
        t = t[cut:].strip()
    if t:
        lines.append(t)

    y = height * 0.52
    line_gap = 26
    for line in lines[:6]:  # avoid endless pages if name is huge
        c.drawCentredString(width / 2, y, line)
        y -= line_gap

    # Subtitle (optional)
    if subtitle:
        c.setFont("Helvetica-Oblique", 12)
        c.drawCentredString(width / 2, height * 0.35, subtitle)

    # Footer hint
    c.setFont("Helvetica", 10)
    c.drawString(2 * cm, 1.5 * cm, "Separator page automatically inserted during merge.")

    c.showPage()
    c.save()
    buf.seek(0)
    return PdfReader(buf)

def main():
    # Collect and sort PDFs (exam_*.pdf)
    pdf_files = sorted([
        os.path.join(FOLDER, f)
        for f in os.listdir(FOLDER)
        if f.lower().endswith(".pdf") and f.startswith("exam_")
    ])

    if not pdf_files:
        raise FileNotFoundError(f"No matching PDFs found in: {FOLDER}")

    writer = PdfWriter()

    for pdf_path in pdf_files:
        base = os.path.basename(pdf_path)

        # 1) Insert a title/separator page for the NEXT file (i.e., this pdf we're about to add)
        title_reader = make_title_page_pdf(base)
        writer.add_page(title_reader.pages[0])

        # 2) Append the PDF itself
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            writer.add_page(page)

    output_path = os.path.join(FOLDER, OUTPUT_NAME)
    with open(output_path, "wb") as f_out:
        writer.write(f_out)

    print("✅ Done!")
    print("📄 Saved to:", output_path)

if __name__ == "__main__":
    main()
