from fastapi import FastAPI, Request

app = FastAPI()

@app.get("/")
async def health_check():
    return {"status": "OK"}

@app.post("/webhook")
async def telegram_webhool(request : Request):
    data = await request.json()
    print(data)
    return {"status": "received"}