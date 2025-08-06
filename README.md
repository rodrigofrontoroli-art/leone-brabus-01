# Leone - Robô Corretor de Imóveis

Leone é um robô corretor de imóveis inteligente que atende leads automaticamente via WhatsApp, utilizando uma abordagem consultiva, empática e estratégica.

## Funcionalidades

- **Atendimento Automatizado**: Responde automaticamente às mensagens no WhatsApp
- **Fluxos Inteligentes**: Três fluxos de conversa especializados:
  - **Studio**: Para clientes interessados em studios/kitinetes
  - **Cobertura**: Para clientes interessados em coberturas
  - **Captação**: Para proprietários que desejam vender imóveis
- **Detecção de Intenção**: Identifica automaticamente o tipo de interesse do cliente
- **Transferência Inteligente**: Ao final do atendimento, transfere para o corretor humano (Rodrigo)

## Configuração

### 1. Credenciais ZAPI

As credenciais do ZAPI estão configuradas no arquivo `src/routes/webhook.py`:

```python
ZAPI_INSTANCE_ID = "3E53AE16CC18B190D85F2AC1CE4E084C"
ZAPI_TOKEN = "FE159CBD3E314AC8890DBA72"
```

### 2. Instalação

```bash
# Clone o projeto
cd leone-robot

# Ative o ambiente virtual
source venv/bin/activate

# Instale as dependências
pip install -r requirements.txt
```

### 3. Execução Local

```bash
# Ative o ambiente virtual
source venv/bin/activate

# Execute o servidor
python src/main.py
```

O servidor estará disponível em `http://localhost:5000`

## Endpoints

### Webhook Principal
- **URL**: `/webhook`
- **Método**: POST
- **Descrição**: Recebe mensagens do ZAPI e processa as conversas

### Health Check
- **URL**: `/health`
- **Método**: GET
- **Resposta**: `{"status": "ok", "message": "Leone ativo"}`

### Status das Conversas
- **URL**: `/status`
- **Método**: GET
- **Descrição**: Mostra quantas conversas estão ativas

## Configuração no ZAPI

1. Acesse o painel do ZAPI
2. Configure o webhook para apontar para: `https://seu-dominio.com/webhook`
3. Certifique-se de que as credenciais (Instance ID e Token) estão corretas

## Fluxos de Conversa

### Studio
1. Saudação e apresentação
2. Pergunta sobre região preferida
3. Pergunta sobre metragem
4. Pergunta sobre proximidade ao metrô
5. Pergunta sobre valor de investimento
6. Pergunta sobre imóvel pronto ou na planta
7. Transferência para corretor humano

### Cobertura
1. Saudação específica para cobertura
2. Pergunta sobre metragem mínima
3. Pergunta sobre suítes e vagas
4. Pergunta sobre região/bairro
5. Pergunta sobre comodidades
6. Transferência para corretor humano

### Captação
1. Saudação da imobiliária
2. Confirmação do interesse em anunciar
3. Pergunta sobre endereço/região
4. Pergunta sobre características do imóvel
5. Pergunta sobre valores (condomínio/IPTU)
6. Pergunta sobre reformas/diferenciais
7. Agendamento para material de marketing
8. Transferência para corretor humano

## Deployment

O projeto está configurado para deployment no Railway. Para fazer o deploy:

1. Conecte seu repositório ao Railway
2. Configure as variáveis de ambiente se necessário
3. O Railway detectará automaticamente o projeto Flask
4. Configure o webhook no ZAPI para apontar para a URL do Railway

## Estrutura do Projeto

```
leone-robot/
├── src/
│   ├── routes/
│   │   ├── webhook.py      # Lógica principal do robô
│   │   └── user.py         # Rotas de usuário (template)
│   ├── models/
│   │   └── user.py         # Modelos de banco (template)
│   ├── static/             # Arquivos estáticos
│   └── main.py             # Ponto de entrada da aplicação
├── venv/                   # Ambiente virtual
├── requirements.txt        # Dependências
└── README.md              # Esta documentação
```

## Personalização

Para personalizar os fluxos de conversa, edite o dicionário `FLUXOS` no arquivo `src/routes/webhook.py`.

Para adicionar novos tipos de detecção de intenção, modifique a função `detect_intent()` no mesmo arquivo.

## Monitoramento

- Use o endpoint `/health` para verificar se o serviço está funcionando
- Use o endpoint `/status` para ver quantas conversas estão ativas
- Monitore os logs do servidor para debugar problemas

## Suporte

Para suporte técnico ou dúvidas sobre a implementação, consulte a documentação do ZAPI ou entre em contato com o desenvolvedor.

