from fastapi import FastAPI

from app.routers import version, users

app = FastAPI(title="Python API Architecture",
              description="This project aims to design and implement a simple, efficient API architecture using "
                          "Python. It will cover essential topics such as RESTful API design, authentication, "
                          "database integration, and error handling. By the end, you'll know how to create and manage "
                          "APIs effectively.",
              version="1.0.0",
              docs_url="/swagger",
              redoc_url="/redoc")
app.include_router(version.router)
app.include_router(users.router)


@app.get("/")
def read_root():
    return {"message": "Python API Architecture"}
