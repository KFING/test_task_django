from django.forms import ModelForm, TextInput, Textarea

class TaskForm(ModelForm):
    class Meta:
        fields = ["email","password"]
        widgets = {"email": TextInput(attrs={
            'class':'form-control',
            'placeholder': 'input name'
        }),
            "password": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'input text'
            })
        }