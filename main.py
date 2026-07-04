from fastapi import FastAPI

app = FastAPI(title="MessageX")

@app.get('/')
def health():
    return {
        'message' : "Your Chat application is up and running!!"
    }