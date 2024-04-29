from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    slug = models.SlugField()

    class Meta:
        ordering = ('nome',)

    def __str__(self):
        return self.nome
    
class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, related_name='produtos', on_delete=models.CASCADE)
    nome = models.CharField(max_length=255)
    slug = models.SlugField()
    descricao = models.TextField(blank=True, null=True) #not obligatory
    preco = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True) #automatic

    class Meta:
        ordering = ('-created_at',)

    def __str__(self):
        return self.nome
    
    def get_preco_formatado(self):
        return f'R${self.preco:.2f}'
    