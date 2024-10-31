from django import forms
from .models import Dish

class DishForm(forms.ModelForm):
    class Meta:
        model = Dish
        fields = ['dish_name', 'description', 'notes', 'food_image_url', 'food_image_file', 'price']

    def clean(self):
        cleaned_data = super().clean()
        food_image_url = cleaned_data.get("food_image_url")
        food_image_file = cleaned_data.get("food_image_file")

        if not food_image_url and not food_image_file:
            raise forms.ValidationError("You must provide either a URL or a file for the food image.")
        if food_image_url and food_image_file:
            raise forms.ValidationError("You can only provide one of URL or file for the food image.")
        return cleaned_data