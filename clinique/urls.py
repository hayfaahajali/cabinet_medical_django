from django.urls import path
from . import views

urlpatterns = [
    # Page d'accueil
    path('', views.accueil, name='accueil'),

    # CRUD Médecin
    path('medecins/', views.liste_medecins, name='liste_medecins'),
    path('medecins/ajouter/', views.ajouter_medecin, name='ajouter_medecin'),
    path('medecins/modifier/<int:pk>/', views.modifier_medecin, name='modifier_medecin'),
    path('medecins/supprimer/<int:pk>/', views.supprimer_medecin, name='supprimer_medecin'),

    # CRUD Patient
    path('patients/', views.liste_patients, name='liste_patients'),
    path('patients/ajouter/', views.ajouter_patient, name='ajouter_patient'),
    path('patients/modifier/<int:pk>/', views.modifier_patient, name='modifier_patient'),
    path('patients/supprimer/<int:pk>/', views.supprimer_patient, name='supprimer_patient'),

    # CRUD Rendez-vous
    path('rendezvous/', views.liste_rendezvous, name='liste_rendezvous'),
    path('rendezvous/ajouter/', views.ajouter_rendezvous, name='ajouter_rendezvous'),
    path('rendezvous/modifier/<int:pk>/', views.modifier_rendezvous, name='modifier_rendezvous'),
    path('rendezvous/supprimer/<int:pk>/', views.supprimer_rendezvous, name='supprimer_rendezvous'),
]