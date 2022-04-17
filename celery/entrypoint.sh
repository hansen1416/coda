#!/bin/bash

# Start the first process
celery --app app.celery worker --loglevel=info &
  
# Start the second process
python3 /app/app.py &
  
# Wait for any process to exit
wait -n
  
# Exit with status of process that exited first
exit $?