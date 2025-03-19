from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

import json

class GenerateInvoicePDF(APIView):

    def post(self, request):
        serializer = GenerateInvoicePDF(data=request.data)

        if not serializer.is_valid():
            return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

        invoice_data = serializer.validated_data

        try:
            # ✅ Render the HTML template with invoice data
            html_content = render_to_string("pdf_template.html", invoice_data)

            # ✅ Convert HTML to PDF
            pdf = HTML(string=html_content).write_pdf()

            # ✅ Return PDF response
            response = HttpResponse(pdf, content_type="application/pdf")
            response["Content-Disposition"] = "inline; filename=invoice.pdf"

            return response

        except Exception as e:
            return JsonResponse({"error": f"PDF Generation Failed: {str(e)}"}, status=500)
