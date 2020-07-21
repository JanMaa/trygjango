from django.urls import path

from .views import (
	#my_fbv,
	CourseView,
)
app_name = 'function_views'
urlpatterns = [
    path('', CourseView.as_view(template_name='contact.html'), name='courses-list'),
    path('<int:id>/', CourseView.as_view(), name='courses-detail'),
]
