from django.urls import path
from .views import rate_recipe
from .views import (
    RecipeListCreateView, RecipeDetailView,
    recipe_list, recipe_create, recipe_edit, recipe_delete,
    register_view, login_view, logout_view,
)

urlpatterns = [
    # API endpoints
    path('recipes/', RecipeListCreateView.as_view(), name='recipe-list'),
    path('recipes/<int:pk>/', RecipeDetailView.as_view(), name='recipe-detail'),

    # UI pages
    path('ui/recipes/', recipe_list, name='recipe-list-ui'),
    path('ui/recipes/create/', recipe_create, name='recipe-create'),
    path('ui/recipes/<int:pk>/edit/', recipe_edit, name='recipe-edit'),
    path('ui/recipes/<int:pk>/delete/', recipe_delete, name='recipe-delete'),


    # Auth
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),

    path('ui/recipes/<int:pk>/rate/', rate_recipe, name='recipe-rate-ui'),
]

