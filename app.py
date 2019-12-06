from flask import Flask, render_template, request
from os import path

app = Flask(__name__)
tasks = ["eat", "sleep", "have fun", "learn", "grow", "code", "compete", "dream", "travel", "help"]


@app.route('/')
def render_main_page():
    return render_template('main.html')


@app.route('/my-todo-list', methods=['GET', 'POST'])
def add_new_task():
    return render_template("todo_list.html",
                           name=request.form.get("name"))


@app.route('/result', methods=['GET', 'POST'])
def show_updated_todo_list():
    new_task = request.form.get("new_task")
    tasks.append(new_task)
    return render_template("result.html",
                           tasks=tasks)


if __name__ == '__main__':
    app.run(
        debug=True,
        # this option enables auto-reloading of your application when code is changes

        extra_files=[path.join(app.root_path, app.template_folder, 'main.html')],
        # Alternative to debug option; enabling auto-reload for specific files only.
        # A smarter way to use this option described here: http://xion.io/tag/flask-script.html

        host='0.0.0.0',
        # IP address of your web-server
        # default: 127.0.0.1

        port=3000
        # Port number - identifies the communication endpoint for your server (used by TCP to find this program)
        # default: 5000
    )


# You can also set all these flags manually, when starting the application from command line:
# flask run --host=0.0.0.0 --port=3000 ...
