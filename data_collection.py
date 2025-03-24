import psutil
import time

while True:
    print(f"CPU: {psutil.cpu_percent()}%", end=' | ')
    print(f"Memory: {psutil.virtual_memory().percent}%")
    time.sleep(2)
    print(*[p.name() for p in psutil.process_iter()][:5], "...") 
