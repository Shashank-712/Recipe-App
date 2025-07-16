from django.db import models
from django.contrib.auth.models import User
from django.db.models import Avg

class Recipe(models.Model):
    DIFFICULTY_CHOICES = [
        ('easy', 'Easy'),
        ('medium', 'Medium'), 
        ('hard', 'Hard'),
    ]

    CATEGORY_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
        ('snack', 'Snack'),
        ('dessert', 'Dessert'),
    ]
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    prep_time = models.PositiveIntegerField(help_text="Prep time in minutes") 
    cook_time = models.PositiveIntegerField(help_text="Cook time in minutes")
    servings = models.PositiveIntegerField()
    difficulty = models.CharField(
        max_length=10,
        choices=DIFFICULTY_CHOICES,
        default='medium'
    )
    category = models.CharField(
        max_length=20,
        choices=CATEGORY_CHOICES,
        default='lunch'
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    @property
    def average_rating(self):
        ratings = self.ratings.all()
        if ratings:
            return round(sum(r.rating for r in ratings) / len(ratings), 1)
        return 0


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='ingredients')
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.quantity} of {self.name}"

class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='instructions')
    step_number = models.PositiveIntegerField()
    text = models.TextField()

    class Meta:
        ordering = ['step_number']

    def __str__(self):
        return f"Step {self.step_number}"

from django.db import models
from django.contrib.auth.models import User

class RecipeRating(models.Model):
    recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, related_name='ratings')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ['recipe', 'user']  # Each user can rate a recipe only once

    def __str__(self):
        return f"{self.user.username} rated {self.recipe.title} as {self.rating}"

    @property
    def average_rating(self):
        return self.ratings.aggregate(Avg('rating'))['rating__avg']
    

