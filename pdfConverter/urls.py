from django.urls import path
from . import  views

urlpatterns = [
path('', views.Index, name='index'),
path('detail/', views.DetailListView, name='detail'),
path('pdf2image/', views.PdfConverter, name='pdf2image'),
path('update/<int:id>', views.UpdateListView, name='update'),
path('del/<int:id>', views.DeleteView, name='delete'),
]