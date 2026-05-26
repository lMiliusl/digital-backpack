from pydantic import BaseModel
from datetime import datetime
from vpn_monitor.models import VPNEventType

class VPNEventSchema(BaseModel):
    id: int
    timestamp: datetime
    username: str
    event_type: VPNEventType
    vpn_type: str
    ip_address: str | None
    details: str | None

    model_config = {
        "from_attributes": True
    }