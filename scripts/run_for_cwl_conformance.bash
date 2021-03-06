#!/bin/bash

set +e

: ${GALAXY_BOOTSTRAP_DATABASE_CONTAINER:="gxpostgres"}
: ${GALAXY_BOOTSTRAP_DATABASE_PASSWORD:="mysecretpassword"}
: ${GALAXY_BOOTSTRAP_DATABASE_NAME:="galaxy"}
: ${GALAXY_BOOTSTRAP_DATABASE:=1}
: ${GALAXY_PORT:=8080}
: ${POSTGRES_PORT:=5432}

if [ $GALAXY_BOOTSTRAP_DATABASE -eq 1 ]; then
	docker stop "${GALAXY_BOOTSTRAP_DATABASE_CONTAINER}" || /bin/true
	docker rm "${GALAXY_BOOTSTRAP_DATABASE_CONTAINER}" || /bin/true
	docker run -p "${POSTGRES_PORT}:${POSTGRES_PORT}" --name "${GALAXY_BOOTSTRAP_DATABASE_CONTAINER}" -e POSTGRES_PASSWORD="${GALAXY_BOOTSTRAP_DATABASE_PASSWORD}" -d postgres
fi

export GALAXY_SKIP_CLIENT_BUILD=1
export GALAXY_PID="cwl.pid"
export GALAXY_CONFIG_OVERRIDE_MASTER_API_KEY=testmasterapikey
export GALAXY_CONFIG_OVERRIDE_DATABASE_CONNECTION="postgres://postgres:${GALAXY_BOOTSTRAP_DATABASE_PASSWORD}@localhost:${POSTGRES_PORT}/${GALAXY_BOOTSTRAP_DATABASE_NAME}"
export GALAXY_CONFIG_OVERRIDE_DATABASE_AUTO_MIGRATE="true"
export GALAXY_CONFIG_OVERRIDE_ALLOW_PATH_PASTE="true"
export GALAXY_CONFIG_OVERRIDE_ADMIN_USERS="cwluser@example.com"

export GALAXY_CONFIG_OVERRIDE_ENABLE_BETA_WORKFLOW_MODULES="true"
export GALAXY_CONFIG_OVERRIDE_ENABLE_BETA_WORKFLOW_FORMAT="true"
export GALAXY_CONFIG_OVERRIDE_ENABLE_BETA_TOOL_FORMATS="true"
export GALAXY_CONFIG_OVERRIDE_CHECK_UPLOAD_CONTENT="false"
export GALAXY_CONFIG_OVERRIDE_STRICT_CWL_VALIDATION="false"

export GALAXY_PORT

./run.sh --daemon

export GALAXY_TEST_EXTERNAL="http://localhost:$GALAXY_PORT/"
while ! curl -s "${GALAXY_TEST_EXTERNAL}api/version";
do
    printf "."
    sleep 4;
done;
