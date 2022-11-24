from django.urls import path
from . import old_views, views

# app_name = "book"
# urlpatterns = [
    # path("", views.greet),
    # path("", views.index, name="index"),
    # path("<int:pk>/", views.publisher_details, name="publisher-details"),
    # path("books/", views.book_list, name= "book-book-list"),
    # path("book-create/", views.book_create, name="book-create")
# ]
urlpatterns = [
   path("books/", views.book_list, name="book-list")
]