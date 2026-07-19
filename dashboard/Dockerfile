# Build from the project root:
#   docker build -f dashboard/Dockerfile -t segmentation-dashboard .
# (context must be the project root so requirements-frontend.txt is visible)

FROM python:3.12-slim
WORKDIR /app

COPY requirements-frontend.txt .
RUN pip install --no-cache-dir -r requirements-frontend.txt
 
COPY dashboard/ ./dashboard/
EXPOSE 8501
CMD [ "streamlit","run","dashboard/app.py","--server.port=8501","--server.address=0.0.0.0" ]