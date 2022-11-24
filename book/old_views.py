# from django.http import HttpResponse
# from django.shortcuts import render, get_object_or_404
# from .models import Publisher, Book
# from django.db.models import *
# from .form import BookForm
#
#
# # Create your views here.
# # def greet(request):
# #     return HttpResponse("Hello world")
#
#
# def index(request):
#     queryset = Publisher.objects.all().filter(website__startswith="https")
#     return render(request, "book/index.html", context={"publishers": list(queryset)})
#
#
# def publisher_details(request, pk):
#     publisher = get_object_or_404(Publisher, pk=pk)
#     return render(request, "book/publisher-details.html", context={"publisher": publisher})
#
#
# def book_list(request):
#     queryset = Book.objects.select_related('publisher').all()
#     result = queryset.aggregate(count=Count('id'), average=Avg('price'))
#     return render(request, "book/book-list.html", context={"books": list(queryset), "result": result})
#
#
# def book_create(request):
#     if request.method == 'GET':
#         form = BookForm()
#         return render(request, "book/book-create.html", context={"form": form})
#     elif request.method == 'POST':
#         print(request.POST)
#         form = BookForm(request.POST)
#         if form.is_valid():
#             print(form.cleaned_data)
#             form.save()
#         return render(request, "book/book-create.html", context={"form": form})
