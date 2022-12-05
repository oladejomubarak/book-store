from django.urls import path, include
from . import old_views, views
from rest_framework.routers import SimpleRouter, DefaultRouter

app_name = "book"
# urlpatterns = [
    # path("", views.greet),
    # path("", views.index, name="index"),
    # path("<int:pk>/", views.publisher_details, name="publisher-details"),
    # path("books/", views.book_list, name= "book-book-list"),
    # path("book-create/", views.book_create, name="book-create")
# ]
router = DefaultRouter() #SimpleRouter()
router.register('books', viewset=views.BookViewSet, basename='book')
router.register('publishers', viewset=views.PublisherViewSet, basename='publisher')
print(router.urls)
urlpatterns = [
   # path("books/", views.BookList.as_view(), name="book-list"),
   # path("books/<int:pk>/", views.BookDetail.as_view(), name="book-detail"),
   path("", include(router.urls)),
   # path("publishers/", views.PublisherList.as_view(), name="publisher-list"),
   # path("publishers/<int:pk>", views.PublisherDetail.as_view(), name="publisher-detail"),

]