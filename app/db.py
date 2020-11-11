from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BaseModelMixin:

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @classmethod
    def get_all(cls):
        return cls.query.order_by(cls.name).all()
    @classmethod
    def get_by_name(cls):
        return cls.query.filter_by(cls.name).all()

    @classmethod
    def get_by_id(cls, id):
        return cls.query.get(id)

    @classmethod
    def simple_filter(cls, **kwargs):
        return cls.query.filter_by(**kwargs).all()
