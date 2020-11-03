from .index import index
from .homework import homework
from .account import account
from .contact import contact
from .signup import signup
from .logout import logout_view as logout
from .login import Login

login = Login.as_view()
