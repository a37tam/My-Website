from app import app

@app.route('/')
def home():
    return "This is the homepage."
