from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import tempfile

from app.main import app
from app.db.database import Base
from app.dependencies import get_db


def get_test_engine(db_path):
    return create_engine(
        f"sqlite:///{db_path}", connect_args={"check_same_thread": False}
    )


def override_get_db(engine):
    SessionTesting = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    def _get_db():
        db = SessionTesting()
        try:
            yield db
        finally:
            db.close()

    return _get_db


def test_register_login_and_protected_admin():
    # use a unique temp DB file per test
    fd, db_path = tempfile.mkstemp(suffix=".db")
    os.close(fd)

    engine = get_test_engine(db_path)
    Base.metadata.create_all(bind=engine)

    # ensure SECRET_KEY is set for token creation in tests
    from app.core import security as sec

    sec.SECRET_KEY = "test-secret-for-integration"

    app.dependency_overrides[get_db] = override_get_db(engine)
    client = TestClient(app)

    # register
    resp = client.post(
        "/auth/register", json={"email": "bob@example.com", "password": "s3cret"}
    )
    if resp.status_code != 200:
        print("register response:", resp.status_code, resp.text)
    assert resp.status_code == 200
    data = resp.json()
    assert data["email"] == "bob@example.com"

    # login
    resp = client.post(
        "/auth/token", data={"username": "bob@example.com", "password": "s3cret"}
    )
    assert resp.status_code == 200
    token = resp.json().get("access_token")
    assert token

    # call protected admin endpoint
    headers = {"Authorization": f"Bearer {token}"}
    project_payload = {
        "name": "Test Project",
        "description": "desc",
        "role": "Développeur",
        "date_debut": "2023-01-01",
    }
    resp = client.post("/admin/create_project", json=project_payload, headers=headers)
    assert resp.status_code == 200
    project_id = resp.json()["id"]
    assert project_id

    # cleanup
    engine.dispose()
    os.remove(db_path)


def test_update_and_delete_project():
    # use a unique temp DB file per test
    fd, db_path = tempfile.mkstemp(suffix=".db")
    os.close(fd)

    engine = get_test_engine(db_path)
    Base.metadata.create_all(bind=engine)

    from app.core import security as sec

    sec.SECRET_KEY = "test-secret-for-integration"

    app.dependency_overrides[get_db] = override_get_db(engine)
    client = TestClient(app)

    # register and login
    client.post(
        "/auth/register", json={"email": "alice@example.com", "password": "s3cret"}
    )
    resp = client.post(
        "/auth/token", data={"username": "alice@example.com", "password": "s3cret"}
    )
    token = resp.json().get("access_token")
    headers = {"Authorization": f"Bearer {token}"}

    # create project
    project_payload = {
        "name": "Original Project",
        "description": "original desc",
        "role": "Développeur",
        "date_debut": "2023-01-01",
    }
    resp = client.post("/admin/create_project", json=project_payload, headers=headers)
    project_id = resp.json()["id"]

    # update project using typed endpoint
    update_payload = {
        "name": "Updated Project",
        "description": "updated desc",
    }
    resp = client.put(
        f"/admin/project/{project_id}", json=update_payload, headers=headers
    )
    assert resp.status_code == 200
    assert resp.json()["id"] == project_id

    # delete project
    resp = client.delete(f"/admin/delete/project/{project_id}", headers=headers)
    assert resp.status_code == 200
    assert resp.json()["id"] == project_id

    # cleanup
    engine.dispose()
    os.remove(db_path)
