# 🔍 AI Code Review for GitHub Pull Requests
Este proyecto es una **aplicación desarrollada en Python** que utiliza **GitHub Actions** y **Inteligencia Artificial** para **analizar automáticamente el código dentro de un Pull Request** y **generar un informe de análisis de calidad, buenas prácticas y posibles mejoras.**

## 🚀 ¿Qué hace este proyecto?
Cuando se crea o actualiza un Pull Request en un repositorio de GitHub:

1. Se ejecuta una **GitHub Action** automáticamente.
2. El **código** **modificado** en el **Pull** **Request** es **analizado**.
3. Se envía el contenido a un modelo de **IA (por ejemplo, OpenAI).**
4. La IA genera un **análisis detallado del código**, incluyendo:

    - Calidad del código
    
    - Buenas prácticas
    
    - Posibles errores o mejoras
    
    - Legibilidad y mantenibilidad

5. El resultado se **publica** directamente **en el Pull Request** como comentario o reporte.

## 💡 Flexibilidad en el uso de IA
La aplicación es compatible con **distintos proveedores de IA** (OpenAI, Groq, DeepSeek, etc.), lo que permite utilizar **modelos con planes gratuitos o de bajo coste**, simplemente ajustando la configuración del workflow.

## 🧠 Tecnologías utilizadas
- **Python**
- **GitHub Actions**
- **API de OpenAI**
- **GitHub REST API**
- **Inteligencia Artificial aplicada a revisión de código**

## 🎯 Objetivo del proyecto

El objetivo principal es **automatizar la revisión de código**, ayudando a los equipos de desarrollo a:

- Reducir tiempo en revisiones manuales
- Mantener estándares de calidad
- Detectar problemas de forma temprana
- Facilitar feedback claro y estructurado

## ⚙️ Requisitos
### <u>Requisitos técnicos</u>
- Repositorio en GitHub
- Python 3.11 o superior
- Cuenta en un proveedor de IA compatible (OpenAI, Groq, etc.)
### <u>Variables de entorno</u>
Configurada como **Secrets en GitHub:**
- ```OPENAI_TOKEN``` o token del proveedor de IA

## 🧪 Cómo probar el proyecto
Para probar el funcionamiento, es necesario contar con un repositorio en GitHub.
<br>El usuario debe clonar el siguiente repositorio base:

```
git clone https://github.com/MarioSFdez/ai-code-reviewer.git
```

Alternativamente, se pueden copiar directamente los archivos necesarios dentro de un repositorio propio.

### 📁 Paso 1: Copiar los archivos al repositorio destino
En el repositorio donde se desea habilitar la revisión automática, se deben copiar los siguientes archivos:
- [main.py](main.py)
- [review_generator.py](review_generator.py)
- [requirements.txt](requirements.txt)
- [.github/workflows/review.yml](.github/workflows/review.yml)

### 🔐 Paso 2: Configurar los Secrets en GitHub
En el repositorio destino:
  1. Ir a **Settings** → **Secrets and variables** → **Actions**
  2. Agregar el siguiente **Repository** **Secret**:

``OPENAI_TOKEN``: Token del proveedor de IA (OpenAI, Groq, DeepSeek, etc.)



El ``GITHUB_TOKEN`` es proporcionado automáticamente por GitHub y no requiere configuración manual

<img width="1178" height="213" alt="Captura de pantalla 2025-12-18 004057" src="https://github.com/user-attachments/assets/df54642b-2b71-43b3-bfb8-2b2155cc731a" />

### ⚙️ Paso 3: Configurar el proveedor de IA
Dentro del archivo .github/workflows/review.yml, el usuario puede modificar el proveedor y el modelo de IA utilizado.

**Ejemplo usando OpenAI**
```
env:
  model: gpt-4o-mini
  temperature: 0.5
  tokens: 2000
```
**Ejemplo usando DeepSeek**
```
env:
  base_url: https://api.deepseek.com/openai/v1
  model: deepseek-chat
  temperature: 0.5
  tokens: 2000
```
**Ejemplo usando Groq**
```
env:
  base_url: https://api.groq.com/openai/v1
  model: llama-3.3-70b-versatile
  temperature: 0.5
  tokens: 2000  
```
> [!NOTE]
> El proyecto permite utilizar cualquier proveedor compatible con la API de OpenAI, simplemente cambiando la base_url y el model

### 🔁 Paso 4: Crear un Pull Request
Una vez configurado el proyecto:
1. Crear una nueva rama
2. Realizar cambios de código
3. Abrir un Pull Request hacia la rama ``main``

El workflow se ejecutará automáticamente y publicará el análisis en el Pull Request.

<img width="1195" height="616" alt="image" src="https://github.com/user-attachments/assets/d055c436-e2a9-4ca3-a24b-3bbdee72b54d" />
<img width="1103" height="809" alt="Captura de pantalla 2025-12-18 011659" src="https://github.com/user-attachments/assets/2d73b089-7268-4d8f-8ad3-7db1098272c7" />

### 🧩 Alternativa: Fork del repositorio
Como alternativa, los usuarios pueden:
1. Hacer fork del repositorio
2. Configurar los Secrets
3. Usar el proyecto directamente sin copiar archivos

## Ejemplo de comentario PR
👉 [**URL**](https://github.com/MarioSFdez/ai-code-reviewer/pull/1)
<img width="1176" height="460" alt="image" src="https://github.com/user-attachments/assets/d689d064-9888-4aa1-bf0e-398514ba8a7c" />

## 🧠 Conclusión
Este proyecto demuestra cómo la Inteligencia Artificial puede
integrarse de forma práctica y eficiente dentro del ciclo de
desarrollo de software, automatizando tareas repetitivas y
mejorando la calidad del código sin interrumpir el flujo de trabajo
del equipo.

## Autor
| [<img src="https://avatars.githubusercontent.com/u/140948023?s=400&u=f1aaaefb0cd2fe5f6be92fba05411a79d3a92878&v=4" width=115><br><sub>Mario Sierra Fernández</sub>](https://github.com/MarioSFdez) |
| :---: | 
