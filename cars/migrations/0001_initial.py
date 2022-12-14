# Generated by Django 3.0.7 on 2022-09-24 18:46

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car_title', models.CharField(max_length=255)),
                ('state', models.CharField(choices=[('Lappi', 'Lapland'), ('Pohjois-Pohjanmaa', '\tNorth Ostrobothnia'), ('Kainuu', 'Kainuu'), ('Pohjois-Karjala', 'North Karelia'), ('Pohjois-Savo', 'North Savo'), ('Etelä-Savo', 'South Savo'), ('Etelä-Karjala', 'South Karelia'), ('Keski-Suomi', 'Central Finland'), ('Etelä-Pohjanmaa', 'South Ostrobothnia'), ('Pohjanmaa', 'Ostrobothnia'), ('Keski-Pohjanmaa', 'Central Ostrobothnia'), ('Pirkanmaa', 'Pirkanmaa'), ('Satakunta', 'Satakunta'), ('Päijät-Häme', 'Päijät-Häme'), ('Kanta-Häme', 'Kanta-Häme (Tavastia Proper)'), ('Kymenlaakso', 'Kymenlaakso'), ('Uusimaa', 'Uusimaa'), ('Varsinais-Suomi', 'Southwest Finland'), ('Ahvenanmaa', 'Åland')], max_length=100)),
                ('city', models.CharField(choices=[('Rovaniemi', 'Rovaniemi'), ('Oulu', 'Oulu'), ('Kajaani', 'Kajaani'), ('Joensuu', 'Joensuu'), ('Kuopio', 'Kuopio'), ('Mikkeli', 'Mikkeli'), ('Lappeenranta', 'Lappeenranta'), ('Jyväskylä', 'Jyväskylä'), ('Seinäjoki', 'Seinäjoki'), ('Vaasa', 'Vaasa'), ('Kokkola', 'Kokkola'), ('Tampere', 'Tampere'), ('Pori', 'Pori'), ('Lahti', 'Lahti'), ('Hämeenlinna', 'Hämeenlinna'), ('Kotka, Kouvola', 'Kotka, Kouvola'), ('Helsinki', 'Helsinki'), ('Turku', 'Turku'), ('Mariehamn', 'Mariehamn')], max_length=100)),
                ('color', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
                ('year', models.IntegerField(choices=[(2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], verbose_name='year')),
                ('condition', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('description', models.TextField(max_length=1000)),
                ('car_photo', models.ImageField(upload_to='photos/%Y/%m/%d/')),
                ('car_photo_1', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('car_photo_2', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('car_photo_3', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('car_photo_4', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('features', models.CharField(choices=[('Cruise Control', 'Cruise Control'), ('Audio Interface', 'Audio Interface'), ('Sound system', 'Sound system'), ('Smartphone integration', 'Smartphone integration'), ('Head-Up display', 'Head-Up display'), ('Airbags', 'Airbags'), ('Air Conditioning', 'Air Conditioning'), ('Seat Heating', 'Seat Heating'), ('Alarm System', 'Alarm System'), ('ParkAssist', 'ParkAssist'), ('Power Steering', 'Power Steering'), ('Reversing Camera', 'Reversing Camera'), ('Front Camera', 'Front Camera'), ('Direct Fuel Injection', 'Direct Fuel Injection'), ('Auto Start/Stop', 'Auto Start/Stop'), ('Wind Deflector', 'Wind Deflector'), ('Bluetooth Handset', 'Bluetooth Handset'), ('Central locking', 'Central locking'), ('Keyless', 'Keyless'), ('Motor heater', 'Motor heater'), ('Traffic sign recognition', 'Traffic sign recognition'), ('Power windows', 'Power windows'), ('Roof Opening Mechanism', 'Roof Opening Mechanism'), ('Tire-pressure monitoring system', 'Tire-pressure monitoring system'), ('Heated steering wheel', 'Heated steering wheel'), ('Heated windshield', 'Heated windshield'), ('ABS brakes', 'ABS brakes'), ('Adaptive headlights', 'Adaptive headlights'), ('Collision avoidance system', 'Collision avoidance system'), ('Isofix-ready', 'Isofix-ready'), ('Curve lights', 'Curve lights'), ('LED-headlights', 'LED-headlights'), ('Traction control', 'Traction control'), ('Fog lights', 'Fog lights'), ('Xenon light', 'Xenon light'), ('Blind spot sensor', 'Blind spot sensor'), ('Immobilizer', 'Immobilizer'), ('Alloy wheels', 'Alloy wheels'), ('Rain Sensor', 'Rain Sensor'), ('Turbo', 'Turbo'), ('Trunk temp-control device', 'Trunk temp-control device'), ('Sun hatch', 'Sun hatch'), ('Plug-in charging for hybrid vehicles', 'Plug-in charging for hybrid vehicles'), ('Sunroof', 'Sunroof'), ('Air suspension', 'Air suspension'), ('Two sets of tyres', 'Two sets of tyres'), ('Driving assistant', 'Driving assistant'), ('Multiactive Steering Wheel', 'Multiactive Steering Wheel')], max_length=100)),
                ('body_style', models.CharField(max_length=100)),
                ('engine', models.CharField(max_length=100)),
                ('transmission', models.CharField(max_length=100)),
                ('interior', models.CharField(max_length=100)),
                ('miles', models.IntegerField()),
                ('doors', models.CharField(choices=[('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6')], max_length=10)),
                ('passengers', models.IntegerField()),
                ('vin_no', models.CharField(max_length=100)),
                ('mileage', models.IntegerField()),
                ('fuel_type', models.CharField(max_length=50)),
                ('no_of_owners', models.CharField(max_length=100)),
                ('is_featured', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
