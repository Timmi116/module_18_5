from django.shortcuts import render

# Create your views here.


def platform(request):
    return render(request, 'platform.html')


def games_store(request):
    main_page = 'Компьютерные игры'
    name_game = ['The Elder Scrolls 5: Skyrim', 'Grand Theft Auto 5', 'Call of Duty: Modern Warfare 2']
    context = {
        'main_page': main_page,
        'name_game': name_game,
    }
    return render(request, 'games.html', context)


def cart_of_store(request):
    return render(request, 'cart.html')