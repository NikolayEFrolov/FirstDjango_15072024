from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
author = {
    "Имя" : "Nik",
    "Фамилия" : "Фролов",
    "Отчество" : "Евгеньевич",
    "телефон": "+7 (917) 828 2232"
     "Email"  "frolov@bk.ru"
}



def home(requiest):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Иванов И.П.</i>
    """
    return HttpResponse(text)

def about(request):
    text = f"""
    Имя : {author["Имя"]}
    Фамилия : {author["Фамилия"]}
    "Отчество" : {author["Отчество"]}
    "телефон": {author["телефон"]}
     "Email": {author["Email"]}
    """