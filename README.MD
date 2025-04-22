# 🧠 RemodelUN - Préparation MUN Automatisée avec CrewAI

RemodelUN est un projet Python propulsé par [CrewAI](https://www.crewai.com) visant à **automatiser la préparation des participants à un MUN (Model United Nations)**.  
Il collecte des documents pertinents sur le sujet, génère une *cheat sheet* et synthétise la position du pays représenté.

---

## 🎯 Objectifs

✅ Rechercher automatiquement des documents fiables sur un sujet MUN  
✅ Générer une fiche de synthèse claire et structurée (*cheat sheet*)  
✅ Résumer la position officielle d’un pays sur le sujet  
✅ Utiliser des agents IA spécialisés (via LLM) pour guider les participants

---

## 📁 Structure du projet

```
remodelun/
├── config/
│   ├── agents.yaml           # Configuration des agents CrewAI
│   └── tasks.yaml            # Configuration des tâches CrewAI
├── tools/
│   └── web_research_tool.py  # Outil personnalisé pour la recherche web
├── outputs/                  # Contient les fichiers générés (cheat sheet, position)
├── mun_crew.py               # Déclaration de la Crew CrewAI
├── main.py                   # Script principal d'exécution
├── requirements.txt          # Dépendances Python
└── .env                      # Variables d’environnement (clé OpenAI)
```

---

## ⚙️ Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/ton-utilisateur/remodelun.git
cd remodelun
```

### 2. Créer un environnement virtuel (optionnel mais recommandé)

```bash
python -m venv .venv
source .venv/bin/activate     # Linux/macOS
.venv\Scripts\activate        # Windows
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Ajouter ta clé OpenAI

Créer un fichier `.env` à la racine avec :

```
OPENAI_API_KEY=sk-votre_clé_personnelle_ici
```

> 🔐 Tu peux obtenir une clé depuis [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)

---

## 🚀 Utilisation

Lance le script principal :

```bash
python main.py
```

Tu seras invité à saisir :
- Le sujet du débat (ex : `La piraterie en mer Rouge`)
- Le pays représenté (ex : `Somalie`)

Les résultats seront générés dans le dossier `outputs/` :
- `research_sources.md` : ressources clés trouvées
- `cheat_sheet.md` : fiche de synthèse thématique
- `position_summary.md` : position officielle du pays

---

## 🛠️ Options avancées

Le fichier `main.py` inclut aussi :

### Entraînement simulé :
```bash
python main.py train <n_iterations> <nom_fichier_sortie>
```

### Rejeu d'une tâche spécifique :
```bash
python main.py replay <task_id>
```

### Test du comportement du crew :
```bash
python main.py test <n_iterations> <nom_modèle_openai>
```

---

## 🧩 Extensions possibles

- Ajouter un outil de scraping automatique via `SerpAPI` ou `NewsAPI`
- Intégration avec Google Docs ou Notion pour distribuer les fiches
- Ajout d’un rôle “Présidence” pour simuler les angles de modération

---

## 🤝 Contributeurs

Projet créé par **Ben**, passionné de MUN et d’IA appliquée à la diplomatie étudiante.  
Tu veux contribuer ? Ouvre une *pull request* ou contacte-moi !

---

## 📄 Licence

Ce projet est sous licence MIT — voir le fichier `LICENSE` pour plus de détails.

---

## 🧽 Fichier `.gitignore` recommandé

```
.venv/
__pycache__/
outputs/
.env
*.pyc
*.log
*.sqlite3
.idea/
.DS_Store
```

---

## 📝 Licence MIT

```
MIT License

Copyright (c) 2025

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
of the Software, and to permit persons to whom the Software is furnished to do
so, subject to the following conditions:

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
```
```

---

Souhaites-tu que je t’envoie aussi ce fichier prêt à télécharger (`README.md`) ?