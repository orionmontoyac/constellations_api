from sqlalchemy.orm import mapped_column, Mapped, relationship
from sqlalchemy import ForeignKey

from extensions import db


class Stars(db.Model):
    __tablename__ = "stars"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(nullable=False)

    constellation_id: Mapped[int] = mapped_column(ForeignKey("constellations.id"))
    constellation: Mapped["Constellations"] = relationship(back_populates="stars")
