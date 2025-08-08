# 🚨 GUIA RÁPIDO DE SOLUÇÃO DE PROBLEMAS

## Problema 1: "Token do Hugging Face não configurado"

### ✅ Solução:
1. **Obter token do Hugging Face:**
   - Acesse: https://huggingface.co/join
   - Crie uma conta gratuita
   - Gere um token em https://huggingface.co/settings/tokens
   - Copie o token

2. **Configurar no projeto:**
   - Abra o arquivo `.env` na raiz do projeto
   - Coloque: `HF_API_TOKEN=seu_token_aqui`
   - Salve o arquivo

3. **Reiniciar aplicação:**
   - Pare a aplicação (Ctrl+C no terminal)
   - Execute novamente: `python app.py`

## Problema 2: Aplicação reiniciando continuamente

### ✅ Solução:
- Mesmo problema acima - token do Hugging Face não configurado
- Siga os passos do Problema 1

## Problema 3: Erro "Não foi possível resolver importação flask"

### ✅ Solução:
```bash
pip install flask python-dotenv requests
```

## Problema 4: Erro de conexão com Hugging Face

### ✅ Verificar:
- [ ] Token está correto
- [ ] Conta Hugging Face não está suspensa
- [ ] Conexão com internet funcionando
- [ ] Arquivo .env está no formato correto

## Problema 5: Interface não carrega

### ✅ Solução:
1. Verificar se aplicação está rodando sem erros
2. Acessar: http://localhost:5000
3. Se ainda não funcionar, verificar console do navegador (F12)

## 📝 Formato correto do arquivo .env:
```
HF_API_TOKEN=seu_token_aqui
```

## 🆘 Se nada funcionar:
1. Delete o arquivo .env
2. Crie um novo token na Hugging Face
3. Configure sua chave no novo arquivo
4. Reinicie a aplicação
