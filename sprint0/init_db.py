#!/usr/bin/env python3

import random
import os
import datetime
import sys

# initialize the django environment
# assumes ./proj/settings.py is your settings file, relative to current dir
os.environ['DJANGO_SETTINGS_MODULE'] = 'sprint0.settings'

import django
django.setup()


from django.contrib.auth.models import Group, Permission, ContentType
from django.db import connection
import subprocess
import homepage.models as hmod
##### DROP DATABASE, RECREATE IT, THEN MIGRATE IT #################

cursor = connection.cursor()
cursor.execute("DROP SCHEMA PUBLIC CASCADE")
cursor.execute("CREATE SCHEMA PUBLIC")
subprocess.call([sys.executable, "manage.py", "migrate"])

##### CREATE PERMISSIONS/GROUPS #####################

Permission.objects.all().delete()
Group.objects.all().delete()

AdminPermission = Permission()
AdminPermission.codename = 'admin_rights'
AdminPermission.content_type = ContentType.objects.get(id=7)
AdminPermission.name = 'Has Admin Rights'
AdminPermission.save()

ManagerPermission = Permission()
ManagerPermission.codename = 'manager_rights'
ManagerPermission.content_type = ContentType.objects.get(id=7)
ManagerPermission.name = 'Has Manager Rights'
ManagerPermission.save()

AdminGroup = Group()
AdminGroup.name = "AdminGroup"
AdminGroup.save()
AdminGroup.permissions.add(AdminPermission)
AdminGroup.permissions.add(ManagerPermission)

ManagerGroup = Group()
ManagerGroup.name = "ManagerGroup"
ManagerGroup.save()
ManagerGroup.permissions.add(ManagerPermission)


GuestGroup = Group()
GuestGroup.name = "GuestGroup"
GuestGroup.save()




print('permissions initialized')

############ MAKE USERS ####################


u = hmod.User()
u.creationDate = '1970-11-22'
u.address = '2295 West Campus Dr'
u.city = 'Provo'
u.state = 'UT'
u.zip = '84606'
u.country = 'USA'
u.phone = '2089082577'
u.security_question = 'What is your favorite subject?'
u.security_answer = 'Information Systems'
u.username = 'Conan'
u.first_name = 'Conan'
u.last_name = 'Albrecht'
u.set_password('Password1')
u.is_superuser = True
u.email = 'short1inslo@gmail.com'
u.save()

g = Group.objects.get(name="AdminGroup")
g.user_set.add(u)



u = hmod.User()
u.creationDate = '1992-11-11'
u.address = '2295 East Campus Dr'
u.city = 'Provo'
u.state = 'UT'
u.zip = '84606'
u.country = 'USA'
u.phone = '3852018669'
u.security_question = 'What is your favorite university?'
u.security_answer = 'BYU'
u.username = 'Tanners'
u.first_name = 'Tanner'
u.last_name = 'Skousen'
u.set_password('Password2')
u.is_superuser = False
u.email = 'johanson.brock@gmail.com'
u.save()

g = Group.objects.get(name="ManagerGroup")
g.user_set.add(u)

u = hmod.User()
u.creationDate = '1990-12-12'
u.address = '2295 North Campus Dr'
u.city = 'Provo'
u.state = 'UT'
u.zip = '84606'
u.country = 'USA'
u.phone = '3852018269'
u.security_question = 'What is your favorite country?'
u.security_answer = 'Brazil'
u.username = 'Bryanp'
u.first_name = 'Bryan'
u.last_name = 'Pinho'
u.set_password('Password3')
u.is_superuser = False
u.email = 'byuisgroup22@gmail.com'
u.save()

g = Group.objects.get(name="GuestGroup")
g.user_set.add(u)

for data in [
    ['Colonial Breeches', 25.50, 'Standard colonial pants for the time period', 12.50, True, 'Runs large', 'LG', 'M',
     'Blue', 'checkered', 'This item is extremely valuable', 1875, 1890, True],
    ['Colonial Shirt', 10.00, 'Standard colonial shirt for the time period', 4.00, True, 'Runs small', 'M', 'F',
     'Green', '', '', 1875, 1890, True],
    ['Colonial Stockings', 5.00, '', 1.00, True, 'Gove wore these so now they run HUGE', 'LG', 'M',
     'Red and White', '', '', 1600, 2015, False],
]:
    wdbItem = hmod.WardrobeItem()
    wdbItem.name = data[0]
    wdbItem.value = data[1]
    wdbItem.description = data[2]
    wdbItem.standard_rental_value = data[3]
    wdbItem.is_rentable = data[4]
    wdbItem.size_modifier = data[5]
    wdbItem.size = data[6]
    wdbItem.gender = data[7]
    wdbItem.color = data[8]
    wdbItem.pattern = data[9]
    wdbItem.note = data[10]
    wdbItem.start_year = data[11]
    wdbItem.end_year = data[12]
    wdbItem.is_available_for_rental = data[13]
    wdbItem.save()

for data in [

    ['Replica Liberty Bell', 'Really tiny copy of the liberty bell done in plastic', 'Novelties', 3.50, True, 100],
    ['Colonial Brick', 'A brick fashioned and manufactured according to true colonial styles', 'Colonial Life', 5.50,
     True, 120],
    ['Replica Declaration of Independence', 'Copy of the original declaration including signatures etc.', 'Novelties',
     13.50, True, 40],
]:
    blkItem = hmod.BulkProduct()
    blkItem.name = data[0]
    blkItem.description = data[1]
    blkItem.category = data[2]
    blkItem.current_price = data[3]
    blkItem.available = data[4]
    blkItem.quantity_on_hand = data[5]
    blkItem.save()
    
for data in [

    ['Personalized Breeches', 'Breeches made to fit YOU just rights', 'Personal Products', 43.50, True, 'Breeches_measurement.pdf', 30],
    ['Engraved Rolling Pin', 'Oak rolling pin with any number of engravings on it', 'Personal Product', 25.50,
     True, 'pin_order_from.doc', 15],
]:
    persProduct = hmod.PersonalProduct()
    persProduct.name = data[0]
    persProduct.description = data[1]
    persProduct.category = data[2]
    persProduct.current_price = data[3]
    persProduct.available = data[4]
    persProduct.order_form_name = data[5]
    persProduct.production_time = data[6]
    persProduct.save()

for data in [

    ['Area Controller', 'Volunteer'],
    ['Performer', 'Volunteer']
]:
    role = hmod.Role()
    role.name = data[0]
    role.type = data[1]
    role.save()

for data in [

    ['Heritage Tours', 'Tour of all Revolutionary Places', '2015-04-05', '2015-05-05', 'Computer/maps/map1', 'Washington DC locations'],
    ['Colonial Event', 'National Provo Event', '2015-06-15', '2015-07-01', 'Computer/maps/map2', 'Scera Park']
]:
    event = hmod.Event()
    event.name = data[0]
    event.description = data[1]
    event.start_date = data[2]
    event.end_date = data[3]
    event.map_file_name = data[4]
    event.venue_name = data[5]
    event.save()

for data in [

    [hmod.User.objects.get(id=1), '2015-03-16'],
    [hmod.User.objects.get(id=1), '2015-03-16'],
    [hmod.User.objects.get(id=2), '2015-03-16'],
    [hmod.User.objects.get(id=2), '2015-03-16'],
    [hmod.User.objects.get(id=1), '2015-03-16'],
    [hmod.User.objects.get(id=3), '2015-03-16'],
    [hmod.User.objects.get(id=3), '2015-03-16'],
    [hmod.User.objects.get(id=2), '2015-03-16'],

]:
    transaction = hmod.Transaction()
    transaction.customer = data[0]
    transaction.date = data[1]
    transaction.save()

for data in [

    ['Good', 'Chip on the side', 1.00, 5.00, '2015-04-01', '2015-03-01', None, 15, 6, hmod.WardrobeItem.objects.get(id=1),
     hmod.Transaction.objects.get(id=7)],
    ['Fair', 'Ripped cloth', 2.00, 4.00, '2015-03-16', '2015-04-01', '2015-04-01', 10, 6,
     hmod.WardrobeItem.objects.get(id=1), hmod.Transaction.objects.get(id=1)],
    ['Fair', 'Ripped cloth', 2.00, 4.00, '2015-03-16', '2015-02-2', None, 10, 6, hmod.WardrobeItem.objects.get(id=1),
     hmod.Transaction.objects.get(id=2)],
    ['Fair', 'Ripped cloth', 2.00, 4.00, '2015-03-16', '2014-12-01', None, 10, 6, hmod.WardrobeItem.objects.get(id=2),
     hmod.Transaction.objects.get(id=3)],
    ['Fair', 'Ripped cloth', 2.00, 4.00, '2015-03-16', '2015-01-23', None, 10, 6, hmod.WardrobeItem.objects.get(id=1),
     hmod.Transaction.objects.get(id=4)],
    ['Fair', 'Ripped cloth', 2.00, 4.00, '2015-03-16', '2014-11-01', None, 10, 6, hmod.WardrobeItem.objects.get(id=2),
     hmod.Transaction.objects.get(id=5)],
    ['Fair', 'Ripped cloth', 2.00, 4.00, '2015-03-16', '2014-04-01', None, 10, 6, hmod.WardrobeItem.objects.get(id=1),
     hmod.Transaction.objects.get(id=6)],
]:
    rentedLineItem = hmod.RentedLineItem()
    rentedLineItem.condition = data[0]
    rentedLineItem.new_damage = data[1]
    rentedLineItem.damage_fee = data[2]
    rentedLineItem.late_fee = data[3]
    rentedLineItem.date_out = data[4]
    rentedLineItem.date_due = data[5]
    rentedLineItem.date_in = data[6]
    rentedLineItem.discount_percent = data[7]
    rentedLineItem.fees_paid = data[8]
    rentedLineItem.wardrobe_item_ID = data[9]
    rentedLineItem.transaction_ID = data[10]
    rentedLineItem.save()
    
for data in [

    ['Old Timey Trail Hike', 'historical walk through the provo canyon', 1, hmod.Event.objects.get(id=1),
     hmod.User.objects.get(id=1), hmod.User.objects.get(id=2)],
    ['Old Timey baking adventure',
     'a walk through of the daily process required for feeding oneself during colonial times', 1, hmod.Event.objects.get(id=1), hmod.User.objects.get(id=2), hmod.User.objects.get(id=3)],
    ['Old Timey arms display', 'a display of the progress of colonial weaponry through the time period', 1,
     hmod.Event.objects.get(id=2), hmod.User.objects.get(id=3), hmod.User.objects.get(id=2)],
]:
    area = hmod.Area()
    area.name = data[0]
    area.description = data[1]
    area.placeNumber = data[2]
    area.event_ID = data[3]
    area.coordinator_ID = data[4]
    area.supervisor_ID = data[5]
    area.save()
    
    
for data in [

    ['Colonial Knife', 'a dull, rusty knife', 22.50, 35.50, hmod.Area.objects.get(id=1)],
    ['Colonial Broom', 'an atrsy colonial broom', 22.50, 40.50, hmod.Area.objects.get(id=1)],
    ['Colonial Stool', 'a typical colonial stool', 52.50, 55.50, hmod.Area.objects.get(id=2)],
    ['Colonial spood', 'a spoon typical of the time period', 32.50, 35.50, hmod.Area.objects.get(id=3)],

        ]:
    saleItem = hmod.SaleItem()
    saleItem.name = data[0]
    saleItem.description = data[1]
    saleItem.low_price = data[2]
    saleItem.high_price = data[3]
    saleItem.area_ID = data[4]
    saleItem.save()