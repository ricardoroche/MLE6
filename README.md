# Containerized Sentiment Analyzer

## Instructions

1. Build docker image:

```
docker build -t <image_name>
```

2. Run docker container:

```
docker run --rm -dp 8000:8000 <image_name>
```

3. Open application in browser: `http://127.0.0.1:8000`

4. Submit a query string for sentiment analysis by navigating to the `endpoint` endpoint and clicking on the 'Test it out' button.
