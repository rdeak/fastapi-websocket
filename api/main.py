import os


host = os.getenv("HOST", "127.0.0.1")
port = int(os.getenv("PORT", 8000))


def main():
    import uvicorn
    uvicorn.run(
        "api.api:app",
        host=host,
        port=port,
        reload=True
    )


if __name__ == "__main__":
    main()
