import uvicorn
import dotenv

config = dotenv.dotenv_values(".env")

if __name__ == "__main__":
    uvicorn.run(
        app="main:app",
        reload=config.get("SERVER_RELOAD", True), 
        port=int(config.get("SERVER_PORT")),
        host=config.get("SERVER_HOST")
        )
