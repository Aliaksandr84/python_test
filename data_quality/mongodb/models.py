from .db import get_db
from datetime import datetime

db = get_db()

# User functions
def create_user(username, email):
    user = {
        "username": username,
        "email": email,
        "created_at": datetime.utcnow()
    }
    return db.users.insert_one(user).inserted_id

def get_user_by_username(username):
    return db.users.find_one({"username": username})

# Dataset functions
def create_dataset(name, path):
    dataset = {
        "name": name,
        "path": path,
        "uploaded_at": datetime.utcnow()
    }
    return db.datasets.insert_one(dataset).inserted_id

# QualityReport with embedded ColumnChecks
def create_quality_report(user_id, dataset_id, column_checks):
    report = {
        "user_id": user_id,
        "dataset_id": dataset_id,
        "checked_at": datetime.utcnow(),
        "column_checks": column_checks  # List of {"column_name": str, "null_count": int}
    }
    return db.quality_reports.insert_one(report).inserted_id

def get_reports_for_dataset(dataset_id):
    return list(db.quality_reports.find({"dataset_id": dataset_id}))