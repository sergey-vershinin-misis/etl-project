import peewee as pw
from dotenv import load_dotenv

from db.common.settings import DBSettings

load_dotenv()
db_settings = DBSettings()

db = pw.SqliteDatabase(db_settings.path)


class AdvWorksProducts(pw.Model):
    product_key = pw.BigAutoField()
    product_subcategory_key = pw.IntegerField()
    product_SKU = pw.TextField()
    model_name = pw.TextField()
    product_description = pw.TextField()
    product_color = pw.TextField()
    product_size = pw.TextField()
    product_style = pw.TextField()
    product_cost = pw.FloatField()
    product_price = pw.FloatField()

    class Meta:
        database = db


class AdvWorksSales(pw.Model):
    order_date = pw.DateField()
    stock_date = pw.DateField()
    order_number = pw.TextField()
    product_key = pw.IntegerField()
    customer_key = pw.IntegerField()
    territory_key = pw.IntegerField()
    order_line_item = pw.IntegerField()
    order_quantity = pw.IntegerField()

    class Meta:
        database = db


class AdvWorksTerritories(pw.Model):
    territory_key = pw.BigAutoField()
    region = pw.TextField()
    country = pw.TextField()
    continent = pw.TextField()

    class Meta:
        database = db
