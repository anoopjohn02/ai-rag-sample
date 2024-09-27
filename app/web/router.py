"""
Router module
"""
import uvicorn
from fastapi import FastAPI
from app.web.controller import ChatController, TestController, TokenUsageController

def start():
    """
    Start method
    """
    api = FastAPI()
    api.include_router(ChatController.create_router())
    api.include_router(TokenUsageController.create_router())
    api.include_router(TestController.create_router())
    uvicorn.run(api, host="0.0.0.0", port=8080)
