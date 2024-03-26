from django.contrib import admin
from django.urls import path


#  views imports
from .views import QuestionCategoryAPIView
urlpatterns = [
    path('questions/', QuestionCategoryAPIView.as_view(), name='question_category_api'),
    path('questions/<int:pk>/', QuestionCategoryAPIView.as_view(), name='question_category_api_detail'),
    path('questions/delete/<int:pk>/', QuestionCategoryAPIView.as_view(), name='question_category_api_delete'),
    path('category/delete/<int:pk>/', QuestionCategoryAPIView.as_view(), name='question_category_api_delete'),
]

