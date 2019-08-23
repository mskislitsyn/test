from django.shortcuts import render

from .views import group_required

@group_required('group 2')
def group_two_view(request):
    
    print("This is View 2")
    context = {"message": "This is View 2"}
    template_name = "app/view2.html"
    
    return render(request, template_name, context)