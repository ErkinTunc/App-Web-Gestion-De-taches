# Application Web de Gestion-De-taches

> **Developeurs** : Erkin Tunc BOYA , Muhammed
> **Techonlogies** : python Django, Bootstrap

---

## Description
C'est une application web multi-utilisateur qui nous permet de faire gestion de tache. Application est constuit avec Django et fait le styliing avec Bootstrap.

--- 

## Comment Démarrer(How to run)
1. **Clone the project**
```bash
git clone <repo-url>
cd App-Web-Gestion-De-taches
```

2. **Installer Environment Virtual**
Dans chaque ordinateur il faut l'installer on ne peut pas mettre sur le git car venv configure juste pour votre pc.
```bash
python -m venv tp-env
```

4. **Ouvrir le Environment Virtuelle**
```bash
# UNIX
source tp-env/bin/activate
# Windows
tp-env\Scripts\activate
```
3. **Installer dependencies**
```bash
# Install Django
python -m pip install Django
# Pour Django (une pour les images)
pip install -r requirements.txt
```


4. **Run the server**
```bash
# Django
python manage.py runserver
```

---

## Fonctionalité

-  Authentification : tous le monde doivent faire une login ou register pour entrer dans la site.

####  Fonctionalite des Tache(Task)
- Une tâche comporte un titre, un statut , une description une liste de sous-taches, une liste de personnes et une liste d'equipes rattachés.
- Une tâche peut être privée : visible seulement par les personnes/équipes qui ont y été associes; ou publique
- Utilisateur peut créer,modifier et supprimer une tache.
- Quand un tache est supprimé tous ses relations avec des equipes et des personnes vont couper automatiqument.

####  Fonctionalite des Equipe(Team)
- Une équipe a un nom, liste de personne
- Une personne peut créer, modifier, quitter et supprimer une equipe 
- Quand un equipe est supprimé tous ses relations avec des taches et des personnes vont couper automatiqument.

#### Fonctionalite des Personne(User)
- Une personne a un Nom, un email, une description ,un mot de passe, une image
- Une personne peut voir le profil d'une autre personne/équipe ainsi que les tâches publiques qui lui ont été assignées.
- Quand un Personne est supprimé tous ses relations avec des taches et des equipes vont couper automatiqument.

---

## Les entités(Models) 

### Task
```json
{
  "private": boolean,
  "creator": User,

  "title": string,
  "status": "todo" | "in_progress" | "done",
  "description": String,
  
  "assigned_users": [User],
  "assigned_teams": [Team],
  "sub_tasks": [Task],

  "created_at" : Date,
  "updated_at" : Date, 
  "deadline" : Date,
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
C'est class est une classe default
```json
{
  "id": int,
  "name": string,
  "email": string,
  "password": string,
}
```

### UserProfile

```json
{
  "user" : User, // Relation one to one 

  "description": string,
  "image": *.png // Dans le dossier "pictures"
}
```

---

## API URI
- `GET /` – Page d'acceuil , il y a tous les taches

### Auth
- `POST /register` – Crée personne
- `POST /login` – Authenticate
- `POST /logout` – Finir session

### User
- `GET /users/:id` – profile d'une personne , il y a aussi ses taches et ses equipes
- `POST /users/add/` - crée une personne
- `PUT /users/update/:id` - mise a jour le profile de personne
- `DELETE /users/delete/:id` - supprimer la personne


### Team
- `GET /teams/:id` – profile d'une tache
- `POST /teams/add` – Create equipe
- `PUT /teams/update/:id` - mise a jour le profile de equipe
- `DELETE /teams/delete/:id` - supprimer la equipe

- `POST /teams/:id/join` – Join
- `POST /teams/:id/leave` – Leave

### Task
- `GET /tasks/:id` – profile d'une tache
- `POST /tasks/add` – Create equipe
- `PUT /tasks/update/:id` - mise a jour le profile de equipe
- `DELETE /tasks/delete/:id` - supprimer la equipe

- `POST /tasks/:id/assign/user/:userId` – Assign user
- `POST /tasks/:id/unassign/user/:userId` – Unassign user

- `POST /tasks/:id/assign/team/:teamId` – Assign team adds one of your teams
- `POST /tasks/:id/unassign/team/:teamId` – Unassign team
