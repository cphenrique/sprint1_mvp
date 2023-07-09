@echo off

REM Create a virtual environment
python -m venv env

REM Activate the virtual environment
call env\Scripts\activate

REM Install required dependencies
pip install -r requirements.txt

REM Run the Python db_init.py script
python3 db_init.py

REM Run flask server on localhost
flask run --host 0.0.0.0 --port 5000 --reload