#!/bin/sh

echo  "########## BUILDING ###################"

cd bin
zip costsaver.zip costsaver.py
cd ../

sam package --template-file template.yml --s3-bucket niro-source --output-template-file packaged.yml

echo  "########## DEPLOYING ###################"

sam deploy --template-file ./packaged.yml  --stack-name CostSaver  --capabilities CAPABILITY_IAM  --region ap-southeast-2
