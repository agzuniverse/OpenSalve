from django.urls import path

from . import views

urlpatterns = [
    path('', views.Camp.as_view()),
    # c/ Camp
    path('c/<int:id>', views.CampView.as_view()),
    path('c/<int:id>/inhabitants', views.CampInhabitantsView.as_view()),
    path('c/<int:id>/inhabitants/<int:inhab_id>',
         views.CampInhabitantsDelete.as_view()),
    path('c/<int:id>/stock', views.CampStockView.as_view()),
]
