from django.db import models

class GamesModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, help_text='Título do jogo')
    platforms = models.CharField(max_length=100, help_text='Plataformas suportadas')
    description = models.TextField(max_length=500, help_text='Descrição do jogo')
    release_date = models.DateField(help_text='Data de lançamento')
    developer = models.CharField(max_length=100, help_text='Desenvolvedora do jogo')