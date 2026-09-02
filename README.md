# 420-C74-SF — Techniques d'apprentissage automatique

Ateliers (travaux pratiques) du cours **420-C74-SF**, programme *Spécialiste en solutions d'intelligence artificielle*.

## Organisation du dépôt

| Répertoire | Contenu |
|---|---|
| `nbs/` | Ateliers, un répertoire par chapitre (énoncé + version `-solution`) |
| `data/` | Jeux de données, référencés depuis les notebooks par `../../data/` |
| `evals/` | Évaluations, examens et projets |
| `materials/` | Diapositives des chapitres (PDF) |
| `docker/` | Image de l'environnement de travail |
| `.devcontainer/` | Configuration Dev Container (VS Code) |

## Chapitres et ateliers

| # | Chapitre | Atelier |
|---|---|---|
| 01 | Introduction à l'apprentissage automatique | — |
| 02 | Régression linéaire simple | `nbs/02-regression-lineaire-simple/` |
| 03 | Algorithme du gradient | `nbs/03-algorithme-gradient/` |
| 04 | Régression linéaire multiple et polynomiale | `nbs/04-regression-lineaire-multiple/` |
| 05 | Équation normale | `nbs/05-equation-normale/` |
| 06 | Métriques et évaluation des modèles de régression | `nbs/06-metriques/` |
| 07 | Régression logistique | `nbs/07-regression-logistique/` |
| 08 | Dilemme biais-variance | `nbs/08-dilemme-biais-variance/` *(à venir)* |
| 09 | Validation croisée | `nbs/09-validation-croisee/` |
| 10 | Techniques de régularisation | `nbs/10-regularisation/` |
| 11 | Introduction à scikit-learn | `nbs/11-intro-scikit-learn/` *(à venir)* |
| 12 | Algorithme des K plus proches voisins | `nbs/12-algorithme-knn/` |
| 13 | Arbres de décision | `nbs/13-arbres-de-decision/` |
| 14 | Bagging, forêts aléatoires et boosting | `nbs/14-bagging-forets-aleatoires-boosting/` |
| 15 | Machines à vecteurs de support | `nbs/15-svm/` |
| 16 | Métriques et évaluation des modèles de classification | `nbs/16-evaluation-models-classification/` |
| 17 | Optimisation des hyperparamètres | `nbs/17-optimisation-des-hyperparametres-101/` |
| 18 | Apprentissage ensembliste | `nbs/18-ensembles/` |
| 19 | Introduction au partitionnement de données | — |
| 20 | Partitionnement en K-moyennes | `nbs/20-partitionnement-k-moyennes/` |
| 21 | Regroupement hiérarchique | `nbs/21-regroupement-hierarchique/` |
| 22 | Validation du partitionnement | `nbs/22-validation-partitionnement/` |
| 23 | DBSCAN et HDBSCAN | `nbs/23-dbscan/` |
| 24 | Considérations pratiques sur le partitionnement | — |
| 25 | Méthodes de partitionnement avancées | — |
| 26 | Partitionnement : exemples d'application | — |
| 27 | Analyse en composantes principales | — |
| 28 | t-SNE | — |
| 29 | Algorithme des plus proches voisins | `nbs/29-recherche-documents/` |
| 30 | Métriques de distance | — |
| 31 | Locality-Sensitive Hashing | `nbs/31-locality-sensitive-hashing/` |
| 32 | Algorithme Apriori et règles d'association | `nbs/32-regles-association/` |
| 33 | Détection d'anomalies | — |
| 34 | Modèles de mélange (Gaussian Mixture Models) | — |

## Environnement de travail

Python 3.13 ; les versions des bibliothèques sont épinglées dans
[docker/requirements.txt](docker/requirements.txt).

### Avec VS Code (recommandé)

Ouvrir le dépôt dans VS Code, puis **Reopen in Container** : le Dev Container construit l'image
et installe les extensions Python / Jupyter.

### Avec Docker seul

Depuis la racine du dépôt :

```bash
docker build -t 420-c74-sf docker/
docker run --rm -it -p 8888:8888 -v $(pwd):/notebooks 420-c74-sf
```

Puis ouvrir http://localhost:8888. Voir [docker/README.md](docker/README.md) pour les détails.
