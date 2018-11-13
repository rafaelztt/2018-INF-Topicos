from django.db import models

# Create your models here.
# Todas as classes extendem a classe models.Model
class Cidade(models.Model):
    # nome_do_atributo = tipoDele(características)
    nome = models.CharField(max_length=50)
    estado = models.CharField(max_length=2, help_text='Informe apenas a sigla')
    
    # apenas para imprimir o objeto conforme abaixo
    def __str__(self):
        # Paranavaí (PR)
        return self.nome + ' (' + self.estado + ')'

class Pessoa(models.Model):
    nome = models.CharField(max_length=50, help_text='Nome completo')
    email = models.CharField(max_length=50)
    nascimento = models.DateField('Data de Nascimento')
    # Chave estrangeira deve informar a Classe e a relação ao excluir
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)

    def __str__(self):
        # Faz um cast da data para string
        return self.nome + ' - ' + str(self.nascimento)
