from django.urls import path
from . import views

urlpatterns = [
    path('', views.PessoaListCreateAPIView.as_view(), name='pessoa-list-create'),
    path('<int:pk>/', views.PessoaRetrieveUpdateDestroyAPIView.as_view(), name='pessoa-detail'),
]
