bind = "0.0.0.0:8000"  # Binds to all interfaces on port 8000
workers = 4  # Number of worker processes (adjust based on CPU cores)
worker_class = "uvicorn.workers.UvicornWorker"  # Uses Uvicorn's ASGI worker
timeout = 120  # Timeout in seconds
loglevel = "info"
