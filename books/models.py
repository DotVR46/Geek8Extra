from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=300, verbose_name="Имя автора")
    description = models.TextField(verbose_name="Краткая биография", blank=True)
    photo = models.ImageField(
        upload_to="authors/photos",
        verbose_name="Фото автора",
        blank=True,
        default="authors/default.jpg",
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Category(models.Model):
    name = models.CharField(max_length=50, verbose_name="Название категории")
    description = models.TextField(verbose_name="Описание", blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Book(models.Model):
    name = models.CharField(max_length=200, verbose_name="Название книги")
    description = models.TextField(verbose_name="Описание", blank=True)
    price = models.IntegerField(verbose_name="Цена")
    cover = models.ImageField(
        upload_to="books/covers",
        verbose_name="Обложка",
        blank=True,
        default="books/default.jpg",
    )
    category = models.ManyToManyField(Category, related_name="book_category", verbose_name="Категория")
    author = models.ManyToManyField(Author, related_name="book_author", verbose_name="Автор")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"
