import psutil
import time
from prometheus_client import start_http_server, Gauge

# 1. Definindo as métricas que queremos monitorar
# Usamos 'Gauge' porque os valores podem subir e descer (como o uso de CPU)
CPU_USAGE = Gauge('system_cpu_usage_percent', 'Porcentagem de uso da CPU')
MEMORY_USAGE = Gauge('system_memory_usage_percent', 'Porcentagem de uso da Memória RAM')
DISK_USAGE = Gauge('system_disk_usage_percent', 'Porcentagem de uso do Disco')

def collect_metrics():
    """Função que coleta dados do hardware e atualiza as métricas."""
    while True:
        # Coleta os dados do sistema
        cpu = psutil.cpu_percent(interval=1)
        memory = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        # Atualiza as métricas do Prometheus
        CPU_USAGE.set(cpu)
        MEMORY_USAGE.set(memory)
        DISK_USAGE.set(disk)

        print(f"Métricas atualizadas: CPU: {cpu}% | RAM: {memory}% | Disco: {disk}%")
        time.sleep(5)

if __name__ == '__main__':
    # Inicia o servidor de métricas na porta 8000
    # O Prometheus vai buscar os dados em http://localhost:8000/metrics
    start_http_server(8000)
    print("Servidor de métricas iniciado na porta 8000")
    collect_metrics()
     