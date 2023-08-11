from django.urls import path
from books import views

urlpatterns = [
    path("", views.IndexPageView.as_view(), name="index-page"),
    path("category/<int:pk>", views.CategoryDetailView.as_view(), name="category-detail"),
    path("authors/", views.AuthorListView.as_view(), name="authors-list"),
    path("authors/<int:pk>", views.AuthorDetailView.as_view(), name="author-detail"),
    path("search/", views.search, name="search"),
]