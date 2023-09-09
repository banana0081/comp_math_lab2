from flask import Flask, render_template, request, make_response, jsonify, Response
import logic
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/equation', methods=['POST'])
def equation():
    return render_template('menu/equation.html')

@app.route('/system', methods=['POST'])
def system():
    return render_template('menu/system.html')

@app.route('/solve_equation', methods=['POST'])
def solve_equation():
    try:
        return jsonify(logic.solve_equation(request.get_json()))
    except Exception as ex:
        return make_response(str(ex), 400)

@app.route('/equation_graphic', methods=['POST'])
def equation_graphic():
    try:
        return Response(logic.draw_equation(request.get_json()), mimetype='image/png')
    except Exception as ex:
        return make_response(str(ex), 400)

@app.route('/solve_system', methods=['POST'])
def solve_system():
    try:
        return jsonify(logic.solve_system(request.get_json()))
    except Exception as ex:
        return make_response(str(ex), 400)

@app.route('/system_graphic', methods=['POST'])
def system_graphic():
    try:
        return Response(logic.draw_system(request.get_json()), mimetype='image/png')
    except Exception as ex:
        return make_response(str(ex), 400)



if __name__ == '__main__':
    app.run(debug=True)