## Airgun Event Queue

### What does this lambda do ?

* This lambda reads from  a kinesis stream that holds generic events.
* It goes to a lookup table in dynamodb to find the queues that need to be affected.
* It then sends the payload to the correct queue based on the context.

### Pre-requisite
* Create the kinesis stream that you need to reference. Read about it [here](http://docs.aws.amazon.com/streams/latest/dev/learning-kinesis-module-one-create-stream.html).

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
  KINESIS_ARN: staging_kinesis_arn
```

```shell
$ pip install -r requirements.txt -t /path/to/serverless/project
$ getcreds staging
$ sls deploy -s staging
```
