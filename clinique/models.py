from django.db import models

class Medecin(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    specialite = models.CharField(max_length=100)
    telephone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"Dr. {self.prenom} {self.nom} - {self.specialite}"


class Patient(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    date_naissance = models.DateField()
    telephone = models.CharField(max_length=20)
    email = models.EmailField(unique=True)
    antecedents = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.prenom} {self.nom}"


class RendezVous(models.Model):
    STATUS_CHOICES = [
        ('planifie', 'Planifié'),
        ('confirme', 'Confirmé'),
        ('annule', 'Annulé'),
    ]
    medecin = models.ForeignKey(Medecin, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date = models.DateField()
    heure = models.TimeField()
    motif = models.TextField()
    statut = models.CharField(max_length=20, choices=STATUS_CHOICES, default='planifie')

    def __str__(self):
        return f"RDV - {self.patient} avec {self.medecin} le {self.date}"