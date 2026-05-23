# Operational Workforce Data Pipeline

## Project Overview

This project simulates an operational workforce monitoring pipeline for agricultural operations using Python and Power BI-oriented datasets.

The objective is to automate the ingestion, validation, transformation, and reporting of workforce operational data across multiple production areas.

The pipeline was designed to simulate real operational workflows commonly found in agro-industrial environments.

---

# Technologies Used

- Python
- Pandas
- VS Code
- Git & GitHub
- CSV datasets
- Power BI (next phase)

---

# Project Architecture

```text
Raw Operational Data
        ↓
Data Consolidation
        ↓
Operational Validation
        ↓
KPI Generation
        ↓
Anomaly Detection
        ↓
Final Dataset for BI
```

---

# Pipeline Components

## 1. Sample Data Generation
Generates simulated operational workforce datasets for multiple agricultural areas.

### Output
```text
data/raw/
```

---

## 2. Data Consolidation
Combines multiple operational CSV files into a centralized dataset.

### Script
```text
consolidate_workforce_data.py
```

---

## 3. Operational Validation
Detects:
- attendance risks
- workforce gaps
- operational inconsistencies

### Output
```text
validated_workforce_data.csv
```

---

## 4. KPI Generation
Creates executive operational KPIs including:
- attendance rate
- workforce gap
- projected vs actual workers
- harvest metrics

---

## 5. Anomaly Detection
Automatically identifies operational anomalies such as:
- low attendance
- critical staffing gaps
- low productivity scenarios

---

## 6. Final Dataset Creation
Builds a clean dataset optimized for Business Intelligence and dashboarding workflows.

### Final Output
```text
data/final/final_operational_dataset.csv
```

---

# Example Operational Metrics

- Attendance Rate
- Workforce Gap
- KG Harvested
- KG per Worker
- Operational Risk Status

---

# Future Improvements

- Power BI dashboard integration
- SQL database integration
- Automated scheduling
- Cloud deployment
- Email alert automation
- API-based ingestion

---

# Author

Andrea Meroussis Puglisevich

Automation & Data Operations Analyst  
Building toward Data Engineering

[LinkedIn](https://www.linkedin.com/in/andreameroussis/)