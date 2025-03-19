import json
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from rest_framework.decorators import api_view
from weasyprint import HTML


@api_view(['POST'])
def GenerateInvoicePDF(request):
    print("✅ Received Request Data:", request.data)  # Debugging
    try:
        invoice_data = request.data

        # Check if 'items' is a list
        if not isinstance(invoice_data.get("items"), list):
            print("❌ Error: 'items' should be a list")
            return JsonResponse({"error": "'items' must be a list"}, status=400)

        # Render template
        html_content = render_to_string("pdf_template.html", invoice_data)
        print("✅ HTML Generated Successfully")  # Debugging

        # Convert to PDF
        pdf = HTML(string=html_content).write_pdf()
        print("✅ PDF Generated Successfully")  # Debugging

        return HttpResponse(pdf, content_type="application/pdf")

    except Exception as e:
        print("❌ Error during PDF generation:", str(e))  # Debugging
        return JsonResponse({"error": f"PDF Generation Failed: {str(e)}"}, status=500)
