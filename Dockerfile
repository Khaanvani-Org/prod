FROM python:3.11.2-slim-buster AS prod

WORKDIR /app

# Copy everything from the local 'td' directory to the '/app' directory in the container
COPY . /app


# Install other Python dependencies from requirements.txt if present
RUN if [ -f "requirements.txt" ]; then pip install --no-cache-dir -r requirements.txt; fi

EXPOSE 3001

CMD ["streamlit", "run", "main.py" "--server.port" "3001"]
