from sqlalchemy import create_engine
from app import app   

engine = create_engine(app.SQLALCHEMY_DATABASE_URI)

class SqlEngine:
    def init(self) -> None:
        self.engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])