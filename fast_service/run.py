import uvicorn

from app.main import app
import os

if __name__ == "__main__":
    DEBUG = os.getenv("DEBUG")
    if DEBUG == "True":
        import ptvsd
        ptvsd.enable_attach(address = ('0.0.0.0', 5678))
        ptvsd.wait_for_attach()
        ptvsd.break_into_debugger()
    uvicorn.run(app, host="0.0.0.0", port=8000)
