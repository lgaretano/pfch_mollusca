import requests, json

#Ask for a search results for shells-BHL limits 10 per page, so we added page size
payload = {'q': 'mollusca', 'api_key': '3a5c7bc4-91c3-4184-91ca-56c657a00933', 'page_size':10}
r = requests.get('http://www.biodiversitylibrary.org/api2/httpquery.ashx?op=SubjectSearch&subject=mollusca&apikey=3a5c7bc4-91c3-4184-91ca-56c657a00933')

print(r.status_code)

print(r.text)

#trun it into a python dictonary

data = json.loads(r.text)

for doc in data['docs']:

	print(json.dumps(doc,indent=2))
	#above makes it "print pretty" and indented