# 🏥 Cabinet Médical — Application Django

> Application web de gestion d'une polyclinique développée avec Django dans le cadre du module **Programmation Python Avancée** — AU 25-26 Semestre 2.

---

## 📋 Description

Cette application permet à une secrétaire de gérer les médecins, les patients et les rendez-vous d'une polyclinique depuis une interface web sécurisée et intuitive.

---

## 🚀 Fonctionnalités

### ✅ Obligatoires
- CRUD complet pour les **Médecins**
- CRUD complet pour les **Patients**
- CRUD complet pour les **Rendez-vous**
- Base de données **SQLite3**
- Architecture **MVT** (Modèle - Vue - Template)
- Environnement virtuel **venv**
- Interface avec **templates Django**

### 🌟 Bonus
- 🔐 Système d'authentification (login/logout)
- 🔗 Relations entre tables (Médecin ↔ Patient via Rendez-vous)
- 🔍 Recherche dans les 3 listes
- 🎨 Interface Bootstrap responsive
- 🏠 Page d'accueil avec tableau de bord

---

## 🗄️ Modèles de données

### Médecin
| Champ | Type |
|---|---|
| nom | CharField |
| prenom | CharField |
| specialite | CharField |
| telephone | CharField |
| email | EmailField |

### Patient
| Champ | Type |
|---|---|
| nom | CharField |
| prenom | CharField |
| date_naissance | DateField |
| telephone | CharField |
| email | EmailField |
| antecedents | TextField |

### Rendez-vous
| Champ | Type |
|---|---|
| medecin | ForeignKey → Médecin |
| patient | ForeignKey → Patient |
| date | DateField |
| heure | TimeField |
| motif | TextField |
| statut | CharField (planifié/confirmé/annulé) |

---

## ⚙️ Installation et lancement

### 1. Cloner le projet
```bash
git clone https://github.com/hayfaahajali/cabinet_medical_django.git
cd cabinet_medical_django
```

### 2. Créer et activer l'environnement virtuel
```bash
python -m venv env
env\Scripts\activate        # Windows
source env/bin/activate     # Mac/Linux
```

### 3. Installer les dépendances
```bash
pip install django
```

### 4. Appliquer les migrations
```bash
python manage.py migrate
```

### 5. Créer un superutilisateur
```bash
python manage.py createsuperuser
```

### 6. Lancer le serveur
```bash
python manage.py runserver
```

### 7. Accéder à l'application
http://127.0.0.1:8000

---

## 🛠️ Technologies utilisées

| Technologie | Version |
|---|---|
| Python | 3.12.9 |
| Django | 6.0.4 |
| Bootstrap | 5.3.0 |
| Font Awesome | 6.4.0 |
| SQLite3 | intégré |

---

## 👩‍💻 Auteur

- **Nom :** Haj ali haifa
- **Niveau :** 3ème année Informatique
- **Module :** Programmation Python Avancée
- **Enseignante :** Dr. Sghaier Amra