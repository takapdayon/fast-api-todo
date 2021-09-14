FROM python:3.9-buster

RUN pip install fastapi uvicorn
#COPY requirements.txt ./
#RUN pip install --no-cache-dir -r requirements.txt

COPY ./fastapi/app /app

EXPOSE 8000
#CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
CMD ["/bin/bash"]