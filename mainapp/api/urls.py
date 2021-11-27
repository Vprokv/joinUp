from django.urls import path

from .views import ProgramTestAPIView

urlpatterns = [
    path('test-api/', ProgramTestAPIView.as_view(), name='program')
]