# chess-python

Jeu d'échecs en Python avec interface graphique, développé dans le cadre d'un projet personnel d'apprentissage.

## Objectifs du projet

- Apprendre la programmation orientée objet en Python
- Transposer mes bases acquises en C# (POO) vers Python
- Découvrir Pygame pour la visualisation graphique

## Technologies utilisées

- Python 3.13
- Pygame 2.6.1

## Lancer le projet

### Prérequis

- Python 3.13
- Git

### Installation

```bash
git clone https://github.com/houssam-ben-othman/chess-python.git
cd chess-python
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

### Lancement

```bash
python main.py
```

## Structure du projet
```
chess-python/
├── main.py        # Point d'entrée
├── game.py        # Logique de la partie
├── board.py       # Gestion du plateau
├── piece.py       # Classes des pièces
├── player.py      # Gestion des joueurs
└── ui.py          # Interface graphique Pygame
```

## Statut

🚧 En cours de développement