__version__ = 20230528


def apply_theme(app,theme:str):
    '''supported theme:\nauto\nlight\ndark'''
    import darkdetect
    from qfluentwidgets.common import setTheme, Theme, setThemeColor

    # setThemeColor("#4cc2ff")
    if theme=='auto':
        theme=('dark' if darkdetect.isDark() else 'light')
    if theme=='dark':
        setTheme(Theme.DARK)
        app.setStyleSheet(STYLESHHET_DARK)
    else:
        setTheme(Theme.LIGHT)
        app.setStyleSheet(STYLESHHET_LIGHT)


STYLESHHET_DARK = """
QMainWindow{background-color:#282828;  border-radius:20px}

QWidget{background-color:#282828;  border-radius:5px}
QTabWidget{background-color:#f0f0f0;border-radius:0px}

QLabel{color:#f0f0f0}

QMessageBox {background-color:#282828;  color:#f0f0f0;  border-radius:5px}
QMessageBox QLabel {color:#f0f0f0;  }
QMessageBox QPushButton {background-color:#353535;  color:#f0f0f0;  padding:5px 10px;  }
QMessageBox QPushButton:hover {background-color:#585858;  }
QMessageBox QPushButton:pressed {background-color:#444444;  }
QMessageBox QPushButton#closeButton {background-color:transparent;  color:#f0f0f0;}
QMessageBox QPushButton#closeButton:hover {color:#ff0000;  }
QMessageBox QPushButton#closeButton:pressed {color:#cc0000;  }


QTabWidget {background-color:#444444;  border-radius:5px;  }
QTabBar::tab {background-color:#444444;  border-radius:5px;  color:#f0f0f0;  padding:8px 12px;  margin-right:4px;  }
QTabBar::tab:selected {background-color:#4cc2ff;  color:#000000;  }
QTabBar::tab:!selected:hover {background-color:#585858;  }
QTabBar::tab:!selected:selected {background-color:#4cc2ff;  }
QTabWidget::pane {background-color:#585858;  }

"""


STYLESHHET_LIGHT ='''
QMainWindow{background-color:#f0f0f0;  border-radius:20px}

QWidget{background-color:#f0f0f0;  border-radius:5px}
QTabWidget{background-color:#ffffff;border-radius:0px}

QLabel{color:#000000}

QMessageBox {background-color:#f0f0f0;  color:#000000;  border-radius:5px}
QMessageBox QLabel {color:#000000;  }
QMessageBox QPushButton {background-color:#585858;  color:#000000;  padding:5px 10px;  }
QMessageBox QPushButton:hover {background-color:#585858;  }
QMessageBox QPushButton:pressed {background-color:#444444;  }
QMessageBox QPushButton#closeButton {background-color:transparent;  color:#000000;}
QMessageBox QPushButton#closeButton:hover {color:#ff0000;  }
QMessageBox QPushButton#closeButton:pressed {color:#cc0000;  }

QTabWidget {background-color:#ffffff;  border-radius:5px;  }
QTabBar::tab {background-color:#ffffff;  border-radius:5px;  color:#000000;  padding:8px 12px;  margin-right:4px;  }
QTabBar::tab:selected {background-color:#4cc2ff;  color:#ffffff;  }
QTabBar::tab:!selected:hover {background-color:#585858;  }
QTabBar::tab:!selected:selected {background-color:#4cc2ff;  }
QTabWidget::pane {background-color:#585858;  }
'''