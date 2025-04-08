def classify_query(question: str) -> str:
    """
    Простая классификация запроса — вернёт тип анализа.
    Поддерживает ключевые слова на английском и русском языках.
    """
    q = question.lower()
    
    if any(word in q for word in ["cryptocurrency", "crypto", "bitcoin", "ethereum"]):
        return "payment_method"
    elif any(word in q for word in [
        "region", "regions", "country", "countries", "location", "locations",
        "continent", "area", "geography",
        "зарплата", "доход", "страна", "регионы", "регион", "польша", "польше"
    ]):
        return "region"
    elif any(word in q for word in ["expert", "experience", "project", "projects", "level", "seniority"]):
        return "experience"
    elif any(word in q for word in ["skill", "skills", "technology", "stack", "tools", "framework", "premium"]):
        return "skill"
    elif any(word in q for word in ["gender", "male", "female", "non-binary", "men", "women"]):
        return "gender"
    else:
        print("Unrecognized query:", q)  # DEBUG
        return "unknown"

