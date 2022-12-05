from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.mixins import ListModelMixin

from .filter import BookFilter
from .models import Book, Publisher
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.viewsets import ModelViewSet
from .serializers import BookSerializer, PublisherSerializer
from rest_framework.filters import SearchFilter, OrderingFilter


class BookViewSet(ModelViewSet):
    queryset = Book.objects.select_related('publisher').all()
    serializer_class = BookSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_class = BookFilter
    search_fields = ['title']
    ordering_fields = ['title']
    #filterset_fields = ['title']

class PublisherViewSet(ModelViewSet):
    queryset = Publisher.objects.annotate(number_of_books_published=Count('books')).all()
    serializer_class = PublisherSerializer




# class BookList(ListCreateAPIView):
#     queryset = Book.objects.select_related('publisher').all()
#     serializer_class = BookSerializer


# class BookDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# class PublisherList(ListCreateAPIView):
#     queryset = Publisher.objects.annotate(number_of_books_published=Count('books')).all()
#     serializer_class = PublisherSerializer
#
#
# class PublisherDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Publisher.objects.annotate(number_of_books_published=Count('books')).all()
#     serializer_class = PublisherSerializer


#     def get(self, request):
#         queryset = Book.objects.select_related('publisher').all()
#         serializer = BookSerializer(queryset, many=True, context={"request": request})
#         return Response(serializer.data)
#
#     def post(self, request):
#         serializer = BookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
#
#
#
#
# @api_view(['GET', 'POST'])  # noqa
# def book_list(request):
#     if request.method == 'GET':
#         queryset = Book.objects.select_related('publisher').all()
#         serializer = BookSerializer(queryset, many=True, context={"request": request})
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         # if serializer.is_valid():
#         #     print(serializer.validated_data)
#         #     return Response("I can post")
#         # else:
#         #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
# class BookDetail(APIView):
#     def get(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         serializer = BookSerializer(book, context={"request": request})
#         return Response(serializer.data)
#     def patch(self,request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         serializer = BookSerializer(book, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     def delete(self, request, pk):
#         book = get_object_or_404(Book, pk=pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
#
#
# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def book_detail(request, pk):  # noqa
#     book = get_object_or_404(Book, pk=pk)
#     if request.method == 'GET':
#
#         serializer = BookSerializer(book, context={"request": request})
#         return Response(serializer.data)
#     elif request.method in ('PUT', 'PATCH'):
#         serializer = BookSerializer(book, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET', 'POST'])
# def publisher_list(request):
#     if request.method == 'GET':
#         queryset = Publisher.objects.annotate(number_of_books_published=Count('books')).all()
#         serializer = PublisherSerializer(queryset, many=True, context={"request": request})
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = PublisherSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(['GET', 'PUT', 'PATCH', 'DELETE'])
# def publisher_detail(request, pk):
#     queryset = Publisher.objects.annotate(number_of_books_published=Count('books')).all()
#     publisher = get_object_or_404(queryset, pk=pk)
#     if request.method == 'GET':
#         serializer = PublisherSerializer(publisher, context={"request": request})
#         return Response(serializer.data)
#     elif request.method in ('PUT', 'PATCH'):
#         serializer = PublisherSerializer(publisher, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'DELETE':
#         publisher.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
