from django.urls import path
from .views import CreateAPiView,ListAPiView,UpdateStatus

urlpatterns = [
    path('get/', ListAPiView.as_view()),
    path('create/', CreateAPiView.as_view()),
    path('update/<int:book_id>/', UpdateStatus.as_view()),
]
