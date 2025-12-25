from fastapi import FastAPI, Request
from function_loader import execute_function
import os

app = FastAPI()

# function execute
@app.post("/func/{func_name}/{method}")
async def call_function(func_name: str, method: str, request: Request):
    try:
      data = await request.json()
    except:
      data = None  # if not body 
    print("Method: ", method)
    print("Arguments: ", data)
    result = execute_function(func_name, data, method)
    return result

# get all framework lists
@app.get("/frmlist")
def frameworklists():
  frmlists = os.listdir("functions")  # getting a list of folders containing libraries
  return {"frameworks": frmlists}
