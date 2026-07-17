from datetime import datetime
from sqlalchemy import VARCHAR, TIMESTAMP, func, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

class Customer(Base):
    __tablename__ = "customers"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    email: Mapped[str] = mapped_column(VARCHAR(255), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(VARCHAR(20), nullable=False, unique=True)
    cep: Mapped[str | None] = mapped_column(VARCHAR(10), nullable=True)
    cpf: Mapped[str] = mapped_column(VARCHAR(11), nullable=False, unique=True)

    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=True)
    lead_id: Mapped[int | None] = mapped_column(ForeignKey("leads.id"), nullable=True)
    lead: Mapped["Lead"] = relationship(back_populates="customers")