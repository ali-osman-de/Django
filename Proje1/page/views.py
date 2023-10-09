from django.shortcuts import render
from django.http import HttpResponse
from random import randint

# Create your views here.

FK_DB = [
    f"https://picsum.photos/id/{id}/100/100" for id in range(21,32)
]

FK_DB_CAROUSEL = [
    f"https://picsum.photos/id/{id}/1600/300" for id in range(96,100)
]

def home_view(request):
    # print(request.META)
    # randomNunmber = f"Randint sayımız: {randint(0,1000)}"
    # context = {"platform" : "Django Platformu Kullanıldı!" + randomNunmber}
    page_title = "Anasayfa"
    hero_content = """
                    Swap the background-color utility and add a `.text-*` color utility to mix up
                    the jumbotron look.
                    Then, mix and match with additional component themes and more."""
    context = dict(
        page_title=page_title,
        hero_content=hero_content,
        FK_DB=FK_DB,
        FK_DB_CAROUSEL=FK_DB_CAROUSEL,
        
    )
    return render(request, "page/home_page.html", context)

def about_us_view(request):
    page_title = "Hakkımızda"
    hero_content = """
                    Swap the background-color utility and add a `.text-*` color utility to mix up
                    the jumbotron look.
                    Then, mix and match with additional component themes and more."""
    context = dict(
        page_title=page_title,
        hero_content=hero_content,

    )
    return render(request, "page/about_us.html", context)

def contact_us_view(request):
    page_title = "İletişim"
    hero_content = """
                    Swap the background-color utility and add a `.text-*` color utility to mix up
                    the jumbotron look.
                    Then, mix and match with additional component themes and more."""
    context = dict(
        page_title=page_title,
        hero_content=hero_content,

    )
    return render(request, "page/contact_us.html", context)

