from flask import Blueprint, render_template, request, jsonify

routes_main = Blueprint('routes_main', __name__)

@routes_main.route('/map')
def map_view():
    return render_template('map.html')

@routes_main.route('/chart')
def chart_view():
    return render_template('chart.html')

@routes_main.route('/procesar_voz', methods=['GET', 'POST'])
def procesar_voz():
    if request.method == 'POST':
        # Recibir JSON desde fetch
        data = request.get_json()
        texto = data.get('texto') if data else ""
        
        print("Texto recibido:", texto)
        
        respuesta = {"mensaje": f"Texto recibido: {texto}"}
        return jsonify(respuesta)
    
    return render_template('speech.html')
