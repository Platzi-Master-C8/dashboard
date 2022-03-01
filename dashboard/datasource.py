from sqlalchemy import create_engine
from sqlalchemy.sql import text
from sqlalchemy.engine import Engine, Connection, CursorResult

DATABASE_URI = "postgresql://dywapbyl:baCNBzlMNccJ69at2VTQ4l8YIPD3xo_w@castor.db.elephantsql.com/dywapbyl"

engine: Engine = create_engine(
    DATABASE_URI, echo=False
)


def execute(conn: Connection, query: str, **kwargs) -> CursorResult:
    return conn.execute(text(query), **kwargs)


def scalar(conn: Connection, query: str, **kwargs) -> any:
    return conn.scalar(text(query), **kwargs)
