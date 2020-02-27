from flask import Flask
from flask import request, jsonify

app = Flask(__name__)


@app.route('/predict', methods=['GET', 'POST', 'DELETE'])
def user():
    if request.method == 'GET':
        return jsonify(
            isError=False,
            message="Success",
            statusCode=200,
            data={'method': "get"}
        )

    if request.method == 'POST':
        print(request.data)
        return jsonify(
            isError=False,
            message="Success",
            statusCode=200,
            data={'method': "post",
                  'json_post_data': request.json}
        )


if __name__ == '__main__':
    app.run(debug=True, port=5000)
