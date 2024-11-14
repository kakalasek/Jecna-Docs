from flask import render_template
from . import main_page

@main_page.route('/')
def show():
        return render_template('home.html')