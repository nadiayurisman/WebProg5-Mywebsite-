from django.urls import path
from appsnad import views

app_name = 'appsnad'
urlpatterns = [
   path('', views.readStudent, name='read-data-student'),
   path('create/', views.createStudent, name='create-data-student'),
   path('update/<str:id>', views.updateStudent, name='update-data-student'),
   path('delete/<str:id>', views.deleteStudent, name='delete-data-student')
]
