# Start with alpine python image variant for minimized image size
FROM python:3-alpine
WORKDIR /usr/src/app

# Copy and install our required libraries
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copy our bot token and files
COPY token.txt ./
COPY ./bot bot

# Default command run main.py to start bot
CMD [ "python", "./bot/main.py" ]