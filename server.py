from flask import Flask
from flask_graphql import GraphQLView

from src.infra.database import db_session
from src.delivery.schema import schema

import os

DEBUG = os.getenv('DEBUG', True)

app = Flask(__name__)

app.add_url_rule('/delivery',
                 view_func=GraphQLView.as_view('delivery', schema=schema, graphiql=True))

@app.teardown_appcontext
def remove_session(exception=None):
    db_session.remove()

if __name__ == '__main__':
    app.run(debug=DEBUG)
