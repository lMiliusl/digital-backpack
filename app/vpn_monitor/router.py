from fastapi import APIRouter, Depends, Query
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from typing import List

from core.database import get_db
from vpn_monitor.models import VPNEvent
from vpn_monitor.schemas import VPNEventSchema

router = APIRouter(
    prefix="/api/vpn",
    tags=["VPN Monitor"]
)

@router.get("/events", response_model=List[VPNEventSchema])
async def get_events(
    limit: int = Query(default=50, le=100),
    offset: int = Query(default=0, ge=0),
    db: AsyncSession = Depends(get_db),
):
    #Получение списка VPN-Событий
    result = await db.execute(
        select(VPNEvent)
        .order_by(VPNEvent.timestamp.desc())
        .limit(limit)
        .offset(offset)
    )
    events = result.scalar().all()
    return events


@router.get("/events/{event_id}", response_model=VPNEventSchema)
async def get_event(event_id: int, db: AsyncSession = Depends(get_db)):
    result = await db.execute(
        select(VPNEvent).where(VPNEvent.id == event_id)
    )
    event = result.scalar_one_or_none()
    if event is None:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Событие не найдено")
    return event