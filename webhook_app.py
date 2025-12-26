from fastapi import FastAPI, Request
from bot import application
from telegram import Update


app = FastAPI()

@app.get("/")
async def health_check():
    return {"status": "OK"}

@app.post("/webhook")
async def telegram_webhook(request : Request):
    print("WEBHOOK HIT")
    data = await request.json()
    update = Update.de_json(data, application.bot)
    await application.process_update(update)
    return {"status": "ok"}

@app.on_event("startup")
async def on_startup():
    await application.initialize()