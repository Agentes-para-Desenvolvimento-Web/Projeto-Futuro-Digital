from datetime import datetime
from sqlalchemy import ForeignKey, String, TIMESTAMP, func
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.database import Base

class Conversation(Base):
    __tablename__ = "conversations"

    id: Mapped[int] = mapped_column(primary_key=True)
    mensagem: Mapped[str] = mapped_column(String, nullable=False)
    agente_id: Mapped[int] = mapped_column(ForeignKey("agents.id"))
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now())
    agente: Mapped["Agent"] = relationship(back_populates="conversas")
    messages: Mapped[list["Message"]] = relationship(back_populates="conversation")