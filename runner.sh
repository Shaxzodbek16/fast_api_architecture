#!/bin/bash

black .

echo "Black formatting done"

sleep 1

pip freeze > requirements.txt

echo "Requirements updated"

sleep 1

uvicorn app.server.app:create_app --reload
