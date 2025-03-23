from flask import Flask
from app.part2.api.v1 import api as api_blueprint
from app.part2.api.persistence.database import Database
from config import DevelopmentConfig

# Initialize Flask app
app = Flask(__name__)

# Initialize the database
db = Database(app)

# Register API blueprints
app.register_blueprint(api_blueprint, url_prefix='/api/v1')
app.config.from_object(DevelopmentConfig)

# Start the application
if __name__ == "__main__":
    app.run(debug=True)
