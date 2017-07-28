## Airgun Create User in Elasticsearch

### What does this lambda do ?

* This lambda reads from  a kinesis stream that holds records that need to be pushed to Elasticsearch
* Creates a new record in Elasticsearch.

### Pre-requisite
* Create the kinesis stream that you need to reference.
* make sure you have full Elasticsearch url with you.

### Running specs

```shell
$ python -m unittest discover -s spec -p "*_spec.py"
```

### Deployment Instructions

In order to prepare for deployment, first copy the environment file.

```shell
$ cp serverless.example.env.yml serverless.env.yml
```

Change the values in serverless.env.yml based on the environment.

```yml
staging:
  ELASTICSEARCH_URL: elasticsearch_staging_url
  KINESIS_ARN: staging_kinesis_arn
```

```shell
$ pip install -r requirements.txt -t /path/to/serverless/project
$ getcreds staging
$ sls deploy -s staging
```
