"""
Dashboard Web para visualización de hallazgos
"""
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>BugBounty IA Web Dashboard</h1><p>Estado: Activo</p>"

@app.route('/api/stats')
def stats():
    return jsonify({
        "status": "running",
        "agents": 4,
        "findings": 0
    })

def run_web():
    app.run(host='0.0.0.0', port=5000)

if __name__ == "__main__":
    run_web()
EOF
