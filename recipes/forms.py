from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'description', 'prep_time', 'cook_time', 'servings', 'difficulty']

from django import forms
from .models import RecipeRating

class RatingForm(forms.ModelForm):
    class Meta:
        model = RecipeRating
        fields = ['rating']
        widgets = {
            'rating': forms.Select(choices=[(i, i) for i in range(1, 6)])
        }



