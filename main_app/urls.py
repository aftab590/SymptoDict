from django.urls import path , re_path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path('admin_ui', views.admin_ui , name='admin_ui'),
    path('patient_ui', views.patient_ui , name='patient_ui'),
    path('doctor_ui', views.doctor_ui , name='doctor_ui'),
    path('pviewprofile/<str:patientusername>', views.pviewprofile , name='pviewprofile'),
    path('dviewprofile/<str:doctorusername>', views.dviewprofile , name='dviewprofile'),
    path('pconsultation_history', views.pconsultation_history , name='pconsultation_history'),
]