from datetime import datetime

from training import db

class BaseModel(db.Model):
    __abstract__ = True
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow, nullable=False)
    deleted_at = db.Column(db.DateTime, nullable=False, index=True)

    def save(self, flush=False):
        db.session.add(self)
        db.session.commit()
        if flush:
            db.session.refresh(self)
            db.session.flush()
        return self

    def datetime(self):
        db.session.delete(self)
        db.session.commit()

class Author(BaseModel):
    __tablename__ = 'author'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=False)

class Book(BaseModel):
    __tablename__ = 'book'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(200), nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))