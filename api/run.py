import os
from flask import Flask
from apis import api
from config import ProductionConfig, TestingConfig, DevelopmentConfig

# Instatiate Flask app
app = Flask(__name__)

print('>>>>> otrrent starting in {} environment <<<<<'.format(app.config['ENV']))

# Configure Flask App
if app.config['ENV'] == 'production':
    app.config.from_object(ProductionConfig())
elif app.config['ENV'] == 'testing':
    app.config.from_object(TestingConfig())
else:
    app.config.from_object(DevelopmentConfig())

# Instatiate Restx Api
api.init_app(app)

# Instantiate Database
from core import db

# Run Flask App
if __name__ == "__main__":
    app.run(debug=app.config['DEBUG'])
