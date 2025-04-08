import pandas as pd
from backend.app.utils.loader import load_dataset


def analyze_payment_method() -> dict:
    df = load_dataset()
    # Пример анализа
    crypto_df = df[df["payment_method"] == "cryptocurrency"]
    traditional_df = df[df["payment_method"] != "cryptocurrency"]
    
    avg_crypto = crypto_df["annual_income"].mean()
    avg_trad = traditional_df["annual_income"].mean()
    
    diff_percent = round((avg_crypto - avg_trad) / avg_trad * 100, 2)
    
    return {
        "text": f"Фрилансеры, принимающие оплату в криптовалюте, зарабатывают в среднем на {diff_percent}% больше.",
        "chart": {
            "type": "bar",
            "labels": ["Cryptocurrency", "Traditional"],
            "data": [avg_crypto, avg_trad],
            "backgroundColor": ["#6c5ce7", "#a29bfe"]
        },
        "table": {
            "headers": ["Payment Method", "Average Income"],
            "rows": [
                ["Cryptocurrency", f"${avg_crypto:,.0f}"],
                ["Traditional", f"${avg_trad:,.0f}"],
                ["Difference", f"+{diff_percent}%"]
            ]
        }
    }


def analyze_region() -> dict:
    df = load_dataset()

    region_stats = df.groupby("region")["annual_income"].agg(["mean", "median"]).sort_values("mean", ascending=False).head(8)

    labels = region_stats.index.tolist()
    avg_incomes = region_stats["mean"].round(2).tolist()
    medians = region_stats["median"].round(2).tolist()

    rows = [
        [region, f"${avg:,.0f}", f"${med:,.0f}"]
        for region, avg, med in zip(labels, avg_incomes, medians)
    ]

    return {
        "text": "Средний доход фрилансеров по регионам. Наибольший доход — в " + labels[0],
        "chart": {
            "type": "bar",
            "labels": labels,
            "data": avg_incomes,
            "backgroundColor": ["#6c5ce7"] * len(labels)
        },
        "table": {
            "headers": ["Регион", "Средний доход", "Медианный доход"],
            "rows": rows
        }
    }


def analyze_experience() -> dict:
    df = load_dataset()
    experts = df[df["experience_level"] == "expert"]
    under_100 = experts[experts["project_count"] < 100]
    percent = round(len(under_100) / len(experts) * 100, 2) if len(experts) > 0 else 0

    return {
        "text": f"Около {percent}% экспертов выполнили менее 100 проектов.",
        "chart": {
            "type": "doughnut",
            "labels": ["<100 проектов", "≥100 проектов"],
            "data": [percent, 100 - percent],
            "backgroundColor": ["#6c5ce7", "#a29bfe"]
        },
        "table": {
            "headers": ["Категория", "Процент"],
            "rows": [
                ["<100 проектов", f"{percent}%"],
                ["≥100 проектов", f"{100 - percent}%"]
            ]
        }
    }


def analyze_skill() -> dict:
    df = load_dataset()
    skill_stats = df.groupby("skill")["annual_income"].mean().sort_values(ascending=False).head(5)
    labels = skill_stats.index.tolist()
    avg_incomes = skill_stats.round(2).tolist()

    rows = [
        [skill, f"${income:,.0f}"]
        for skill, income in zip(labels, avg_incomes)
    ]

    return {
        "text": "Навыки с наивысшим средним доходом среди фрилансеров.",
        "chart": {
            "type": "bar",
            "labels": labels,
            "data": avg_incomes,
            "backgroundColor": ["#6c5ce7"] * len(labels)
        },
        "table": {
            "headers": ["Навык", "Средний доход"],
            "rows": rows
        }
    }


def analyze_gender() -> dict:
    df = load_dataset()
    gender_stats = df.groupby("gender")["annual_income"].mean().sort_values(ascending=False)
    labels = gender_stats.index.tolist()
    avg_incomes = gender_stats.round(2).tolist()

    rows = [
        [gender, f"${income:,.0f}"]
        for gender, income in zip(labels, avg_incomes)
    ]

    return {
        "text": "Средний доход фрилансеров по гендерному признаку.",
        "chart": {
            "type": "bar",
            "labels": labels,
            "data": avg_incomes,
            "backgroundColor": ["#6c5ce7"] * len(labels)
        },
        "table": {
            "headers": ["Гендер", "Средний доход"],
            "rows": rows
        }
    }

