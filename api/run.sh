virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
python3 db_init.py
flask run --host 0.0.0.0 --port 5000 --reload