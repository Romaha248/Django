from django import forms

from .models import Review

# class ReviewForm(forms.Form):
#     username = forms.CharField(label="Your Name", max_length=15, error_messages={
#         "required": "Your name must not be empty",
#         "max_length": "Pls enter shorter name",
#     })
#     review = forms.CharField(label="Your Feedback", widget=forms.Textarea, max_length=200)
#     rating = forms.IntegerField(label="Your rating", min_value=1, max_value=5)

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        # fields = ["username", "review", "rating"]
        fields = "__all__"
        # exclude = ["rating"]
        labels = {
            "username": "Your Name",
            "review": "Feedback",
            "rating": "Your Rating",
        }
        error_messages = {
            "username":{
                "required": "Your name must not be empty",
                "max_length": "Pls enter shorter name",
            }
        }
