from django.db import models
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from django.conf import settings
from django.contrib.auth.models import AbstractUser

from django.db import models


class User(AbstractUser):

    creationDate = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    city = models.TextField(null=True, blank=True)
    state = models.TextField(null=True, blank=True)
    zip = models.IntegerField(null=True, blank=True)
    country = models.TextField(null=True, blank=True)
    phone = models.TextField(null=True, blank=True)
    security_question = models.TextField(null=True, blank=True)
    security_answer = models.TextField(null=True, blank=True)
    contact_first = models.TextField(null=True, blank=True)
    contact_last = models.TextField(null=True, blank=True)
    contact_relationship = models.TextField(null=True, blank=True)
    contact_phone = models.TextField(null=True, blank=True)
    organization = models.TextField(null=True, blank=True)
    position_company = models.TextField(null=True, blank=True)

    #INHERITED FIELDS:
    #password
    #last_login
    #username
    #first_name
    #last_name
    #email
    #is_staff
    #is_active
    #date_joined

class Address(models.Model):
    address_1 = models.TextField()
    address_2 = models.TextField(null=True)
    city = models.TextField()
    state = models.CharField(max_length=2)
    zip = models.TextField()

class Event(models.Model):
    name = models.TextField()
    description = models.TextField(null=True)
    start_date = models.DateField(null=True)
    end_date = models.DateField(null=True)
    map_file_name = models.TextField(null=True)
    venue_name = models.TextField(null=True)
    address_ID = models.ForeignKey('Address', null=True)

class Area(models.Model):
    name = models.TextField()
    description = models.TextField(null=True)
    placeNumber = models.IntegerField()
    event_ID = models.ForeignKey('Event', null=False)
    coordinator_ID = models.ForeignKey('User', null=True, related_name='coordinator')
    supervisor_ID = models.ForeignKey('User', null=True, related_name='supervisor')

class Role(models.Model):
    name = models.TextField()
    type = models.TextField()
    area_ID = models.ForeignKey('Area', null=True)
    user_ID = models.ForeignKey('User', null=True, related_name = "user_ID")

class HistoricalFigure(models.Model):
    name = models.TextField()
    birth_date = models.DateField(null=True)
    birth_place = models.TextField(null=True)
    death_date = models.DateField(null=True)
    death_place = models.TextField(null=True)
    biographical_note = models.TextField(null=True)
    is_fictional = models.BooleanField(default=False)


class SaleItem(models.Model):
    name = models.TextField()
    description = models.TextField(null=True, blank=True)
    low_price = models.DecimalField(max_digits=10, decimal_places=2)
    high_price = models.DecimalField(max_digits=10, decimal_places=2)
    area_ID = models.ForeignKey(Area)

class Item(models.Model):
    name = models.TextField(null=True, blank=True)
    value = models.DecimalField(max_digits=7, decimal_places=2)
    description = models.TextField(null=True)
    standard_rental_value = models.DecimalField(max_digits=7, decimal_places=2)
    is_rentable = models.BooleanField(default=True)
    is_available_for_rental = models.BooleanField(default=True)

class WardrobeItem(Item):
    size_modifier = models.TextField(null=True, blank=True)
    size = models.TextField(null=True, blank=True)
    gender = models.CharField(null=True, blank=True, max_length=1)
    color = models.TextField(null=True, blank=True)
    pattern = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    start_year = models.IntegerField(null=True, blank=True)
    end_year = models.IntegerField(null=True, blank=True)

class ShoppingCart(models.Model):
    item_count = models.IntegerField()
    session_ID = models.ForeignKey(Session)


class Transaction(models.Model):
    customer = models.ForeignKey('User', null=False, related_name='customer')
    payment_id = models.TextField(null=True)
    date = models.DateField()
    phone = models.TextField(null=True)
    date_packed = models.DateField(null=True)
    packed_by = models.ForeignKey('User', null=True, related_name='packed_by')
    date_paid = models.DateField(null=True)
    payment_handler = models.ForeignKey('User', null=True, related_name='payment_handler')
    date_shipped = models.DateField(null=True)
    shipped_by = models.ForeignKey('User', null=True, related_name='shipped_by')
    tracking_number = models.TextField(null=True)
    order_total = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    line_item_total = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    line_rental_total = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    discount_applied = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    payment_id = models.TextField(null=True, blank=True)

class RentedLineItem(models.Model):
    condition = models.TextField(null=True)
    new_damage = models.TextField(null=True)
    damage_fee = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    late_fee = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    date_out = models.DateField()
    date_in = models.DateField(null=True, blank=True)
    date_due = models.DateField()
    discount_percent = models.DecimalField(null=True, max_digits=5, decimal_places=2)
    fees_paid = models.DecimalField(null=True, max_digits=7, decimal_places=2)
    item_ID = models.ForeignKey('Item', null=True)
    wardrobe_item_ID = models.ForeignKey('WardrobeItem', null=True, related_name='wardrobe_item_ID')
    transaction_ID = models.ForeignKey(Transaction, null=True, blank=True)

class Product(models.Model):
    name = models.TextField()
    description = models.TextField(null=True)
    category = models.TextField(null=True)
    current_price = models.DecimalField(null=True, max_digits=10, decimal_places=2)
    available = models.BooleanField(default=False)

    class Meta:
        abstract = True

class BulkProduct(Product):
    quantity_on_hand = models.IntegerField(null=True)

class PersonalProduct(Product):
    order_form_name = models.TextField(null=True)
    production_time = models.IntegerField(null=True)

class IndividualProduct(Product):
    date_made = models.DateField(null=True)

class LineItem(models.Model):
    product_type = models.IntegerField()
    line_item_total = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.IntegerField()
    bulk_product_ID = models.ForeignKey('BulkProduct', null = True)
    personal_product_ID = models.ForeignKey('PersonalProduct', null = True)
    individual_product_ID = models.ForeignKey('IndividualProduct', null = True)
    shopping_cart_ID = models.ForeignKey(ShoppingCart)