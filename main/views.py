from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name': 'main component',
        'amount': '100',
        'description': 'Component that is used for main component in the product ',
        'price': 'Rp 2.500.000',
        'date': 'Mon, 14 Jan 2023'
    }

    return render(request, 'main.html', context)
