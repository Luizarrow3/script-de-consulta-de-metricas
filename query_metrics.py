import requests
import json
from datetime import datetime

# Configurações
PROMETHEUS_URL = "http://localhost:9090" # URL do Prometheus (não do Python)
QUERY = "system_cpu_usage_percent"       # Nome da métrica que queremos consultar

def query_prometheus(query):
    try:
        # Endpoint de consulta instantânea do Prometheus
        response = requests.get(
            f"{PROMETHEUS_URL}/api/v1/query",
            params={'query': query}
        )
        response.raise_for_status() # Levanta erro se a requisição falhar
        
        data = response.json()
        
        if data['status'] == 'success':
            results = data['data']['result']
            
            if not results:
                print("Nenhum dado encontrado para esta métrica.")
                return

            for result in results:
                metric_name = result['metric'].get('__name__', 'metrica')
                value = result['value'][1] # O valor atual
                timestamp = result['value'][0] # Horário da coleta
                
                # Converte o timestamp para algo legível
                dt_object = datetime.fromtimestamp(timestamp)
                
                print(f"--- Consulta: {dt_object.strftime('%Y-%m-%d %H:%M:%S')} ---")
                print(f"Métrica: {metric_name}")
                print(f"Valor Atual: {value}%")
                print("-" * 40)
        else:
            print(f"Erro na resposta do Prometheus: {data.get('error')}")

    except requests.exceptions.ConnectionError:
        print("Erro: Não foi possível conectar ao Prometheus. Verifique se ele está rodando na porta 9090.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

if __name__ == "__main__":
    query_prometheus(QUERY)
    #usando scripts para automatizar os processo de monitoramento