# Configuration du serveur Jupyter (jupyter-server 2 / Notebook 7 / JupyterLab 4)
#
# Note: les anciens réglages `c.NotebookApp.*` du Notebook classique ne sont plus
# lus depuis Notebook 7 ; ils sont remplacés par leurs équivalents `c.ServerApp.*`.

# Écoute sur toutes les interfaces du conteneur (accès depuis l'hôte)
c.ServerApp.ip = "0.0.0.0"
c.ServerApp.port = 8888

# Répertoire de travail (monté depuis l'hôte, voir docker/README.md)
c.ServerApp.root_dir = "/notebooks"

# Pas de navigateur dans le conteneur
c.ServerApp.open_browser = False

# Le conteneur tourne en root
c.ServerApp.allow_root = True

# Environnement de cours local: ni jeton ni mot de passe
c.ServerApp.token = ""
c.ServerApp.password = ""
c.ServerApp.password_required = False
c.ServerApp.allow_remote_access = True
c.IdentityProvider.token = ""
