# review_generator.py
import openai
from openai import OpenAI

class ai_reviewer:
    """Clase para manejar revisiones de código utilizando IA"""
    def __init__(self, api_key, model, temperature, tokens, base_url):
        self.api_key = api_key
        self.model = model
        self.temperature = temperature
        self.tokens = tokens
        self.base_url = base_url

        self.client = self._client()

    def _client(self):
        """Inicializa el cliente de OpenAI"""
        try:
            if self.base_url:
                client = OpenAI(base_url=self.base_url, api_key=self.api_key)
                return client
            else:
                client = OpenAI(api_key=self.api_key)
                return client
        except Exception as e:
            raise RuntimeError(f"Error al inicializar el cliente de IA: {e}")

    def build_prompt(self, diff_content):
        """Construcción del Prompt para la IA"""
        if not diff_content:
            print("Diff vacío, no se puede revisar")
            return None

        prompt=f"""Analiza el siguiente Pull Request y proporciona:
    1. **Resumen general**: Qué hace este cambio en 2-3 líneas
    2. **Aspectos positivos**: Qué está bien hecho
    3. **Sugerencias de mejora**: Problemas potenciales, bugs, malas prácticas, o mejoras de rendimiento
    4. **Seguridad**: Posibles vulnerabilidades
    5. **Recomendaciones**: Cambios específicos con ejemplos de código si es necesario

    Sé constructivo, específico y proporciona ejemplos cuando sea posible.

            DIFF DEL PULL REQUEST:

            {diff_content}
            """
        return prompt

    def review_code(self, prompt_content):
        """Genera una revisión del código utilizando IA"""

        if not prompt_content:
            print("No hay contenido para revisar")
            return None

        prompt = self.build_prompt(prompt_content)

        try:   
            completion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        'role': 'system', 'content': 'Eres un experto revisor de codigo'
                    },
                    {
                        'role' : 'user', 'content' : prompt
                    }
                ],
                temperature=self.temperature,
                max_completion_tokens=self.tokens
            )

            result = completion.choices[0].message.content

            if not result:
                print("La IA no devolvió una respuesta")
                return None
            
            return result
        
        except openai.AuthenticationError as e:
            print(f"Falló al intentar autenticarse a través de OpenAI API: {e}")
            return None
        except openai.APIError as e:
            print(f"La API de OpenAI devolvió el siguiente error: {e}")
            return None
        except openai.APIConnectionError as e:
            print(f"Falló al conectar a OpenAI API: {e}")
            return None
        except openai.RateLimitError as e:
            print(f"Excedió el limite de solicitudes a OpenAI API: {e}")
            return None