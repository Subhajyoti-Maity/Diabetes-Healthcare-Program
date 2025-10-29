# DHCP - Diabetes Health Care Programme

DHCP or Diabetes Health Care Programme is an integrated healthcare application focused on Diabetes and its health implications. Unlike normal detection or prediction software, DHCP uses Generative AI (Gemini) which produces responses and data in real time. What more? You get a completely interactive and real-time chatbot named Capsule. You have any doubts regarding symptoms, medical dosage, health implications, side effects or anything that comes to your mind, Capsule will answer you tirelessly.

## Tech Used:
- Python (3.12 or higher)
- Streamlit
- React JS
- Cron JOB
- Gemini AI API

## Modules:
- Home Page
- Ask Query
- Diagnosis

# Diabetes Healthcare Programme

Small, focused README with quickstart and project layout.

Quickstart (Windows / PowerShell)

1. Create & activate venv:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
pip install -r requirements.txt
```

3. Required files

- `diabetes.csv` — place in the project root (same folder as `main.py`).
- `images/` — optional UI images (keep if you have assets).

Run

```powershell
.\.venv\Scripts\python.exe -m streamlit run .\main.py
```

Open http://localhost:8501

Project structure

```
Diabetes-Healthcare-Programme-main/
├─ main.py                # Streamlit entrypoint
├─ web_functions.py       # data loader & model logic
├─ diabetes.csv           # (not committed) dataset - place here
├─ requirements.txt
├─ README.md
├─ images/                # optional image assets (diabetic.png, capsule.png, ...)
└─ Tabs/
	├─ __init__.py
	├─ home.py
	├─ diagnosis.py
	├─ result.py
	├─ talk2doc.py
	└─ kc.py
```

Security

- Do NOT commit API keys or service-account JSON to source control.
- For production, prefer service accounts or a secrets manager and restrict/rotate keys.

Files of interest

- `main.py` — app entry
- `web_functions.py` — data/model
- `Tabs/` — UI pages

Troubleshooting (short)

- Missing `diabetes.csv`: ensure file is present in project root.
- Missing images: ensure `images/` contains referenced PNGs.
- Port 8501 in use: stop the occupying process or run Streamlit with `--server.port 8502`.

If you want this README adjusted further (shorter/longer or to include deploy steps), tell me which sections to keep.


