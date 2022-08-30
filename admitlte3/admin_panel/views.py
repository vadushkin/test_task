from django.shortcuts import render


def index(requests):
    return render(requests, 'admin_panel/index.html', context={'title': 'Главная'})
