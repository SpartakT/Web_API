from pydantic import BaseModel
from typing import Optional, List

class ExchangerResponse(BaseModel):
    id: int
    name: str
    rate: float
    reserve: float
    reviews: int
    min_btc: float
    max_btc: float

    class Config:
        from_attributes = True


class ExchangerListResponse(BaseModel):
    total: int
    items: List[ExchangerResponse]