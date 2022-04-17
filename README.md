To run the project `./start.sh`

The web UI is at http://localhost:3000

API is a Flask behind an Nginx

Celery is integrated with another Flask webserver, it's only an example, which is called in /thread/add to process a long task

## Auth 

Register and login via JWT

When visit /home, fetch a new token via refresh token

The first user (id=1), is the default Superuser, who can sort Board and edit user permission
## Board

There is a board list at /home

A login user can create board

The board admin can edit board, superuser can sort board

Board admin can invite another user, grant him/her mod permission when accepted the invitation

## Thread

There is a thread list at board front page

A login user can post a new thread

The thread author, board admin and mod can edit/delete thread

## Post

A login user can post a new post under a thread

The thread author, board admin and mod can edit/delete post