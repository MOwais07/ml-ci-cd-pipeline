# app/app.py

from app import app
from app.main import main

# Register the main blueprint
app.register_blueprint(main)

if __name__ == "__main__":
    app.run(debug=True)
