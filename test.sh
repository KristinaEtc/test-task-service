#!/bin/bash

curl http://127.0.0.1:8000/tasks/
curl -X POST http://127.0.0.1:8000/tasks/ -d '{"title":"curlTst3!", "description": "blabla", "due_date": ""2017-03-18"}' -H "Content-Type: application/json"}

curl http://127.0.0.1:8000/task/1/
