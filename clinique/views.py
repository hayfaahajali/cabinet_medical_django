from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Medecin, Patient, RendezVous
from .forms import MedecinForm, PatientForm, RendezVousForm

# ─── Accueil ───────────────────────────────────────────
@login_required
def accueil(request):
    derniers_rdv = RendezVous.objects.order_by('-id')[:5]  # ou '-date' selon votre modèle
    return render(request, 'clinique/accueil.html', {
        'nb_medecins': Medecin.objects.count(),
        'nb_patients': Patient.objects.count(),
        'nb_rdv': RendezVous.objects.count(),
        'derniers_rdv': derniers_rdv,
    })

# ─── CRUD Médecin ───────────────────────────────────────
@login_required
def liste_medecins(request):
    query = request.GET.get('q', '')
    medecins = Medecin.objects.filter(
        nom__icontains=query
    ) | Medecin.objects.filter(
        prenom__icontains=query
    ) | Medecin.objects.filter(
        specialite__icontains=query
    )
    return render(request, 'clinique/liste_medecins.html', {
        'medecins': medecins,
        'query': query
    })

@login_required
def ajouter_medecin(request):
    form = MedecinForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_medecins')
    return render(request, 'clinique/form_medecin.html', {'form': form, 'titre': 'Ajouter un Médecin'})
@login_required
def modifier_medecin(request, pk):
    medecin = get_object_or_404(Medecin, pk=pk)
    form = MedecinForm(request.POST or None, instance=medecin)
    if form.is_valid():
        form.save()
        return redirect('liste_medecins')
    return render(request, 'clinique/form_medecin.html', {'form': form, 'titre': 'Modifier un Médecin'})
@login_required
def supprimer_medecin(request, pk):
    medecin = get_object_or_404(Medecin, pk=pk)
    if request.method == 'POST':
        medecin.delete()
        return redirect('liste_medecins')
    return render(request, 'clinique/confirmer_suppression.html', {'objet': medecin, 'type': 'médecin'})

# ─── CRUD Patient ───────────────────────────────────────
@login_required
def liste_patients(request):
    query = request.GET.get('q', '')
    patients = Patient.objects.filter(
        nom__icontains=query
    ) | Patient.objects.filter(
        prenom__icontains=query
    ) | Patient.objects.filter(
        telephone__icontains=query
    )
    return render(request, 'clinique/liste_patients.html', {
        'patients': patients,
        'query': query
    })

@login_required
def ajouter_patient(request):
    form = PatientForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_patients')
    return render(request, 'clinique/form_patient.html', {'form': form, 'titre': 'Ajouter un Patient'})

@login_required
def modifier_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    form = PatientForm(request.POST or None, instance=patient)
    if form.is_valid():
        form.save()
        return redirect('liste_patients')
    return render(request, 'clinique/form_patient.html', {'form': form, 'titre': 'Modifier un Patient'})

@login_required
def supprimer_patient(request, pk):
    patient = get_object_or_404(Patient, pk=pk)
    if request.method == 'POST':
        patient.delete()
        return redirect('liste_patients')
    return render(request, 'clinique/confirmer_suppression.html', {'objet': patient, 'type': 'patient'})

# ─── CRUD Rendez-vous ───────────────────────────────────
@login_required
def liste_rendezvous(request):
    query = request.GET.get('q', '')
    rendezvous = RendezVous.objects.filter(
        patient__nom__icontains=query
    ) | RendezVous.objects.filter(
        patient__prenom__icontains=query
    ) | RendezVous.objects.filter(
        medecin__nom__icontains=query
    )
    return render(request, 'clinique/liste_rendezvous.html', {
        'rendezvous': rendezvous,
        'query': query
    })

@login_required
def ajouter_rendezvous(request):
    form = RendezVousForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('liste_rendezvous')
    return render(request, 'clinique/form_rendezvous.html', {'form': form, 'titre': 'Ajouter un Rendez-vous'})

@login_required
def modifier_rendezvous(request, pk):
    rdv = get_object_or_404(RendezVous, pk=pk)
    form = RendezVousForm(request.POST or None, instance=rdv)
    if form.is_valid():
        form.save()
        return redirect('liste_rendezvous')
    return render(request, 'clinique/form_rendezvous.html', {'form': form, 'titre': 'Modifier un Rendez-vous'})

@login_required
def supprimer_rendezvous(request, pk):
    rdv = get_object_or_404(RendezVous, pk=pk)
    if request.method == 'POST':
        rdv.delete()
        return redirect('liste_rendezvous')
    return render(request, 'clinique/confirmer_suppression.html', {'objet': rdv, 'type': 'rendez-vous'})