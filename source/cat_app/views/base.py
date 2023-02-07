from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect

cat = []


def index_view(request: WSGIRequest):
    return render(request, 'index.html',
                  context={'name': request.GET.get("name"),
                           'age': request.GET.get("age"),
                           'happiness': request.GET.get("happiness"),
                           'satiety': request.GET.get("satiety")})


def cat_view(request: WSGIRequest):
    context = {'name': request.GET.get("name"),
               'age': request.GET.get("age", 1),
               'happiness': request.GET.get("happiness", 25),
               'satiety': request.GET.get("satiety", 30)}
    cat.append(context)
    return render(request, 'cat.html', context=context)


def feed_cat():
    if int(cat[0]['satiety']) >= 100:
        number = int(cat[0]['happiness']) - 30
        updated_happiness(number)
    else:
        number_2 = int(cat[0]['satiety']) + 15
        number = int(cat[0]['happiness']) + 5
        updated_happiness(number)
        updated_satiety(number_2)
    return redirect(f'/cat/?name={cat[0]["name"]}&age={cat[0]["age"]}&satiety={cat[0]["satiety"]}&happiness={cat[0]["happiness"]}')


def play_cat():
    number = int(cat[0]['happiness']) + 15
    number_2 = int(cat[0]['satiety']) - 5
    updated_happiness(number)
    updated_satiety(number_2)
    return redirect(f'/cat/?name={cat[0]["name"]}&age={cat[0]["age"]}&satiety={cat[0]["satiety"]}&happiness={cat[0]["happiness"]}')


def sleep_cat():
    number = int(cat[0]['happiness']) - 15
    number_2 = int(cat[0]['satiety']) - 15
    updated_happiness(number)
    updated_satiety(number_2)
    return redirect(f'/cat/?name={cat[0]["name"]}&age={cat[0]["age"]}&satiety={cat[0]["satiety"]}&happiness={cat[0]["happiness"]}')


def updated_happiness(one):
    cat[0].update({'happiness': one})


def updated_satiety(two):
    cat[0].update({'satiety': two})

