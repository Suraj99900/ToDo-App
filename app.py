from flask import Flask, jsonify
from route.user import rUserBp

app = Flask(__name__)

# Register the user blueprint with the app
app.register_blueprint(rUserBp)

if __name__ == '__main__':
    app.run(debug=True)
