from django.db import models

# Create your models here.
class time(models.Model):
    equipe = models.CharField(max_length=50)
    fundacao = models.DateField()
    mascote = models.CharField(max_length=30, default='Nenhum')
    rebaixamento = models.CharField(max_length=5, default='Nenhum')
    principal_titulo = models.CharField(max_length=100, default='Nenhum')
    maior_idolo = models.CharField(max_length=100, default='Nenhum')
    treinador = models.CharField(max_length=50, default='Nenhum')
    def __str__(self):
        return f"{self.equipe}"

class jogador(models.Model):
    POSICAO = (
        ('G', 'Goleiro'),
        ('D', 'Defensor'),
        ('M', 'Meio Campo'),
        ('A', 'Atacante')
    )

    nome_jogador = models.CharField(max_length=50)
    data_nascimento = models.DateField()
    posicao = models.CharField(max_length=1, choices=POSICAO, blank=False, null=False, default='A')
    time_jogador = models.ForeignKey(time, on_delete=models.CASCADE, null=False, blank=False)
    def __str__(self):
        return f"{self.nome_jogador}"

class campeonato (models.Model):
    nome_campeonato = models.CharField(max_length=50)
    edicao = models.CharField(max_length=5, default='1')
    campeao = models.OneToOneField(time, on_delete=models.CASCADE, null=True, blank=True)
    artilheiro = models.OneToOneField(jogador, on_delete=models.CASCADE, null=True, blank=True)
    def __str__(self):
        return f"{self.nome_campeonato}"

