# devshutdown

The Solution will be using the following services :-
 - SAM --> To deploy all related resources to execute the lambda , This will include the function itself, execution roles/policies, Schedule Triggers to run the script based on a CRON expression

<h1>Deployment of the SAM template<h1>

Load AWS access into current terminal session

```
export AWS_PROFILE="<profilename>"
```

Running the following script will package the template resources and deploy them into the target account

```
./deploy.sh

```
<h1>Localised Testing<h1>

The function can be tested using the `sam local` offering by sam

Executing the following will create a  mock endpoint to test the function against

```
sam local start-lambda
```

Then you can invoke the function with something like the following

```
aws lambda invoke --function-name "CostSaver" --endpoint-url "http://127.0.0.1:3001" --no-verify-ssl out.txt --region ap-southeast-2 --payload "{\"action\":\"start\"}"

```

<h1>Improvements<h1>
The Alternative way of testing the lambda function against is the use of localstack. Most of the AWS service offerings are available

Configure aws profile override
```
aws configure --profile localstack
AWS Access Key ID: dummy
AWS Secret Access Key: dummy
Default region name [None]: us-east-1
Default output format [None]: json
```

Bring up local localstack

```
docker-compose up -d
```

using `awslocal` we can now mock most of the AWS offerings . once we have the  infrastructure mock'd and ready the exact same procedure can be used to create the function and related resources for testing 
