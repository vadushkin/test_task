import json

from django.shortcuts import render, redirect
from slugify import slugify

from .models import News
from .models import Tag


def index(requests):
    return render(requests, 'admin_panel/admin_index.html', context={'title': 'Главная'})


def add_products(requests):
    with open('admin_panel/jsons/output_ozon.json', 'r') as file:
        text = json.load(file)
        for i in text:
            n = News.objects.create(name=i['title'], description=i['url'], created_at=i['date'])
            for j in i['theme']:
                if not Tag.objects.filter(name=j['name']):
                    Tag.objects.create(name=j['name'], slug=slugify(j['name']))
                n.tags.add(Tag.objects.filter(name=j['name']).values().last()['id'])
    with open('admin_panel/jsons/output_yandex.json', 'r') as file:
        text = json.load(file)
        for i in text:
            n = News.objects.create(name=i['title'], description=i['url'], created_at=i['date'])
            for j in i['tags']:
                if not Tag.objects.filter(name=j[1:]):
                    Tag.objects.create(name=j[1:], slug=slugify(j[1:]))
                n.tags.add(Tag.objects.filter(name=j[1:]).values().last()['id'])
    return redirect('home')
