import os
import openai

class AIHelper:
    def __init__(self):
        """Inicializa o helper da IA usando Azure OpenAI ou OpenAI padrão."""
        # Azure OpenAI
        self.azure_api_key = os.getenv('AZURE_OPENAI_KEY')
        self.azure_endpoint = os.getenv('AZURE_OPENAI_ENDPOINT')
        self.azure_deployment = os.getenv('AZURE_OPENAI_DEPLOYMENT')
        self.azure_api_version = os.getenv('AZURE_OPENAI_API_VERSION', '2024-02-15-preview')
        # OpenAI padrão (fallback)
        self.api_key = os.getenv('OPENAI_API_KEY')
        if not (self.azure_api_key and self.azure_endpoint and self.azure_deployment):
            if not self.api_key or self.api_key == 'sua_chave_aqui':
                print('⚠️  ATENÇÃO: Chave da OpenAI/Azure OpenAI não configurada!')
                print('📝 Configure sua chave no arquivo .env para usar a IA')
        # Exercícios de relaxamento
        self.exercises = {
            'respiracao': {
                'name': 'Exercício de Respiração 4-7-8',
                'instructions': [
                    '1. Sente-se confortavelmente com as costas retas',
                    '2. Expire completamente pela boca',
                    '3. Inspire pelo nariz contando até 4',
                    '4. Segure a respiração contando até 7',
                    '5. Expire pela boca contando até 8',
                    '6. Repita este ciclo 4 vezes'
                ],
                'duration': '3-5 minutos'
            },
            'relaxamento_progressivo': {
                'name': 'Relaxamento Muscular Progressivo',
                'instructions': [
                    '1. Deite-se ou sente-se confortavelmente',
                    '2. Tensione os músculos dos pés por 5 segundos, depois relaxe',
                    '3. Suba gradualmente: panturrilhas, coxas, abdômen',
                    '4. Continue com braços, ombros, pescoço e rosto',
                    '5. Sinta a diferença entre tensão e relaxamento',
                    '6. Mantenha todo o corpo relaxado por 2 minutos'
                ],
                'duration': '10-15 minutos'
            },
            'visualizacao': {
                'name': 'Visualização Positiva',
                'instructions': [
                    '1. Feche os olhos e respire profundamente',
                    '2. Imagine-se entrando na sala de prova calmo e confiante',
                    '3. Visualize-se lendo as questões com clareza',
                    '4. Veja-se respondendo com segurança e conhecimento',
                    '5. Imagine a sensação de completar a prova com sucesso',
                    '6. Mantenha essa imagem positiva por alguns minutos'
                ],
                'duration': '5-10 minutos'
            }
        }

    def process_message(self, user_message, conversation, current_phase):
        """Processa a mensagem do usuário e retorna resposta da IA via Azure OpenAI ou OpenAI padrão, priorizando clareza, concisão e evitando repetições."""
        # Prioriza Azure OpenAI se configurado
        system_prompt = (
            "Você é uma IA que acalma estudantes antes de provas. "
            "Responda de forma humana, acolhedora, empática e confiante, como um amigo experiente. "
            "Adapte o tom conforme a emoção do estudante, demonstre compreensão e apoio real. "
            "Use frases naturais, linguagem simples, positiva e motivadora. "
            "Seja claro, mas não excessivamente curto. Mostre interesse genuíno pelo bem-estar do estudante. "
            "Quando o usuário pedir ajuda para se acalmar, sugira exercícios práticos em tópicos, como respiração 4-7-8, relaxamento muscular progressivo e visualização positiva, e explique de forma gentil. "
            "Sempre que possível, indique links de vídeos do YouTube e artigos de sites confiáveis sobre como se acalmar e se preparar para provas. Dê exemplos reais de exercícios e rotinas que o estudante pode seguir. "
            "Seja espontâneo, evite respostas robóticas e personalize a conversa conforme o contexto."
        )
        if self.azure_api_key and self.azure_endpoint and self.azure_deployment:
            import requests
            prompt = self._build_prompt(user_message, conversation, current_phase)
            url = f"{self.azure_endpoint}openai/deployments/{self.azure_deployment}/chat/completions?api-version={self.azure_api_version}"
            headers = {
                "Content-Type": "application/json",
                "api-key": self.azure_api_key
            }
            data = {
                "messages": [
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                "max_tokens": 140,
                "temperature": 0.3
            }
            try:
                response = requests.post(url, headers=headers, json=data, timeout=30)
                response.raise_for_status()
                result = response.json()
                ai_message = result["choices"][0]["message"]["content"]
                return {"message": ai_message.strip()}
            except Exception as e:
                return {"message": f"Erro ao conectar com a Azure OpenAI: {str(e)}"}
        # Fallback: OpenAI padrão
        elif self.api_key and self.api_key != 'sua_chave_aqui':
            prompt = self._build_prompt(user_message, conversation, current_phase)
            try:
                client = openai.OpenAI(api_key=self.api_key)
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=140,
                    temperature=0.3
                )
                ai_message = response.choices[0].message.content if hasattr(response.choices[0].message, 'content') else response.choices[0].message['content']
                return {'message': ai_message.strip()}
            except Exception as e:
                return {'message': f'Erro ao conectar com a OpenAI: {str(e)}'}
        else:
            return {
                'message': '🔧 Para usar a IA, configure sua chave da Azure OpenAI no arquivo .env.\n\n'
                           '1. Crie um recurso Azure OpenAI e faça o deployment de um modelo.\n'
                           '2. Copie a chave, endpoint e nome do deployment para o arquivo .env.\n\n'
                           'Por enquanto, posso simular uma resposta: "Quando você configurar a chave, poderei te ajudar de verdade!"'
            }

    def _build_prompt(self, user_message, conversation, current_phase):
        """Monta o prompt para a IA com base na fase da conversa."""
        if current_phase == 'initial':
            return f"Você é uma IA que acalma estudantes antes de provas. Pergunte como o estudante está se sentindo. Mensagem: {user_message}"
        elif current_phase == 'assessment':
            return f"Você é uma IA que avalia ansiedade pré-prova. Pergunte sobre ansiedade e preparação. Mensagem: {user_message}"
        elif current_phase == 'exercises':
            return f"Sugira um exercício de relaxamento para ansiedade antes de provas. Mensagem: {user_message}"
        elif current_phase == 'final':
            return f"Dê dicas finais e motivação para o estudante antes da prova. Mensagem: {user_message}"
        return user_message
