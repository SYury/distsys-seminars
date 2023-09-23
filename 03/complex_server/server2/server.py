import os

from flask import Flask, request, send_from_directory


def create_app() -> Flask:
    """
    Create flask application
    """
    app = Flask("complex server")

    @app.route('/hello', methods=['GET'])
    def hello():
        return "Hello!"

    @app.route('/<path:path>', methods=['GET', 'POST', 'DELETE'])
    def serve(path):
        if request.method == 'GET':
            return send_from_directory('/static', path)
        elif request.method == 'POST':
            data = request.get_data()
            with open('/static/' + path, 'wb') as f:
                f.write(data)
            return '', 204
        else:
            try:
                os.unlink('/static/' + path)
            except FileNotFoundError:
                return 'Not Found', 404
            else:
                return '', 204

    return app


app = create_app()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
