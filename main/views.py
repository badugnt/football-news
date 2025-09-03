from django.shortcuts import render
def show_main(request):
    context = {
        'npm' : '2406410494',
        'name': 'Edlyn Marva',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)
# Create your views here.
