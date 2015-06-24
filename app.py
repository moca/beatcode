from bottle import route, run

@route('/')
def index():
    return "There will be dragons"


if  __name__ == "__main__":
    run(host='0.0.0.0', port=8000)