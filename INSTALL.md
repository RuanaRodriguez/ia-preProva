# INSTALAÇÃO E CONFIGURAÇÃO

## Pré-requisitos
- Python 3.8 ou superior
- Conta na OpenAI com créditos disponíveis

## Passo a passo

### 1. Instalar dependências
```bash
pip install -r requirements.txt
```

### 2. Configurar chave da OpenAI
1. Acesse https://platform.openai.com/api-keys
2. Crie uma nova chave da API
3. Copie o arquivo `.env.example` para `.env`
4. Substitua `sk-sua_chave_aqui` pela sua chave real

### 3. Executar a aplicação
```bash
python app.py
```

### 4. Acessar no navegador
Abra http://localhost:5000

## Solução de Problemas

### Erro de importação do Flask
```bash
pip install flask
```

### Erro de chave da OpenAI
- Verifique se o arquivo `.env` está correto
- Confirme se sua conta OpenAI tem créditos

### Erro de conexão
- Verifique sua conexão com a internet
- Confirme se a API da OpenAI está funcionando

## Funcionalidades

### Fases da Conversa
1. **Inicial**: Cumprimento e primeira avaliação
2. **Avaliação**: Análise detalhada do estado emocional
3. **Exercícios**: Técnicas de relaxamento se necessário
4. **Final**: Preparação e motivação para a prova

### Exercícios Disponíveis
- **Respiração 4-7-8**: Técnica de respiração para reduzir ansiedade
- **Relaxamento Muscular**: Tensão e relaxamento progressivo
- **Visualização**: Imaginação de cenários positivos para a prova

### Interface Web
- Design moderno e responsivo
- Chat em tempo real
- Indicadores visuais de exercícios
- Botão para reiniciar conversa
