from django.shortcuts import render
from django.views import generic
from books.models import Book, Category, Author


def search(request):
    if request.method == "POST":
        query = request.POST.get("search")
        books = Book.objects.filter(name__icontains=query)
        authors = Author.objects.filter(name__icontains=query)
        return render(request, "books/search.html",
                      {"books": books, "authors": authors, "categories": Category.objects.all()})


class IndexPageView(generic.ListView):
    queryset = Book.objects.all()[0:10]
    context_object_name = "books"
    extra_context = {"categories": Category.objects.all()}
    template_name = "books/index.html"


class CategoryDetailView(generic.DetailView):
    model = Category
    context_object_name = "category"
    extra_context = {"categories": Category.objects.all()}
    template_name = "books/category.html"


class AuthorListView(generic.ListView):
    model = Author
    context_object_name = "authors"
    template_name = "books/authors_list.html"
    extra_context = {"categories": Category.objects.all()}


class AuthorDetailView(generic.DetailView):
    model = Author
    context_object_name = "author"
    template_name = "books/author_detail.html"
    extra_context = {"categories": Category.objects.all()}
