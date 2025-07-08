from fastapi import APIRouter
from ..services.alphaVantage import get_stock_data


router = APIRouter()


@router.get("/ping")
def health_check():
    return {"status": "ok"}

@router.get("/analyze/{symbol}")
def analyze(symbol: str):
    try:
        data = get_stock_data(symbol)
        return data.tail(5).to_dict(orient="records")
    except Exception as e:
        return{"error": str(e)}