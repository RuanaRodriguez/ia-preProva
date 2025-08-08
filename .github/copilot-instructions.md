<!-- Use this file to provide workspace-specific custom instructions to Copilot. For more details, visit https://code.visualstudio.com/docs/copilot/copilot-customization#_use-a-githubcopilotinstructionsmd-file -->

# IA de Apoio Pré-Prova - Instruções para Copilot

Este é um projeto Python Flask que implementa uma IA para acalmar e preparar estudantes antes de provas.

## Arquitetura do Projeto

- **Flask**: Framework web para a interface
- **OpenAI GPT**: IA conversacional para interação com estudantes
- **Sessões**: Para manter contexto da conversa
- **Fases da Conversa**: initial → assessment → exercises → final

## Funcionalidades Principais

1. **Avaliação Inicial**: Cumprimentar e entender o estado emocional
2. **Análise de Aptidão**: Determinar se o estudante está pronto para a prova
3. **Exercícios de Relaxamento**: Respiração, relaxamento muscular, visualização
4. **Preparação Final**: Dicas e motivação para a prova

## Padrões de Código

- Use docstrings em português para funções
- Mantenha a lógica da IA em `ai_helper.py` separada do Flask
- Interface responsiva e moderna no frontend
- Tratamento de erros robusto para API da OpenAI

## Exercícios Disponíveis

- Respiração 4-7-8
- Relaxamento Muscular Progressivo  
- Visualização Positiva

## Configuração

Requer chave da OpenAI em arquivo `.env`
