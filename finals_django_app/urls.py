# myapp/urls.py
from django.urls import path
from .views import BookListView, BookDetailView, AuthorListView, PublisherListView, ReaderListView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book_list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book_detail'),
    path('authors/', AuthorListView.as_view(), name='author_list'),
    path('publishers/', PublisherListView.as_view(), name='publisher_list'),
    path('readers/', ReaderListView.as_view(), name='reader_list'),
]


# projectname/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('myapp/', include('myapp.urls')),
]
