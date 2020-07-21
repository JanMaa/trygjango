from django.shortcuts import render, get_object_or_404
from django.views import View

from .models import Course

# BASE VIEW CLASS = VIEW

class CourseView(View):
	template_name = 'function_views/course_detail.html'
	# GEY Method
	def get(self, request, id=None, *args, **kwargs):
		context = {}
		if id is not None:
			obj = get_object_or_404(Course, id=id)
			context['object'] = obj
		return render(request, self.template_name, context)

	# def get(request, *args, **kwargs):
	# return render(request, 'about.html', {})


# HTTP METHODS

def my_fbv(request, *args, **kwargs):
	return render(request, 'about.html', {})
