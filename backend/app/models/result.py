from pydantic import BaseModel
from typing import List, Any


class ChartData(BaseModel):
    type: str
    labels: List[str]
    data: List[float]
    backgroundColor: List[str]


class TableData(BaseModel):
    headers: List[str]
    rows: List[List[str]]


class QueryResponse(BaseModel):
    text: str
    chart: ChartData
    table: TableData
