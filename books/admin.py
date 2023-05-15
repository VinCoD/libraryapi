from django.contrib import admin
from .models import Book

# Register your models here.

class BookAdmin(admin.ModelAdmin):
  # This class inherits from the admin.ModelAdmin class.

  list_display = (
    "title",
    "subtitle",
    "author",
    "isbn"
  )
  # This attribute specifies the fields that will be displayed in the list view for the Todo model.

admin.site.register(Book, BookAdmin)

