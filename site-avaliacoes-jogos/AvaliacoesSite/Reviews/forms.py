from .models import Review
from django import forms

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'rating', 'comment']
        labels = {
            'title': 'Título do Jogo/Filme',
            'rating': 'Nota (1 a 10)',
            'comment': 'Comentário',
        }
        help_texts = {
            'title': 'Informe o título do jogo ou filme.',
            'rating': 'Escolha uma nota de 1 a 10.',
            'comment': 'Escreva um comentário sobre o jogo/filme (máx. 500 caracteres).',
        }
        error_messages = {
            'title': {'max_length': 'O título é muito longo.', 'required': 'O título é obrigatório.'},
            'rating': {'required': 'A nota é obrigatória.'},
            'comment': {'max_length': 'O comentário é muito longo.', 'required': 'O comentário é obrigatório.'},
        }

    def clean_title(self):
        """Custom validation to ensure title is valid."""
        title = self.cleaned_data.get('title')
        
        if not title:
            raise forms.ValidationError("O título é obrigatório.")
        if len(title) < 3:
            raise forms.ValidationError("O título deve ter pelo menos 3 caracteres.")
        
        return title
    
    def clean_rating(self):
        """Custom validation to ensure rating is between 1 and 10."""
        rating = self.cleaned_data.get('rating')
        
        print(f"########## Rating is {rating} ##############")

        if rating is None:
            raise forms.ValidationError("A nota é obrigatória.")
        if rating < 1 or rating > 10:
            raise forms.ValidationError("A nota deve ser um número inteiro entre 1 e 10.")
        
        return rating

    def clean_comment(self):
        """Custom validation to ensure comment is valid."""
        comment = self.cleaned_data.get('comment')
        
        if not comment:
            raise forms.ValidationError("O comentário é obrigatório.")
        if len(comment) < 10:
            raise forms.ValidationError("O comentário deve ter pelo menos 10 caracteres.")
        if len(comment) > 500:
            raise forms.ValidationError("O comentário não pode exceder 500 caracteres.")
        
        return comment