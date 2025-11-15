# app.py
import os
from github import Auth, Github

pat_token = os.getenv("PAT_TOKEN")

if not pat_token:
    raise RuntimeError("Falta token de autenticación en el entorno") 

# Autenticación en Github
auth = Auth.Token(pat_token)
g = Github(auth=auth)

# Cerrar sesión
g.close()