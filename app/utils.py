from flask_admin.contrib.sqla import ModelView
from flask_admin import Admin, BaseView, expose
from app import app, db
from app.models import Category, Product
from flask_login import logout_user, current_user
from flask import redirect
from app.models import UserRoleEnum

def count_cart(cart):
    total_quantity, total_amount= 0,0

    if cart:
        for c in cart.values():
            total_quantity+=c['quantity']
            total_amount+=c['quantity']*c['price']

    return {
        'total_quantity': total_quantity,
        'total_amount':total_amount
    }

