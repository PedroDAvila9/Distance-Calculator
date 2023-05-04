from flask import Flask, request, render_template
import requests

app = Flask(__name__)

@app.route('/routes', methods=['GET'])
def distancia():
        
    api_key = '<YOUR_API_KEY>'

    rua = request.args['rua']
    num = request.args['num']
    cidade = request.args['cidade']
    estado = request.args['estado']
    rua_d = request.args['rua_d']
    num_d = request.args['num_d']
    cidade_d = request.args['cidade_d']
    estado_d = request.args['estado_d']

    if not rua or not num or not cidade or not estado:
        return render_template('invalid.html')
    if not rua_d or not num_d or not cidade_d or not estado_d:
        return render_template('invalid.html')
        

    origem = f"{rua} {num}, {cidade} - {estado}"
    destino = f"{rua_d} {num_d}, {cidade_d} - {estado_d}"

        # Faz a chamada HTTP para a API
    url = f'https://maps.googleapis.com/maps/api/distancematrix/json?units=metric&origins={origem}&destinations={destino}&key={api_key}'
    response = requests.get(url).json()
        
        # Tratamento de erro para caso a chave 'distance' não esteja presente no dicionário
    if 'distance' not in response['rows'][0]['elements'][0]:
        return render_template('invalid.html')

        # Exibe os resultados da API
    distancia = response['rows'][0]['elements'][0]['distance']['text']
    tempo = response['rows'][0]['elements'][0]['duration']['text']
    coordenadas_origem = response['origin_addresses'][0]
    coordenadas_destino = response['destination_addresses'][0]

    google_maps_url = f'https://www.google.com/maps/embed/v1/directions?key={api_key}&origin={origem}&destination={destino}'

    return render_template('resultado.html', distancia=distancia, tempo=tempo, coordenadas_origem=coordenadas_origem, coordenadas_destino=coordenadas_destino, google_maps_url=google_maps_url)


@app.route('/', methods=['GET'])
def index():
    return render_template('distancia.html')

if __name__ == '__main__':
    app.run(port=0)

