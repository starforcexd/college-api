from fastapi import FastAPI , HTTPException
import json
import csv

app = FastAPI()

@app.get('/usr/get/hello')
def hello():
	return {'message': 'Hello World'}

@app.get('/usr/get/alldetails')
def get_all_details():
	with open('assets/output.json') as f:
		data = f.read()
		print(data)

@app.get('/usr/get/id/{id}')
def get_details_by_id(id: int):
	try:
		with open('assets/output.json') as file:
			data = json.load(file)
			for item in data:
				if item.get('id') == id:
					return item
	except FileNotFoundError:
		raise HTTPException(status_code=400, detail="file not found")
	except json.JSONDecodeError:
		raise HTTPException(status_code=400, detail="Json cannot be decoded")