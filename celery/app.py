from celery_app import task1
from flask import Flask, jsonify, url_for, redirect


# Your API definition
app = Flask(__name__)
app.config.from_object('config')


@app.route('/', methods=['POST'])
def longtask():
    task = task1.delay(10)
    return redirect(url_for('taskstatus', task_id=task.id))


@app.route('/status/<task_id>')
def taskstatus(task_id):
    task = task1.AsyncResult(task_id)
    if task.state == 'PENDING':

        response = {
            'queue_state': task.state,
            'status': 'Process is ongoing...',
            'status_update': url_for('taskstatus', task_id=task.id)
        }
    else:
        response = {
            'queue_state': task.state,
            'result': task.wait()
        }
    return jsonify(response)


if __name__ == '__main__':
    app.run()
