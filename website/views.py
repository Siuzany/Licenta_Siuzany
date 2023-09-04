from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
import secrets
import os


views = Blueprint('views', __name__)


@views.route('/', methods=['POST', 'GET'])
@login_required
def home():
    # data = studentii.query.filter_by(id=id).first()
    return render_template("home.html", user=current_user)

