#!/bin/bash

PROJECT_PREFIX=riflessione
APP_IMAGE=app

docker tag ${APP_IMAGE}:latest ${ECR_REPO}:${PROJECT_PREFIX}-${CIRCLE_SHA1}
docker push ${ECR_REPO}:${PROJECT_PREFIX}-${CIRCLE_SHA1}

if [ ${CIRCLE_BRANCH} == "master" ]; then
  docker tag ${APP_IMAGE} ${ECR_REPO}:stg-latest
  docker push ${ECR_REPO}:stg-latest
  echo "STAGING build done and running ecsdeploy..."
  ./scripts/ecs-deploy --timeout ${ECS_TIMEOUT} -c ${STG_ECS_CLUSTER} -n ${STG_ECS_SERVICE} -i ${ECR_REPO}:${PROJECT_PREFIX}-${CIRCLE_SHA1}
elif [ ${CIRCLE_BRANCH} == "release" ]; then
  docker tag ${APP_IMAGE} ${ECR_REPO}:latest
  docker push ${ECR_REPO}:latest
  echo "PRODUCTION build done and running ecsdeploy..."
  ./scripts/ecs-deploy --timeout ${ECS_TIMEOUT} -c ${PRD_ECS_CLUSTER} -n ${PRD_ECS_SERVICE} -i ${ECR_REPO}:${PROJECT_PREFIX}-${CIRCLE_SHA1}
fi

RETURNCD=$?
if [ ${RETURNCD} -ne 0 ]; then
  echo
  echo "ECS DEPLOY FAILED"
  echo
  exit ${RETURNCD}
fi

exit 0
