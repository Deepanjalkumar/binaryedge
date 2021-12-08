from typing import Optional
import os
from fastapi import FastAPI

app = FastAPI()

@app.get("/subdomain/{domain}")
def read_root(domain:str):
    cwd=os.getcwd() #Getting the location of current working directory
    path=os.path.join(cwd, "data", "subdomain")
    with open(f"{path}/{domain}.txt", "r") as file:
        file=file.readlines()
    return {domain:file}

@app.get("/dataleaks/{domain}")
def read_root(domain:str):
    cwd=os.getcwd() #Getting the location of current working directory
    path=os.path.join(cwd, "data", "email")
    with open(f"{path}/{domain}.txt", "r") as file:
        file=file.readlines()
    return {domain:file}


