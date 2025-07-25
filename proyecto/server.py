from flask import Flask, request, jsonify, send_from_directory
import modelo1

app = Flask(__name__, static_folder='static')

# 1) Sirve el HTML estático
@app.route('/')
def index():
    return send_from_directory(app.static_folder, 'index.html')

# 2) Recibe los datos del formulario y predice
@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    # Llama a tu función del modelo
    result = modelo1.predict_person(data)
    return jsonify({'prediction': result})

if __name__ == '__main__':
    # Ejecuta en http://localhost:5000
    app.run(debug=True)
