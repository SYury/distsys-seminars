import logging

from flask import Flask, redirect, request


def create_app() -> Flask:
    """
    Create flask application
    """
    app = Flask("simple server", static_folder='/static', static_url_path='')

    @app.route('/hello', methods=['GET'])
    def hello():
        return "Hello!"

    @app.route('/hi', methods=['GET'])
    def hi():
        return redirect('/hello', code=301)

    return app


app = create_app()

if __name__ == '__main__':
    logging.basicConfig()
    app.run(host='0.0.0.0', port=80)
