import uuid

from sqlalchemy import ForeignKey, Integer, String, Uuid
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.sim_log import SimLog


class HazardStat(Base):
    __tablename__ = "hazard_stats"

    stat_id: Mapped[uuid.UUID] = mapped_column(
        Uuid, primary_key=True, default=uuid.uuid4
    )
    log_id: Mapped[uuid.UUID] = mapped_column(
        Uuid,
        ForeignKey("sim_logs.log_id", ondelete="CASCADE"),
        nullable=False,
        index=True,
    )
    hazard_type: Mapped[str | None] = mapped_column(String(32), nullable=True)
    count: Mapped[int | None] = mapped_column(Integer, nullable=True)

    log: Mapped[SimLog] = relationship(back_populates="hazard_stats")
