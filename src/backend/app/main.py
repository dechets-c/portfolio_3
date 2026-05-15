from fastapi import FastAPI
from app.routers import admin, auth, public


app = FastAPI()
app.include_router(public.router)
app.include_router(admin.router)
app.include_router(auth.router)


def main():
    print("Hello from portfolio-s3!")


if __name__ == "__main__":
    main()
