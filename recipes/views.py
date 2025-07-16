# Add below your existing DRF API views

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from .models import Recipe
from .forms import RecipeForm  # ✅ Make sure this file exists

# UI Views
def recipe_list(request):
    category = request.GET.get('category')
    search_query = request.GET.get('search')
    
    recipes = Recipe.objects.all()

    if category:
        recipes = recipes.filter(category=category)

    if search_query:
        recipes = recipes.filter(
            Q(title__icontains=search_query) | Q(description__icontains=search_query)
        )

    return render(request, 'recipes/recipe_list.html', {
        'recipes': recipes,
        'selected_category': category,
        'search_query': search_query,
    })



from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import Recipe
from .serializers import RecipeSerializer

class RecipeListCreateView(generics.ListCreateAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

class RecipeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]


@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe-list-ui')
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'recipes/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('recipe-list-ui')
    else:
        form = AuthenticationForm()
    return render(request, 'recipes/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login')

from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm  # Make sure you have this!

@login_required
def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.author != request.user:
        return redirect('recipe-list-ui')

    if request.method == 'POST':
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            form.save()
            return redirect('recipe-list-ui')
    else:
        form = RecipeForm(instance=recipe)
    
    return render(request, 'recipes/recipe_form.html', {'form': form})

@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if recipe.author == request.user:
        recipe.delete()
    return redirect('recipe-list-ui')

from .forms import RatingForm
from .models import RecipeRating

@login_required
def rate_recipe(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    rating_instance, created = RecipeRating.objects.get_or_create(recipe=recipe, user=request.user)

    if request.method == 'POST':
        form = RatingForm(request.POST, instance=rating_instance)
        if form.is_valid():
            form.save()
            return redirect('recipe-list-ui')
    else:
        form = RatingForm(instance=rating_instance)

    return render(request, 'recipes/rate_recipe.html', {'form': form, 'recipe': recipe})


