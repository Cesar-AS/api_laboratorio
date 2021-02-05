from django.db import models
from uuid import uuid4
# Create your models here.

def upload_exame_paciente(instance, filename):
    return f"(instance.id_patient)-(filename)"

class Pacientes(models.Model):
    id_paciente = models.UUIDField(primary_key=True, default=uuid4, editable=False)
    nome = models.CharField(max_length=255, null=True)
    nasc = models.DateField(null=True)
    cpf = models.CharField(max_length=20, null=True)
    end = models.CharField(max_length=255, null=True)
    cep = models.CharField(max_length=20, null=True)
    bairro = models.CharField(max_length=255, null=True)
    cidade = models.CharField(max_length=50, null=True)
    uf = models.CharField(max_length=50, null=True)
    tel = models.CharField(max_length=20, null=True)
    #exam = models.ImageField(upload_to=upload_patient_exam, blank=True, null=True