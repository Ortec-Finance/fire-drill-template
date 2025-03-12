from fastapi import FastAPI
import threading
import time
import uvicorn

app = FastAPI()

# Dictionary to keep track of threads and their stop flags
tasks = {}

def cpu_intensive_task(task_id: str, stop_flag, duration_in_minutes: float):
    """ Function to simulate CPU load for a given duration in minutes """
    end_time = time.time() + duration_in_minutes * 60  # Convert minutes to seconds
    while time.time() < end_time and not stop_flag["stop"]:
        # Perform some CPU-intensive computations
        [x**2 for x in range(10000)]

@app.get("/consume/cpu/{millicpu}/{duration_in_minutes}")
async def consume_cpu(millicpu: int, duration_in_minutes: float):
    """ Endpoint to trigger CPU load for a specified duration """
    task_id = f"task_{time.time()}"  # Unique identifier for the task

    # Create a stop flag for this task
    stop_flag = {"stop": False}
    tasks[task_id] = stop_flag

    # Run the CPU task in a separate thread
    thread = threading.Thread(target=cpu_intensive_task, args=(task_id, stop_flag, duration_in_minutes))
    thread.start()

    return {"message": f"Started CPU load for {millicpu} millicpu for {duration_in_minutes} minutes", "task_id": task_id}

@app.get("/compute/factorial/{factorial}/{jobs}")
async def compute(factorial: int, jobs: int):
    print("Computing the Factorial of", factorial)
    
    threads = []
    for _ in range(jobs):
        thread = threading.Thread(target=highly_inefficient_factorial, args=(factorial,))
        thread.start()
        threads.append(thread)

    # Optionally, wait for all threads to complete
    for thread in threads:
        thread.join()

    return f"Triggered {jobs} jobs to compute the factorial of {factorial}"

from multiprocessing import Pool

@app.get("/compute/extreme/{factorial}/{jobs}")
async def compute(factorial: int, jobs: int):
    print("Computing the Factorial of", factorial)

    with Pool(jobs) as p:
        results = p.map(highly_inefficient_factorial, [factorial] * jobs)
        print(results)
        
    return f"Triggered {jobs} jobs to compute the factorial of {factorial}"

    
def highly_inefficient_factorial(n):
    if n == 0:
        return 1
    else:
        result = 1
        for i in range(n):
            result *= highly_inefficient_factorial(i)
        return result

@app.get("/cancel/{task_id}")
async def cancel_task(task_id: str):
    """ Endpoint to cancel a running CPU task """
    if task_id in tasks:
        tasks[task_id]["stop"] = True
        return {"message": f"Task {task_id} is being stopped."}
    else:
        return {"message": f"No task found with ID {task_id}"}

if __name__ == "__main__":
    jobs=50
    factorial=9999
    with Pool(jobs) as p:
        results = p.map(highly_inefficient_factorial, [factorial] * jobs)
        print(results)
    print("Bootup finished")
    uvicorn.run(app, host="0.0.0.0", port=8000)
