from django.db import models
from django.contrib.auth.models import User

class Review(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, help_text='Usuário que criou a avaliação')
    title = models.CharField(max_length=100, help_text='Título do jogo')
    rating = models.IntegerField(help_text='Nota de 1 a 10')
    comment = models.TextField(max_length=500, help_text='Comentário sobre o jogo')
    created_at = models.DateTimeField(auto_now_add=True, help_text='Data de criação')

    def __str__(self):
        return f"{self.title} ({self.rating}) - {self.user.username}"
