from django.shortcuts import render
from.models import *
# Create your views here.
def project(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    context = {"products": products, "categories": categories}
    return render(request, "project.html", context)


def contact(request):
    if request.method =="POST":
        first_name = request.POST["firstName"]
        last_name = request.POST["lastName"]
        email = request.POST["emailName"]
        comment = request.POST["commentName"]
        Contact(contact_name = first_name,
        contact_lastname = last_name,
        contact_email = email,
        contact_comment = comment).save()
    return render(request, "contact.html")

def about(request):
    categories = Category.objects.all()
    context = {"categories": categories}
    return render(request, "about.html")

def Terms(request):
    return render(request, "Terms.html")

def detail(request, id):
    detailItem = Product.objects.get(pk = id)
    context = {"detailItem": detailItem}
    return render(request, "detail.html", context)

def category(request,id):
    categories = Category.objects.all()
    cat = Category.objects.get(pk = id)
    productsCategory = Product.objects.filter(product_category = cat)
    context = {"categories": categories, "cat": cat, "productsCategory" : productsCategory}
    return render(request, "category.html", context)


   

