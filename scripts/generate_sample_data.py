import pandas as pd
import random
from datetime import datetime, timedelta

areas = [
    "Biloxi",
    "Ventura",
    "Rocío",
    "Emerald",
    "Packing Plant",
    "Field Operations",
    "Quality Control"
]

start_date = datetime(2026, 5, 20)

for i in range(7):

    current_date = start_date + timedelta(days=i)

    data = []

    for area in areas:

        # Campos productivos
        if area in ["Biloxi", "Ventura", "Rocío", "Emerald"]:

            projected_workers = random.randint(90, 160)

            actual_workers = projected_workers - random.randint(0, 12)

            kg_harvested = random.randint(4500, 9500)

        # Áreas operativas
        else:

            projected_workers = random.randint(15, 60)

            actual_workers = projected_workers - random.randint(0, 5)

            kg_harvested = 0

        attendance_rate = round(
            (actual_workers / projected_workers) * 100, 1
        )

        data.append({
            "date": current_date.strftime("%Y-%m-%d"),
            "area": area,
            "projected_workers": projected_workers,
            "actual_workers": actual_workers,
            "attendance_rate": attendance_rate,
            "kg_harvested": kg_harvested
        })

    df = pd.DataFrame(data)

    filename = (
        f"data/raw/workforce_projection_"
        f"{current_date.strftime('%Y%m%d')}.csv"
    )

    df.to_csv(filename, index=False)

print("Sample operational datasets created successfully.")