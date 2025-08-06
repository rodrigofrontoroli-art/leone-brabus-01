# Leone Brabus

API com Flask + OpenAI GPT-4 para atendimento automatizado via WhatsApp.

Endpoints:
- [GET]  /          → Verifica se está no ar
- [POST] /webhook   → Recebe {"message": "texto"} e responde com GPT-4