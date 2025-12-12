# main.py
import os
from github import Auth, Github
from review_generator import ai_reviewer

# Variables de entorno
git_token = os.getenv("g_token")
git_repository = os.getenv('g_repository')
git_pr_number = os.getenv('g_pr_number')

# Configuración de la IA
base_url = os.getenv('base_url', "")
api_key = os.getenv('api_key')
model = os.getenv('model')
temperature = float(os.getenv('temperature', 0.7))
tokens = int(os.getenv('tokens', 1500))

if not git_token:
    raise RuntimeError("Falta el token de autenticación en el entorno")

if not api_key:
    raise RuntimeError("Falta la clave API de la IA")

def git_authentication(token):
    """Autentica con GitHub usando token"""
    try:
        auth = Auth.Token(token)
        g = Github(auth=auth)
        print(f"Autenticación exitosa en GitHub")
        return g
    except Exception as e:
        raise RuntimeError(f"Error al autenticarse en Github: {e}")

def get_pr(g, repository, pr_number):
    """Obtiene el Pull Request especificado"""
    try:
        repo = g.get_repo(repository)
        pr = repo.get_pull(int(pr_number))
        print(f"PR #{pr_number} obtenido: '{pr.title}'")
        return pr
    except Exception as e:
        raise RuntimeError(f"Error al obtener PR: {e}")
    
def get_diff_content(pr):
    """Extrae el contenido diff de todos los archivos del PR"""
    files = pr.get_files()

    if files.totalCount == 0:
        print("No hay archivos modificados en este PR")
        return None

    diff_content = ""
    print(f"Procesando {files.totalCount} archivo(s)...")

    excluded_ext = ['txt', 'md', 'json', 'png', 'jpg', 'jpeg', 'svg', 'gif', 
                'lock', 'pdf', 'zip', 'ico']

    for file in files:
        """Filtrar archivos que no queremos revisar"""
        extension = file.filename.split('.')[-1].lower()

        if extension not in excluded_ext:
            diff_content += f"\n--- {file.filename} ---\n"
            diff_content += f"{file.patch}\n"
        else:
            print(f"Archivo omitido (extensión {extension}): {file.filename}")

    """Verifica si no hay ningun archivo para revisar"""
    if not diff_content.strip():
        print("Todos los archivos fueron filtrados - no hay código para revisar")
        return None
    
    return diff_content

def create_comment(pr, model, review_content):
    """Crea un comentario en el PR con el resultado de la revisión del código"""
    if not review_content:
        print("No hay contenido para comentar")
        return None
    
    comment_body = f"""### Revisión Automática de Código

{review_content}

---
*Revisión generada por IA usando **{model}***
"""

    try:
        comment = pr.create_issue_comment(comment_body)
        print("Comentario publicado exitosamente en el PR")
        return comment
    except Exception as e:
        print(f"Error al publicar comentario: {e}")

def main():
    # Autenticación en Github
    g = git_authentication(git_token)

    # Obtiene el PR actual
    pr = get_pr(g, git_repository, git_pr_number)

    # Extrae el contenido diff del PR
    diff_content = get_diff_content(pr)

    if not diff_content:
        return None

    # Iniciación de OpenAI
    ai = ai_reviewer(api_key, model, temperature, tokens, base_url)

    # Respuesta de la IA
    result = ai.review_code(diff_content)
    if result:
        create_comment(pr, model, result)

if __name__ == "__main__":
    main()