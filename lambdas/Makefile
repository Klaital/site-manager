.PHONY: test publish zips clean

test:
	python3 -m unittest discover --pattern "tc_*.py"

vita_apis.zip: functions/api_handler.py models/site.py models/user.py models/session.py
	zip $@ $^

site_json_compiler.zip: functions/site_content_compiler.py models/site.py
	zip $@ $^

zips: vita_apis.zip site_json_compiler.zip

publish: zips
	aws lambda update-function-code --function-name vita-api-lambda --zip-file fileb://vita_apis.zip
	aws lambda update-function-code --function-name vita-site-json-lambda --zip-file fileb://site_json_compiler.zip

clean:
	rm -f *.zip
