from fastapi import APIRouter, HTTPException
from backend.app.models.query import QueryRequest
from backend.app.models.result import QueryResponse, ChartData, TableData
from backend.app.services.query_parser import classify_query
from backend.app.services.analyzer import analyze_payment_method, analyze_region

router = APIRouter()

# Словарь, связывающий тип запроса с функцией-аналитиком
analyzers = {
    "payment_method": analyze_payment_method,
    "region": analyze_region,
    # Добавлять можно дополнительные функции, например:
    # "experience": analyze_experience,
    # "skill": analyze_skill,
    # "gender": analyze_gender,
}

@router.post("/analyze", response_model=QueryResponse)
def analyze_query(query: QueryRequest):
    query_type = classify_query(query.question)
    print(f">>> 📌 Detected query type: {query_type}")

    if query_type in analyzers:
        result = analyzers[query_type]()
    else:
        detail = ("Не удалось понять тип запроса. Поддерживаются: "
                  "платежи, регионы, опыт, скиллы, гендер.")
        raise HTTPException(status_code=400, detail=detail)

    return QueryResponse(
        text=result["text"],
        chart=ChartData(**result["chart"]),
        table=TableData(**result["table"])
    )
