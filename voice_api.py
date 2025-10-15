from flask import Flask, request, jsonify
from src.pipeline import run_pipeline

app = Flask(__name__)

@app.route('/api/voice', methods=['POST'])
def voice_api():
    data = request.json
    if not data or 'input' not in data:
        return jsonify({"error": "Provide input data in JSON format: {'input': [W,M,D,C,A,E,T,H,CO2,Hmd]}"}), 400
    input_data = data['input']
    weight_variant = data.get('weight_variant', 'linear')
    result = run_pipeline(data=input_data, weight_variant=weight_variant)
    return jsonify(json.loads(result))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)