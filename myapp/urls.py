from django.urls import path
from myapp.views import test_pdf  # 🚨 This is a class-based view in `serializers.py`, not in `views.py`

urlpatterns = [
    path('api/test-pdf/', test_pdf, name='test_pdf'),
]
