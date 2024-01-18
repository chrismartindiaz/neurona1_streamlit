FROM python:3.8
RUN pip install streamlit
COPY src/app.py /app/
COPY src/neurona.jpg /app/
WORKDIR /app
ENTRYPOINT [ "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0" ]