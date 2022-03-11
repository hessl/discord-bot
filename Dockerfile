FROM python:3-alpine
WORKDIR /usr/src/app

# Copy and install our required libraries
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy our bot token and files
COPY token.txt ./
COPY main.py ./

# Default command run main.py to start bot
CMD [ "python", "./main.py" ]