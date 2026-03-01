from .models import Category

def categories_processors(request):
    categories = Category.objects.all()
    return {'categories': categories}