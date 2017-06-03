import sys, os, os.path
from flask import Flask, render_template


app = Flask(__name__)


@app.route('/')
def debug_info():
    environment = []
    for k in os.environ.keys():
        environment.append({
            'key':k,
            'value':os.environ.get(k)})
    sys_path = []
    for x in sys.path:
        sys_path.append(x)
    ls_pwd = os.listdir(os.path.dirname(__file__))

    return render_template(
        'index.html',
        environment=environment,
        sys_path=sys_path,
        this_file=__file__,
        ls_pwd=ls_pwd), 200


if __name__ == '__main__':
    app.run(debug=True)
