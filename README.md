# Application Web de Gestion de Tâches

> **Développeurs** : Erkin Tunc BOYA, Mohamed SAIDANE 
> **Technologies** : Python Django, Bootstrap

---

## Description

C'est une application web multi-utilisateur permettant la gestion de tâches.  
L'application est construite avec Django et utilise Bootstrap pour le style.

---

## Comment démarrer

1. **Cloner le projet**
```bash
git clone <repo-url>
cd App-Web-Gestion-De-taches
```

2. **Créer un environnement virtuel**  
Chaque ordinateur doit avoir son propre environnement virtuel (non partagé via Git).
```bash
python -m venv tp-env
```

3. **Activer l’environnement virtuel**
```bash
# UNIX
source tp-env/bin/activate
# Windows
tp-env\Scripts\activate
```

4. **Installer les dépendances**
```bash
# Installer Django
python -m pip install Django
# Installer les dépendances (ex : pour la gestion d’images)
pip install -r requirements.txt
```

5. **Lancer le serveur**
```bash
python manage.py runserver
```

---

## Fonctionnalités

- **Authentification** : chaque utilisateur doit se connecter ou s’inscrire pour accéder au site.

### Fonctionnalités des Tâches

- Une tâche comporte un titre, un statut, une description, une liste de sous-tâches, une liste de personnes et une liste d'équipes associées.
- Une tâche peut être privée (visible uniquement par les personnes/équipes associées) ou publique.
- L'utilisateur peut créer, modifier et supprimer une tâche.
- Lorsqu'une tâche est supprimée, tous ses liens avec les équipes et les personnes sont automatiquement supprimés.

### Fonctionnalités des Équipes

- Une équipe a un nom et une liste de personnes.
- Un utilisateur peut créer, modifier, quitter et supprimer une équipe.
- Lorsqu'une équipe est supprimée, tous ses liens avec les tâches et les personnes sont automatiquement supprimés.

### Fonctionnalités des Utilisateurs

- Un utilisateur a un nom, un e-mail, une description, un mot de passe et une image.
- Un utilisateur peut consulter le profil d’un autre utilisateur/équipe, ainsi que les tâches publiques qui lui sont attribuées.
- Lorsqu’un utilisateur est supprimé, toutes ses relations avec les tâches et les équipes sont automatiquement supprimées.

---

## Modèles (Entities)

### Task
```json
{
  "private": boolean,
  "creator": User,

  "title": string,
  "status": "todo" || "in_progress" || "done",
  "description": string,

  "assigned_users": [User],
  "assigned_teams": [Team],
  "sub_tasks": [Task],

  "created_at": Date,
  "updated_at": Date, 
  "deadline": Date
}
```

### Team
```json
{
  "name": string,
  "users": [User]
}
```

### User
Classe utilisateur par défaut :
```json
{
  "id": int,
  "name": string,
  "email": string,
  "password": string
}
```

### UserProfile
```json
{
  "user": User, // Relation un-à-un
  "description": string,
  "image": *.png // Dossier "pictures"
}
```

---

## Routes API

### Page d’accueil
- `GET /` – Affiche toutes les tâches

### Authentification
- `POST /register` – Créer un compte
- `POST /login` – Se connecter
- `POST /logout` – Se déconnecter

### Utilisateur
- `GET /users/:id` – Voir le profil d’un utilisateur, ses tâches et ses équipes
- `POST /users/add/` – Créer un utilisateur
- `PUT /users/update/:id` – Mettre à jour le profil
- `DELETE /users/delete/:id` – Supprimer un utilisateur

### Équipe
- `GET /teams/:id` – Voir le profil d’une équipe
- `POST /teams/add` – Créer une équipe
- `PUT /teams/update/:id` – Mettre à jour une équipe
- `DELETE /teams/delete/:id` – Supprimer une équipe
- `POST /teams/:id/join` – Rejoindre une équipe
- `POST /teams/:id/leave` – Quitter une équipe

### Tâche
- `GET /tasks/:id` – Voir une tâche
- `POST /tasks/add` – Créer une tâche
- `PUT /tasks/update/:id` – Mettre à jour une tâche
- `DELETE /tasks/delete/:id` – Supprimer une tâche

- `POST /tasks/:id/assign/user/:userId` – Assigner un utilisateur à une tâche
- `POST /tasks/:id/unassign/user/:userId` – Retirer un utilisateur d’une tâche

- `POST /tasks/:id/assign/team/:teamId` – Assigner une équipe
- `POST /tasks/:id/unassign/team/:teamId` – Retirer une équipe
