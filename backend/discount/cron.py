from datetime import datetime
from products.models import Product
from .models import Discount
from datetime import date

def my_scheduled_job():
    for discount in Discount:
        if discount.valid_to <= date.today():
            discount.delete()