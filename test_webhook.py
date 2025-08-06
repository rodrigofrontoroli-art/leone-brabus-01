#!/usr/bin/env python3
"""
Script de teste para o webhook do Leone
Simula diferentes tipos de mensagens e testa os fluxos de conversa
"""

import requests
import json
import time

BASE_URL = "http://localhost:5000"

def test_health_check():
    """Testa o health check"""
    print("🔍 Testando health check...")
    response = requests.get(f"{BASE_URL}/health")
    print(f"Status: {response.status_code}")
    print(f"Resposta: {response.json()}")
    print()

def test_status():
    """Testa o endpoint de status"""
    print("📊 Testando status...")
    response = requests.get(f"{BASE_URL}/status")
    print(f"Status: {response.status_code}")
    print(f"Resposta: {response.json()}")
    print()

def send_message(phone, message, sender_name=None):
    """Envia uma mensagem para o webhook"""
    payload = {
        "phone": phone,
        "message": {
            "text": message
        }
    }
    
    if sender_name:
        payload["senderName"] = sender_name
    
    response = requests.post(f"{BASE_URL}/webhook", json=payload)
    return response

def test_studio_flow():
    """Testa o fluxo de studio"""
    print("🏠 Testando fluxo de STUDIO...")
    phone = "5511111111111"
    
    # Primeira mensagem
    response = send_message(phone, "Olá, estou procurando um studio", "Maria")
    print(f"Resposta 1: {response.json()}")
    
    # Simula respostas do usuário
    responses = [
        "Sim, pode perguntar",
        "Prefiro Vila Madalena",
        "Uns 30m²",
        "Sim, próximo ao metrô seria ótimo",
        "Até R$ 300.000",
        "Prefiro pronto"
    ]
    
    for i, resp in enumerate(responses, 2):
        time.sleep(1)  # Pequena pausa entre mensagens
        response = send_message(phone, resp)
        print(f"Resposta {i}: {response.json()}")
    
    print()

def test_cobertura_flow():
    """Testa o fluxo de cobertura"""
    print("🏢 Testando fluxo de COBERTURA...")
    phone = "5522222222222"
    
    # Primeira mensagem
    response = send_message(phone, "Estou interessado em cobertura", "Carlos")
    print(f"Resposta 1: {response.json()}")
    
    # Simula respostas do usuário
    responses = [
        "Sim, pode perguntar",
        "No mínimo 80m²",
        "2 suítes e 2 vagas",
        "Prefiro Moema ou Vila Olímpia",
        "Piscina e churrasqueira"
    ]
    
    for i, resp in enumerate(responses, 2):
        time.sleep(1)
        response = send_message(phone, resp)
        print(f"Resposta {i}: {response.json()}")
    
    print()

def test_captacao_flow():
    """Testa o fluxo de captação"""
    print("📋 Testando fluxo de CAPTAÇÃO...")
    phone = "5533333333333"
    
    # Primeira mensagem
    response = send_message(phone, "Quero vender meu apartamento", "Ana")
    print(f"Resposta 1: {response.json()}")
    
    # Simula respostas do usuário
    responses = [
        "Sim, gostaria de anunciar",
        "Rua das Flores, 123 - Vila Madalena",
        "60m², 2 quartos, 1 vaga",
        "Condomínio R$ 800, IPTU R$ 200",
        "Sim, reformei a cozinha recentemente",
        "Posso na próxima semana"
    ]
    
    for i, resp in enumerate(responses, 2):
        time.sleep(1)
        response = send_message(phone, resp)
        print(f"Resposta {i}: {response.json()}")
    
    print()

def main():
    """Executa todos os testes"""
    print("🤖 INICIANDO TESTES DO LEONE\n")
    
    # Testes básicos
    test_health_check()
    test_status()
    
    # Testes de fluxo
    test_studio_flow()
    test_cobertura_flow()
    test_captacao_flow()
    
    # Status final
    print("📊 Status final:")
    test_status()
    
    print("✅ Testes concluídos!")

if __name__ == "__main__":
    main()

