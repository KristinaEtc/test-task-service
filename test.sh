#!/bin/bash

#curl http://127.0.0.1:8000/tasks/
#curl -X POST http://127.0.0.1:8000/tasks/ -d '{"title":"curlTst3!", "description": "blabla", "due_date": ""2017-03-18"}' -H "Content-Type: application/json"}
#curl http://127.0.0.1:8000/task/1/


curl -X GET http://127.0.0.1:8000/task/get-all/
curl -X POST http://127.0.0.1:8000/task/add/ -d '{"project": {"title": "pr", "description":"pr_des"}, "title":"ProjectTT", "description":"new desc", "due_date":"2017-03-21"}'
curl -X GET http://127.0.0.1:8000/task/get-by-id/2/

curl http://127.0.0.1:8000/project/get-all/
curl -X POST http://127.0.0.1:8000/task/add/ -d '{"project": {"title": "pr23","description": "pr_des2"},"title": "ProjectTT","description": "new desc","due_date": "2017-03-21"}'
curl -X POST http://127.0.0.1:8000/task/add/ -d '{"project": {"title": "pr23","description": "pr_des2"},"title": "ProjectTT","description": "new desc","due_date": "2017-03-21"}'
