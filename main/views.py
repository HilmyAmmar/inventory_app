from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'Piece of Eden',
        'amount': '1',
        'description': 'Technologically advanced pieces of equipment created by First Civilization',
        'price': '$100.000.000.000.000',
        'date': 'Mon, 14 Jan 2023'
    }

    return render(request, 'main.html', context)
