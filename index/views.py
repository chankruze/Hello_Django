from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'insert_me':"Now I am inserted from first_app/index.html" }
    return render(request, 'index/index.html', context = my_dict)
