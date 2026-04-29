from flask import Flask
from dotenv import load_dotenv

# Load env FIRST
load_dotenv()

# Create app BEFORE using it
app = Flask(__name__)

# Import routes AFTER app creation
from routes.describe import describe_bp
from routes.recommend import recommend_bp
from routes.generate_report import report_bp
from routes.health import health_bp

# Register blueprints
app.register_blueprint(describe_bp)
app.register_blueprint(recommend_bp)
app.register_blueprint(report_bp)
app.register_blueprint(health_bp)

# Run app
if __name__ == "__main__":
    app.run(debug=True, port=5000)