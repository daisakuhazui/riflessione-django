#!/bin/bash
set -a

if [ ! -f ".env" ]; then
  echo "'.env' file not found."
  exit 1
fi

source .env

$(aws ecr get-login --region ap-northeast-1 --no-include-email)

LOGIN_RETURN_CD=$?
if [ $LOGIN_RETURN_CD -ne 0 ]; then
  echo "AWS ECR login failed."
  echo "Please check your AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY and try again."
  echo "RETURN_CD: ${LOGIN_RETURN_CD}"
  exit ${LOGIN_RETURN_CD}
fi

cd docker/nginx/

docker build -f ./Dockerfile_fargate -t nginx .
RETURN_CD=$?

if [ $RETURN_CD -ne 0 ]; then
	echo "RETURN_CD: ${RETURN_CD}"
	exit ${RETURN_CD}
else
	echo ""
	echo "docker nginx build done."
	echo ""
	echo "pushing image to ECR."
	docker tag nginx:latest ${ECR_NGINX_REPO}:latest
	docker push ${ECR_NGINX_REPO}:latest
	echo ""
	echo "docker nginx push done."
fi
