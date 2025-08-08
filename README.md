# IA de Apoio Pré-Prova

Uma aplicação web que utiliza IA gratuita (Hugging Face) para avaliar e acalmar estudantes antes de provas.

## Funcionalidades

- Avaliação do estado emocional do estudante
- Perguntas personalizadas para identificar ansiedade
- Exercícios de relaxamento guiados
- Interface web moderna e intuitiva

## Como usar

1. **Instale as dependências:**
```bash
pip install -r requirements.txt
```

2. **Configure seu token gratuito do Hugging Face:**
   - Crie uma conta em https://huggingface.co/join
   - Gere um token em https://huggingface.co/settings/tokens
   - Edite o arquivo `.env` e coloque:
     ```
     HF_API_TOKEN=seu_token_aqui
     ```

3. **Execute a aplicação:**
```bash
python app.py
```

4. **Acesse no navegador:**
   - http://localhost:5000

## Estrutura do Projeto

- `app.py` - Aplicação Flask principal
- `ai_helper.py` - Lógica da IA para avaliação e aconselhamento
- `templates/` - Templates HTML
- `static/` - Arquivos CSS e JavaScript
- `requirements.txt` - Dependências do projeto

## Observações
- O plano gratuito da Hugging Face tem limite de requisições por minuto.
- Não é necessário cartão de crédito para usar o plano gratuito.
