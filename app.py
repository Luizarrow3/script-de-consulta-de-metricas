from prometheus_client import start_http_server, Counter
import time

# Cria uma métrica de contador
REQUISICOES = Counter('app_requisicoes_total', 'Total de requisições na App')

if __name__ == '__main__':
    start_http_server(8000) # Expõe métricas em http://localhost:8000
    while True:
        REQUISICOES.inc()
        time.sleep(1)
        