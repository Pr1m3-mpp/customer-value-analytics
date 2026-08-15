**P0-1 Local Development Environment Check** — PASS



Date: 2026-08-08



Environment:

\- OS: Windows

\- Conda environment: clv-analytics

\- Python: 3.12.13

\- Python path:

&#x20; D:\\Users\\mpp\\Software\\anaconda3\\envs\\clv-analytics\\python.exe

\- Git: 2.55.0.windows.3

\- Cursor: 3.15.6 x64



Result:

Project-specific Python 3.12 environment was successfully

created, activated and verified.



Status: PASS



\----------------------------------------------------------------------------------------------------------

**P0-2 GitHub Repository Setup** — PASS



Date: 2026-08-09



Repository:

\- Owner: Pr1m3-mpp

\- Repository: customer-value-analytics

\- Visibility: Public

\- Default branch: main

\- README: Initialized

\- .gitignore: Python

\- License: None



Description:

Customer lifetime value prediction and marketing attribution analytics

using SQL, probabilistic modeling, machine learning, and Power BI.



Result:

Public GitHub repository was successfully created and initialized

with README.md and Python .gitignore.



Status: PASS



\----------------------------------------------------------------------------------------------------------

**P0-3 Local Project Directory Setup** — PASS



Date: 2026-08-14



Local Repository:

\* Project folder: `customer-value-analytics`

\* Local path: `C:\\Users\\mpp\\Desktop\\customer-value-analytics`

\* Remote repository: `Pr1m3-mpp/customer-value-analytics`

\* Branch: `main`



Initial Project Structure:

```text

customer-value-analytics/

├── README.md

├── .gitignore

├── sql/

├── notebooks/

├── src/

├── dashboard/

├── reports/

├── docs/

└── data/

&#x20;   ├── raw/

&#x20;   │   └── .gitkeep

&#x20;   └── processed/

&#x20;       └── .gitkeep

```



Data Rules:

\- `data/raw/\*` and `data/processed/\*` are ignored by Git.

\- `.gitkeep` files remain trackable to preserve the directory structure.

\- Ignore rules were verified successfully using temporary test CSV files.



Result:

Local repository, minimum project structure, and CLV-specific data ignore rules were successfully created and verified.



Status: PASS



\----------------------------------------------------------------------------------------------------------

**P0-Reset Project Scope Reset** — PASS



Date: 2026-08-14



Scope:

\- The original extended CLV + marketing attribution plan was deprecated.

\- The project scope was refocused on:
  UCI Online Retail → SQL → RFM → BG/NBD + Gamma-Gamma → 90-day revenue-based CLV → Power BI → GitHub → Resume/Interview.

\- BigQuery, Google Analytics, LightGBM, SHAP, Markov attribution, Streamlit, and other non-essential components were removed.

\- Existing Conda environment, GitHub repository, and local project structure were retained.



Result:

Project scope was successfully refined and is ready for execution.



Status: PASS



\----------------------------------------------------------------------------------------------------------

**Customer Data Preparation, SQL & RFM** — PASS



Date: 2026-08-15



Outputs:

\* Cleaned UCI Online Retail transaction data.

\* Completed three SQL analyses for transaction validation, customer RFM, and business KPIs.

\* Built four customer segments: Champions, Loyal Customers, At Risk, and Others.

\* Generated reusable Python scripts for data preparation, SQL execution, and RFM segmentation.



Key Results:

\- Customers: 4,338

\- Orders: 18,532

\- Revenue: 8,911,407.90

\- Average Order Value: 480.87

\- Repeat Customers: 2,845

\- Repeat Purchase Rate: 65.58%



Result:

Customer-level RFM features, business KPIs, and customer segmentation were successfully generated and validated.



Status: PASS