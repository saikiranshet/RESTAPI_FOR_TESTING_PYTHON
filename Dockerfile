FROM python:latest

WORKDIR /usr/app/src

COPY . /usr/app/src/

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python","-m","pytest","-vs","test_free_api.py","--html=reports/report.html"]
