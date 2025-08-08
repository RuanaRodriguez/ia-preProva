from flask import Flask, render_template, request, jsonify, session
import os
from dotenv import load_dotenv
from ai_helper import AIHelper
import secrets

# Carregar variáveis de ambiente
load_dotenv()

app = Flask(__name__)
app.secret_key = secrets.token_hex(16)

# Inicializar o helper da IA
try:
    ai_helper = AIHelper()
    print("✅ IA Helper inicializado com sucesso!")
except Exception as e:
    print(f"❌ Erro ao inicializar IA Helper: {e}")
    ai_helper = None

@app.route('/')
def index():
    """Página inicial"""
    session.clear()  # Limpar sessão anterior
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    """Endpoint para conversa com a IA"""
    try:
        data = request.get_json()
        user_message = data.get('message', '')
        
        if not user_message:
            return jsonify({'error': 'Mensagem vazia'}), 400
        
        # Verificar se AI Helper está disponível
        if not ai_helper:
            return jsonify({
                'message': '❌ Erro: IA não disponível. Verifique a configuração.',
                'phase': 'error'
            })
        
        # Inicializar histórico da conversa se não existir
        if 'conversation' not in session:
            session['conversation'] = []
            session['phase'] = 'initial'  # initial, assessment, exercises, final
        
        # Adicionar mensagem do usuário ao histórico
        session['conversation'].append({
            'role': 'user',
            'content': user_message
        })
        
        # Processar mensagem com a IA
        response = ai_helper.process_message(
            user_message, 
            session['conversation'], 
            session['phase']
        )
        
        # Adicionar resposta da IA ao histórico
        session['conversation'].append({
            'role': 'assistant',
            'content': response['message']
        })
        
        # Atualizar fase se necessário
        if 'next_phase' in response:
            session['phase'] = response['next_phase']
        
        return jsonify({
            'message': response['message'],
            'phase': session['phase'],
            'exercise': response.get('exercise'),
            'assessment': response.get('assessment')
        })
        
    except Exception as e:
        print(f"❌ Erro no endpoint /chat: {e}")
        return jsonify({
            'error': f'Erro interno: {str(e)}',
            'message': 'Desculpe, ocorreu um erro. Tente novamente em alguns segundos.'
        }), 500

@app.route('/reset')
def reset():
    """Resetar conversa"""
    session.clear()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
