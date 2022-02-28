from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.engine import Engine, Connection, CursorResult

DATABASE_URI = "sqlite:///job_placement.db"

engine: Engine = create_engine(
    DATABASE_URI,
    connect_args={"check_same_thread": False}
)


def execute(conn: Connection, query: str, **kwargs) -> CursorResult:
    return conn.execute(text(query), **kwargs)


def scalar(conn: Connection, query: str, **kwargs) -> any:
    return conn.scalar(text(query), **kwargs)
