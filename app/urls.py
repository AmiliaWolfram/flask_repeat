from . import app
from .views import index, category_create, category_list, category_update, \
    item_create, item_update, item_delete, register, login, logout

# НЕ ВЫЗЫВАЕМ ФУНКЦИИ!!!!
app.add_url_rule('/', view_func=index)
app.add_url_rule('/item/create', view_func=item_create, methods=['GET', 'POST'])
app.add_url_rule('/item/<int:id>/update', view_func=item_update, methods=['GET', 'POST'])
app.add_url_rule('/item/<int:id>/delete', view_func=item_delete, methods=['GET', 'POST'])


app.add_url_rule('/category/create', view_func=category_create, methods=['GET', 'POST'])
app.add_url_rule('/category', view_func=category_list, endpoint='categories')
app.add_url_rule('/category/<int:id>/update', view_func=category_update, methods=['GET', 'POST'])

app.add_url_rule('/register', view_func=register, methods=['GET', 'POST'])
app.add_url_rule('/login', view_func=login, methods=['GET', 'POST'])
app.add_url_rule('/logout', view_func=logout)
