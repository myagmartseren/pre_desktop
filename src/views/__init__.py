from .login import LoginView
from .register import RegisterView
from .edit import EditView
from .home import HomeView
from .pop import PopView

VIEWS = {
    "login": LoginView,
    "home": HomeView,
    "register": RegisterView,
    "pop": PopView,
    "edit": EditView,
}
