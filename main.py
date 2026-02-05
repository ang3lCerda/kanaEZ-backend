import uvicorn

if __name__ == "__main__":
    # This points to the 'app' instance inside your app/app.py file
    uvicorn.run("app.app:app", host="0.0.0.0", port=8000, reload=True)