from django.db import models

PATENTE_CHOICES = (
    ('S2', 'Soldado de 2ª Classe'),
    ('S1', 'Soldado de 1ª Classe'),
    ('CB', 'Cabo'),
    ('3S', '3º Sargento'),
    ('2S', '2º Sargento'),
    ('1S', '1º Sargento'),
    ('SO', 'Sub-Oficial'),
    ('AP', 'Aspirante'),
    ('2T', '2º Tenente'),
    ('1T', '1º Tenente'),
    ('CP', 'Capitão'),
    ('MJ', 'Major'),
    ('TC', 'Tenente-Coronel'),
    ('CL', 'Coronel'),
    ('BR', 'Brigadeiro'),
    ('MB', 'Major-Brigadeiro'),
    ('TB', 'Tenente-Brigadeiro'),
    ('CV', 'Civil'),
    )

PROJETO_CHOICES = (
    ('FABDOC', 'FABDOC'),
    ('SPCOA', 'SPCOA'),
    ('SAGEM', 'SAGEM'),
    ('C2/CENTRAL', 'C2/CENTRAL'),
    ('C2/DEA2', 'C2/DEA2'),
    ('C2/HERCULES 2', 'C2/HERCULES 2'),
    ('IFFM4BR', 'IFFM4BR'),
    ('SIMULADOR T27', 'SIMULADOR T27'),
    ('A29 RV', 'A29 RV'),
)

class Feedback(models.Model):
    nome = models.CharField(max_length=30)
    patente = models.CharField(max_length=2, choices= PATENTE_CHOICES)
    email = models.EmailField(max_length=50)
    contato = models.CharField(max_length=11)
    projeto = models.CharField(max_length=13,choices = PROJETO_CHOICES)
    feedback = models.TextField(max_length=500)

def __str__(self):
    return self.nome
# Create your models here.
