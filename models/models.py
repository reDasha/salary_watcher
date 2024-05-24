from sqlalchemy import Table, Column, Integer, Float, String, Boolean, Date

from auth.database import metadata

user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("username", String, nullable=False),
    Column("email", String),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),
    Column("current_salary", Float),
    Column("salary_increase_date", Date),
)
