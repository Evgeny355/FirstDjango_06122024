from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

from MainApp.models import Item
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.

author = {
    "Имя": "Евгений",
    "Отчество": "Вячеславович",
    "Фамилия": "Трушков",
    "телефон": "8-800-600-50-40",
    "email": "vasya@mail.ru"
}


# items = [
#    {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
#    {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
#    {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
#    {"id": 7, "name": "Картофель фри" ,"quantity":0},
#    {"id": 8, "name": "Кепка" ,"quantity":124},
# ]


def home(request):
    # text = """
    # <h1>"Изучаем django"</h1>
    # <strong>Автор</strong>: <i>Иванов И.П.</i>
    # """
    # return HttpResponse(text)
    context = {
        "name": "Петров Иван Николаевич",
        "email": "eto_ego_pochta@mail.ru"
    }
    return render(request, "index.html", context)

def about(request):
    author = {
    "name": "Евгений",
    "middle_name": "Вячеславович",
    "last_name": "Трушков",
    "phone": "8-800-600-50-40",
    "email": "vasya@mail.ru"
}
    return render(request, "about_list.html", {"author": author})

def get_item(request, item_id: int):
    """ По указанному id возвращаем имя элемента"""
    # for item in items:
    #     if item['id'] == item_id:
    #         result = f"""
    #         <h2> Имя: {item["name"]} </h2>
    #         <p> Количество: {item["quantity"]} </p>
    #         <p> <a href="/items"> Назад к списку товаров </p>
    #         """
    #         return HttpResponse(result)
    # return HttpResponseNotFound(f"Item with id={item_id} not found")

    # item = next((item for item in items if item['id'] == item_id), None)
    """ По указанному ID возвращаем элемент из БД """
    try:
        item = Item.objects.get(id=item_id)
    except ObjectDoesNotExist:
        return HttpResponseNotFound(f"Item with id={item_id} not found")
    # if item is not None:
    else:
        context = {
              "item": item
        }
        return render(request, "item_page.html", context)
    

def get_items(request):
    # result = "<h1> Список товаров </h1><ol>"
    # for item in items:
    #     result += f"""<li><a href="/item/{item['id']}"> {item['name']} </li> """
    # result += "</ol>"
    # return HttpResponse(result)
    items = Item.objects.all()
    context = {
        "items": items
    }
    return render(request, "items_list.html", context)