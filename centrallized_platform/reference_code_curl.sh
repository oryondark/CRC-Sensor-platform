#must increase atomic number(index) manually
curl -XPUT https://ElasticSearch_Domain/index_name/_doc/1 -d '{"GroupID" : "999", "DeviceID" : "adfsdf", "Sensors": "Test","CollectedTime":"255"}' -H 'Content-Type: application/json'
#Automated increase atomic number(index)
curl -XPOST https://ElasticSearch_Domain/index_name/_doc/ -d '{"GroupID" : "999", "DeviceID" : "adfsdf", "Sensors": "Test","CollectedTime":"255"}' -H 'Content-Type: application/json'
#delete your index
curl -XDELETE https://ElasticSearch_Domain/index_name -H 'Content-Type: application/json'
