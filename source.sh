#!/bin/bash

AIRBYTE_URL="http://localhost:8000"

SOURCE_DEFINITION_ID="207704f0-22d2-44e5-b9bb-400725bcdda1"
WORKSPACE_ID="c182688c-e8ab-44d9-8f19-92ef141ca2b9"

curl -u airbyte:password \
     -X POST "$AIRBYTE_URL/api/v1/sources/create" \
     -H "Content-Type: application/json" \
     -d '{
           "sourceDefinitionId": "'"$SOURCE_DEFINITION_ID"'",
           "workspaceId": "'"$WORKSPACE_ID"'",
           "name": "My Source",
           "connectionConfiguration": {
             "endpoint": "https://exnaton-public-s3-bucket20230329123331528000000001.s3.eu-central-1.amazonaws.com/challenge/95ce3367-cbce-4a4d-bbe3-da082831d7bd.json"
           }
         }'
