import uuid

from sqlalchemy import Float, ForeignKey, Integer, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.build import Build


class SimLog(Base):
    __tablename__ = "sim_logs"

    log_id: Mapped[uuid.UUID] = mapped_column(
        Uuid, primary_key=True, default=uuid.uuid4
    )
    build_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("builds.build_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    total_cycles: Mapped[int | None] = mapped_column(Integer, nullable=True)
    cpi_value: Mapped[float | None] = mapped_column(Float, nullable=True)

    build: Mapped[Build] = relationship(back_populates="sim_logs")
    hazard_stats: Mapped[list["HazardStat"]] = relationship(  # noqa: F821
        back_populates="log", cascade="all, delete-orphan"
    )
