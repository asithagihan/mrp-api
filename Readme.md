# full-stack-python

python3 -m pip install --user --upgrade pip
python3 -m pip --version
python3 -m pip install --user virtualenv
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

Run API
cd api
uvicorn main:app --reload
