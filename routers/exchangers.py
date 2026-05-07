from fastapi import APIRouter, Depends, Query, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import desc, asc
from database import get_db
from models import Exchanger
from schemas import ExchangerResponse, ExchangerListResponse
from typing import Optional

router = APIRouter()

@router.get("/exchangers", response_model=ExchangerListResponse)
def get_exchangers(
    db: Session = Depends(get_db),
    limit: int = Query(20, ge=1, le=100),
    offset: int = Query(0, ge=0),
    min_rate: Optional[float] = None,
    min_reserve: Optional[float] = None,
    search: Optional[str] = None,
    sort_by: str = Query("rate", enum=["rate", "reserve", "reviews", "name"]),
    order: str = Query("desc", enum=["asc", "desc"])
):
    query = db.query(Exchanger)

    if min_rate:
        query = query.filter(Exchanger.rate >= min_rate)
    if min_reserve:
        query = query.filter(Exchanger.reserve >= min_reserve)
    if search:
        query = query.filter(Exchanger.name.ilike(f"%{search}%"))

    # Сортировка
    if sort_by == "name":
        order_column = Exchanger.name
    elif sort_by == "reserve":
        order_column = Exchanger.reserve
    elif sort_by == "reviews":
        order_column = Exchanger.reviews
    else:
        order_column = Exchanger.rate

    if order == "desc":
        query = query.order_by(desc(order_column))
    else:
        query = query.order_by(asc(order_column))

    total = query.count()
    items = query.offset(offset).limit(limit).all()

    return {"total": total, "items": items}


@router.get("/exchangers/{exchanger_id}", response_model=ExchangerResponse)
def get_exchanger(exchanger_id: int, db: Session = Depends(get_db)):
    exchanger = db.query(Exchanger).filter(Exchanger.id == exchanger_id).first()
    if not exchanger:
        raise HTTPException(status_code=404, detail="Обменник не найден")
    return exchanger


@router.get("/stats")
def get_stats(db: Session = Depends(get_db)):
    total = db.query(Exchanger).count()
    top_rate = db.query(Exchanger).order_by(desc(Exchanger.rate)).first()
    avg_reserve = db.query(Exchanger.reserve).all()

    return {
        "total_exchangers": total,
        "highest_rate": top_rate.name if top_rate else None,
        "highest_rate_value": top_rate.rate if top_rate else None
    }