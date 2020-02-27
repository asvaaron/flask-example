# Python Flask Example

## Start Server 

```bash 
$ python app.py
```

## Client Requests


Make request to the Get Endpoint 

```bash 
curl --location --request GET 'localhost:5000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
	"lala": 15
}'
```


Make request to the Post Endpoint


```bash 
$ curl --location --request POST 'localhost:5000/predict' \
--header 'Content-Type: application/json' \
--data-raw '{
	"lala": 15
}'
```