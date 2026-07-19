# Build from the project root:
#   docker build -f backend/Dockerfile -t segmentation-backend .
# (context must be the project root, not backend/, so it can see data/ and models/)
FROM python:3.12-slim
WORKDIR /app
COPY backend/ ./backend/
COPY data/processed/rfm.csv ./data/processed/rfm.csv
COPY models/ ./models/
EXPOSE 8000
CMD ["uvicorn", "backend.main:app", "--host", "0.0.0.0", "--port", "8000" ]
