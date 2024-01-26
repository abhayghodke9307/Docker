from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def get_data():
    file_name = request.args.get('n')
    line_number = request.args.get('m')

    if file_name is None:
        return "Missing 'n' parameter", 400

    file_path = f'/tmp/data/{file_name}.txt'

    try:
        with open(file_path, 'r') as file:
            if line_number is not None:
                content = next(line for i, line in enumerate(file, start=1) if i == int(line_number))
            else:
                content = file.read()

        return content
    except FileNotFoundError:
        return "File not found", 404

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=8080)
