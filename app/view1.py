from django.shortcuts import render

from .views import group_required

@group_required('group 1')
def group_one_view(request):
    
    print("This is View 1")
    context = {"message": "This is View 1"}
    template_name = "app/view1.html"
    
    return render(request, template_name, context)