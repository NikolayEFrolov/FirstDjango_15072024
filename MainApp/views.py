from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
author = {
    "Имя" : "Николай",
    "Фамилия" : "Фролов",
    "Отчество" : "Евгеньевич",
    "телефон": "+7 (917) 828 2232",
     "Email" : "frolov@bk.ru"
}



def home(requiest):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Иванов И.П.</i>
    """
    return HttpResponse(text)

def about(request):
    text = f"""
    Имя : {author["Имя"]}<br>
    Фамилия : {author["Фамилия"]}<br>
    Отчество : {author["Отчество"]}<br>
    телефон: {author["телефон"]}<br>
    Email: {author["Email"]}<br>
    """
    return HttpResponse(text)