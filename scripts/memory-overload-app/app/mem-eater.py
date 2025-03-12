from fastapi import FastAPI, HTTPException
import time

app = FastAPI()

data = []

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.post("/consume/{mb}")
def consume_memory(mb: int):
    """Consume specified amount of memory in megabytes."""
    global data
    if mb < 0:
        raise HTTPException(status_code=400, detail="Memory size must be non-negative")

    # 1 float = 8 bytes, 1 MB = 1024 * 1024 bytes
    num_floats = (mb * 1024 * 1024) // 8
    # Create a list of floats
    data = [0.0] * num_floats
    return {"status": "success", "message": f"Consuming {mb} MB of memory"}

@app.post("/release")
def release_memory():
    """Release the consumed memory."""
    global data
    data = []
    return {"status": "success", "message": "Memory released"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
