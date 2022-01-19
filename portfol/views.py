from django.shortcuts import render
from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter

def home(request):
    return render(request, 'index.html')


def pdf(request):
    buf = io.BytesIO()
    c = canvas.Canvas(buf, pagesize=letter,bottomup=0)
    textob = c.beginText()
    textob.setTextOrigin(inch, inch)
    textob.setFont('Helvetica', 14)
    
    lines = "D:\Python\one-page-website-html-css-project-for-practice-master\media"
    
    for line in lines:
        textob.textLine(line)
        
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf, as_attachment=True, filename='venue.pdf')