
import SEP_Login
import SEP_Product_List_Page

class widgetConstructor(object):
    def __init__(self, fileName):
        import sys

        if (fileName == 'SEP_Login.py'):
            app = SEP_Login.QtWidgets.QApplication(sys.argv)
            LoginForm = SEP_Login.QtWidgets.QWidget()
            ui = SEP_Login.Ui_LoginForm()
            ui.setupUi(LoginForm)
            LoginForm.show()

            sys.exit(app.exec_())

        elif (fileName == 'SEP_Product_List_Page.py'):
            app = SEP_Product_List_Page.QtWidgets.QApplication(sys.argv)
            UserForm = SEP_Product_List_Page.QtWidgets.QWidget()
            ui = SEP_Product_List_Page.Ui_UserForm()
            ui.setupUi(UserForm)
            UserForm.show()

            sys.exit(app.exec_())
