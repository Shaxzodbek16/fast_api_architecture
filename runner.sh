#!/bin/bash

export PYTHONPATH=/Users/shaxzodbek/Developer/PDPEcosystem/PDPUniversity/2-kurs/1-semestr/Programming/fastapi/fast_4_models


uvicorn app.server.app:create_app --reload --host 0.0.0.0 --port 8000
