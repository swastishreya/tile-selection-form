from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/submit', methods=['POST'])
def submit():
    data = request.json
    selected_tiles = data.get('selected', [])
    return jsonify({"message": "Success", "selected_tiles": selected_tiles})

if __name__ == '__main__':
    app.run(debug=True)
