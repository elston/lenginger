import traceback

# ...app
from flask import Flask
app = Flask(__name__)


# ...config
import config
config.init_app(app)



# ...
from flask import (
    request,
    url_for,
    redirect,
    flash,
    render_template,
)


# ...500
@app.errorhandler(500)
def errorhandler(_):
    app.logger.error(traceback.format_exc())
    return 'Internal Server Error', 500

# ..404
@app.errorhandler(404)
def page_not_found(_):
    flash(u'Запрошенная страница %s не существует' % request.url, 'error')
    return redirect(url_for('index'))



# ..index
@app.route('/')
def index():
    # ..
    context = {}
    # ..
    return render_template('index.html'
        , **context
    )




# print app.url_map    