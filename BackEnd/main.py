#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 24/8/2021 下午8:02
# @Author  : Song Zihan
# @File    : main.py
# @useage  :
# -*- +++++++++++++ -*-
import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


origins = [
    "http://localhost",
    "http://localhost:8080",
]

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/hello")
async def root():
    return {"message": "Hello World"}

if __name__ == '__main__':
    uvicorn.run("main:app", host="localhost", port=5000, log_level="info")
