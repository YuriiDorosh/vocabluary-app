from django.contrib import admin
from src.apps.words.models import Word, WordTranslation


class WordTranslationInline(admin.TabularInline):
    """
    Displays the WordTranslation model in an inline form under Word.
    You could also use `admin.StackedInline` if you prefer a stacked layout.
    """
    model = WordTranslation
    extra = 1  # Number of empty inline forms to display


@admin.register(Word)
class WordAdmin(admin.ModelAdmin):
    """
    Customize how the Word model is displayed in the admin.
    """
    list_display = ("word", "owner", "created_at", "updated_at")
    search_fields = ("word", "definition", "owner__username")
    list_filter = ("owner",)
    
    # You can add your WordTranslation inline so you can edit translations
    # directly on the Word admin page
    inlines = [WordTranslationInline]


@admin.register(WordTranslation)
class WordTranslationAdmin(admin.ModelAdmin):
    """
    Separate admin page for WordTranslation (if you want to manage translations
    independently as well).
    """
    list_display = ("word", "translation_text", "language", "created_at", "updated_at")
    list_filter = ("language",)
    search_fields = ("translation_text", "word__word")
