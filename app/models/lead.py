from datetime import datetime

from sqlalchemy import TIMESTAMP, VARCHAR, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base
from app.models.customer import Customer

class Lead(Base):
    __tablename__ = "leads"

    id: Mapped[int] = mapped_column(primary_key=True)
    full_name: Mapped[str] = mapped_column(VARCHAR(255), nullable=False)
    email: Mapped[str] = mapped_column(VARCHAR(255), nullable=False, unique=True)
    phone: Mapped[str] = mapped_column(VARCHAR(20), nullable=False, unique=True)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=True)

    customer: Mapped["Customer"] = relationship(back_populates="leads")