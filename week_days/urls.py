from django.urls import path
from . import views

urlpatterns = [
    path('<int:w_day>', views.get_info_about_w_days_by_number),
    path('<str:w_day>', views.get_info_about_w_days, name='week_d-name'),
]