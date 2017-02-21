from django.shortcuts import render
from classlist.utils import get_class_list

# Create your views here.
def default_view(request):
    class_list = get_class_list()
    print("Class List:",class_list)
    return render(request,'default.html', {'object_list':class_list})

