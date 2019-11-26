from .. import app

@app.template_filter('format_date')
def format_date(value):
    return value.strftime('%d/%m/%Y')