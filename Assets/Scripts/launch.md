psql -U postgres
teoh0628
\dt
\pset pager off
\x

cd GameWebAPI
python -m uvicorn app.main:app --reload