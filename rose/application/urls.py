from django.urls import path
from . import views
urlpatterns = [
    path("", views.project, name="projectPage"),
    path("contact/", views.contact, name="contactPage"),
    path("about/", views.about, name="aboutPage"),
    path("terms/", views.Terms, name="termsPage"),
    path("detail/<int:id>", views.detail, name="detailPage"),
    path("category/<int:id>", views.category, name="categoryPage")
]