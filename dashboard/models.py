from django.db import models

class Produto(models.Model):
    nome = models.CharField(max_length=100)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()

    def __str__(self):
        return self.nome

class Vendedor(models.Model):
    nome = models.CharField(max_length=100)


    def __str__(self):
        return self.nome

class Venda(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    quantidade = models.IntegerField()
    data_venda = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Venda de {self.produto.nome} por {self.vendedor.nome}"