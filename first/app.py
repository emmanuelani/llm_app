from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from simple import *

app = FastAPI()

@app.get('/')
async def default():
    return{
        "message": "App running sucessfully"
    }

@app.get('/healthz')
async def health():
    """
    This is used to 
    """
    return{
        "application": "Simple LLM App",
        "message": "Running successfully"
    }

@app.post("/chat")
async def generate_chat(request: Request):

    query = await request.json()
    model = query["model"]

    try:
        temperature = float(query['temp'])
    except:
        return{
            "error": "Invalid input, pass a number between 0 and 2"
        }
    
    if model not in models:
        return{
            "error": "You did not pass a correct model code"
        }

    response = generate(
        model, 
        query['question'],
        temp=temperature
    )

    return{
        "status": "success",
        "response": response
    }


if __name__ == "__main__":
    import uvicorn
    print("Starting LLM API")
    uvicorn.run(app, host="localhost", reload=True)