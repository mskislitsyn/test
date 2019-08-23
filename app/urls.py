from django.urls import path

from app.view1 import group_one_view
from app.view2 import group_two_view
from app.views import index

urlpatterns = [
    path('', index, name="index"),
    path('view1/', group_one_view, name="group_one_view"),
    path('view2/', group_two_view, name='group_two_view'),
]