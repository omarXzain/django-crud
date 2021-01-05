from django.urls import path, include
from .views import HomeView, CrudDetailsView, CrudCreateView, CrudUpdateView, CrudDeleteView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('<int:pk>/', CrudDetailsView.as_view(), name='crud_details'),
        path('add/', CrudCreateView.as_view(), name='crud_create'),
    path('<int:pk>/update/', CrudUpdateView.as_view(), name='crud_update'),
    path('<int:pk>/delete/', CrudDeleteView.as_view(), name='crud_delete'),
]