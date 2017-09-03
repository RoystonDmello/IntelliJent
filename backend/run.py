""" RUnning this starts the backend
"""


from backend import app

app.run(host='0.0.0.0', port=5000, debug=True)
