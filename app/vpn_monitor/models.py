from sqlalchemy import Column, Integer, String, DateTime, Text, Enum as SQLEnum
from sqlalchemy.orm import DeclarativeBase
import enum
from datetime import datetime

class Base(DeclarativeBase):
    pass


class VPNEventType(str, enum.Enum):
    CONNECT = "connect"
    DISCONNECT = "disconnect"
    ERROR = "error"

class VPNEvent(Base):
    __tablename__ = "vpn_events"

    id = Column(Integer, primary_key=True, autoincrement=True)
    timestamp = Column(DateTime, default=datetime.utcnow, nullable=False)
    username = Column(String(100), nullable=False)
    event_type = Column(VPNEventType, nullable=False)
    vpn_type = Column(String(50), nullable=False)
    ip_address = Column(String(45), nullable=True)
    details = Column(Text, nullable=True)

    def __repr__(self):
        return f"<VPNEvent {self.event_type.value} - {self.username} at {self.timestamp}>"