from fastapi import FastAPI
import uvicorn
import requests

app = FastAPI()

@app.get("/deneme")
def index():
	return "denemiyor"


@app.get("/dene")
def mindex():
	try:
		response = requests.get("http://dev_web/test")
	except:
		return("ERROR CONNECTINNN")

	return response.text


if __name__ == "__main__":
	uvicorn.run(app, port=8000, host='0.0.0.0')
