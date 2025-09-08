from django.shortcuts import render

def show_main(request):
    context = {
        'title': 'Selcaster United Shop',
        'npm' : '2406496233',
        'name': 'Razan M Salim',
        'class': 'PBP B'
    }

    return render(request, "main.html", context)

# Create your views here.
