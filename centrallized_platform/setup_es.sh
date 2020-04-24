ElasticSearch_Domain=your_es_domain
ES_VERSION=es_version
TYPE=r5.large.elasticsearch
PROVISIONING=1


aws es create-elasticsearch-domain --domain-name $ElasticSearch_Domain \
--elasticsearch-version $ES_VERSION --elasticsearch-cluster-config  InstanceType=$TYPE,InstanceCount=$PROVISIONING \
--ebs-options EBSEnabled=true,VolumeType=standard,VolumeSize=15 --access-policies '{json form}'
