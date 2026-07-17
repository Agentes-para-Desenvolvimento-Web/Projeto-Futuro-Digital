from datetime import datetime  # Corrigido de 'time' para 'datetime'
from sqlalchemy import TIMESTAMP, VARCHAR, func, TEXT
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base

class Agent(Base):
    __tablename__ = "agents"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(VARCHAR(100))
    system_prompt: Mapped[str] = mapped_column(TEXT)

    created_at: Mapped[datetime] = mapped_column(
        TIMESTAMP(timezone=True),
        server_default=func.now(),
        nullable=True
    )