from django import forms
from .models import Quiz,Image


# creating a form
class QuizForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Quiz

        # specify fields to be used
        fields = [
            "name",
        ]

class ImageForm(forms.ModelForm):
    # create meta class
    class Meta:
        # specify model to be used
        model = Image

        # specify fields to be used
        fields = [
            "answer","organism","question","cellType","component","description","doi","mode","name"
        ]