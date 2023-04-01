from sqlalchemy.orm import mapped_column, Mapped, relationship
from typing import List

from extensions import db
from api.models.stars import Stars


class Constellations(db.Model):
    __tablename__ = "constellations"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)
    abbr: Mapped[str] = mapped_column(nullable=False)
    right_ascension: Mapped[str] = mapped_column(nullable=False)

    stars: Mapped[List[Stars]] = relationship(back_populates='constellation', cascade="all, delete-orphan")
