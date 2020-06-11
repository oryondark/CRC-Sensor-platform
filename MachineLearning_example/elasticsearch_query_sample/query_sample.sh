
#Search for range of date
curl -X GET 'https://search-crc-es-awscloud-wft3afe5m7g2wcw2jmwk5.ap-northeast-2.es.amazonaws.com/climate/_search' -H 'Content-Type: application/json' -d
'{"query":
  {"range":
    {"date":
      {"gte":"now-3d/d", "lt":"now/d"}
    }
  }
}'
