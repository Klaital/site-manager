test:
	python3 -m unittest discover --pattern "tc_*.py"

zip:
	zip vita_apis.zip functions/*.py models/*.py

publish: zip
	aws lambda update-function-code --function-name vita-api-lambda --zip-file fileb://vita_apis.zip

clean:
	rm -f vita_apis.zip
