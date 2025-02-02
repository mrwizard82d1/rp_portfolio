from django.shortcuts import render

# Create your views here.
def home(request):
    """
    Return the home page
    :param request:
    :return:
    """
    return render(request, 'pages/home.html')
