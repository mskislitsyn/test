from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

@login_required
def index(request):
    
    template_name = "app/index.html"
    
    return render(request, template_name)


def group_required(*group_names):

    def in_groups(user):
        if user.is_authenticated:
            if user.groups.filter(name__in=group_names) or user.is_superuser:
                return True
        return False

    return user_passes_test(in_groups)