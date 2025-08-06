# Configuração do ZAPI para o Leone

## Passo a Passo para Configurar o Webhook

### 1. Acesse o Painel do ZAPI
- Entre em https://developer.z-api.io/
- Faça login com suas credenciais

### 2. Localize sua Instância
- Vá para "Minhas Instâncias"
- Encontre a instância com ID: `3E53AE16CC18B190D85F2AC1CE4E084C`
- Clique em "Configurar"

### 3. Configure o Webhook
- Na seção "Webhooks", clique em "Adicionar Webhook"
- **URL do Webhook**: `https://seu-dominio.com/webhook`
- **Método**: POST
- **Eventos**: Marque "message" (mensagens recebidas)

### 4. Teste a Conexão
- Use o botão "Testar Webhook" no painel do ZAPI
- Verifique se o endpoint `/health` responde corretamente

## URLs Importantes

### Desenvolvimento Local
- Health Check: `http://localhost:5000/health`
- Status: `http://localhost:5000/status`
- Webhook: `http://localhost:5000/webhook`

### Produção (Railway)
- Health Check: `https://seu-app.railway.app/health`
- Status: `https://seu-app.railway.app/status`
- Webhook: `https://seu-app.railway.app/webhook`

## Credenciais Configuradas

```
Instance ID: 3E53AE16CC18B190D85F2AC1CE4E084C
Token: FE159CBD3E314AC8890DBA72
```

## Estrutura da Mensagem Recebida

O ZAPI enviará mensagens no seguinte formato:

```json
{
  "phone": "5511999999999",
  "message": {
    "text": "Olá, estou procurando um imóvel"
  },
  "senderName": "João Silva",
  "timestamp": 1234567890
}
```

## Estrutura da Mensagem Enviada

O Leone enviará mensagens no seguinte formato:

```json
{
  "phone": "5511999999999",
  "message": "Olá! Me chamo Leone, sou o corretor virtual da Brabus..."
}
```

## Monitoramento

### Logs do Servidor
- Monitore os logs do Flask para ver as mensagens recebidas
- Verifique erros de conexão com a API do ZAPI

### Endpoints de Monitoramento
- `/health`: Verifica se o serviço está ativo
- `/status`: Mostra quantas conversas estão ativas

## Solução de Problemas

### Webhook não recebe mensagens
1. Verifique se a URL está correta no painel do ZAPI
2. Confirme se o servidor está acessível publicamente
3. Teste o endpoint `/health` externamente

### Mensagens não são enviadas
1. Verifique as credenciais (Instance ID e Token)
2. Confirme se a instância está ativa no ZAPI
3. Verifique os logs para erros de API

### Fluxos não funcionam corretamente
1. Teste localmente com o script `test_webhook.py`
2. Verifique se a detecção de intenção está funcionando
3. Monitore o endpoint `/status` para ver conversas ativas

## Backup e Segurança

- Mantenha as credenciais do ZAPI seguras
- Faça backup regular do código
- Monitore o uso da API para evitar limites
- Configure logs adequados para auditoria

