from fastapi import FastAPI
from app.routers import admin


app = FastAPI()
app.include_router(admin)


def main():
    print("Hello from portfolio-s3!")


if __name__ == "__main__":
    main()
