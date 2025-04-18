
# app/app.py - Flask-based Python web application

from flask import Flask
import logging

# Configure logging for production
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Initialize Flask app
app = Flask(__name__)

# Define health check endpoint
@app.route('/health')
def health():
    logger.info("Health check endpoint called")
    return {"status": "healthy"}, 200

# Define main endpoint
@app.route('/')
def home():
    logger.info("Home endpoint called")
    return {"message": "Welcome to the Python App!"}, 200

# Run the app in production mode
if __name__ == '__main__':
    logger.info("Starting Flask application")
    app.run(host='0.0.0.0', port=8080)