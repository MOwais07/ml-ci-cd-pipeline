from flask import Flask
from .main import main

app = Flask(__name__)
app.register_blueprint(main)  # Ensure this line is present

if __name__ == "__main__":
    app.run(debug=True)
