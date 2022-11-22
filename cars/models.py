from django.db import models
from datetime import datetime
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField



# Created car model here specified by state, city, , body, doors, technical features etc.

class Car(models.Model):

    state_choice = (
        ('Lappi', 'Lapland'),
        ('Pohjois-Pohjanmaa', '	North Ostrobothnia'),
        ('Kainuu', 'Kainuu'),
        ('Pohjois-Karjala', 'North Karelia'),
        ('Pohjois-Savo', 'North Savo'),
        ('Etelä-Savo', 'South Savo'),
        ('Etelä-Karjala', 'South Karelia'),
        ('Keski-Suomi', 'Central Finland'),
        ('Etelä-Pohjanmaa', 'South Ostrobothnia'),
        ('Pohjanmaa', 'Ostrobothnia'),
        ('Keski-Pohjanmaa', 'Central Ostrobothnia'),
        ('Pirkanmaa', 'Pirkanmaa'),
        ('Satakunta', 'Satakunta'),
        ('Päijät-Häme', 'Päijät-Häme'),
        ('Kanta-Häme', 'Kanta-Häme (Tavastia Proper)'),
        ('Kymenlaakso', 'Kymenlaakso'),
        ('Uusimaa', 'Uusimaa'),
        ('Varsinais-Suomi', 'Southwest Finland'),
        ('Ahvenanmaa', 'Åland'),
    )

    city_choice = (
        ('Rovaniemi', 'Rovaniemi'),
        ('Oulu', 'Oulu'),
        ('Kajaani', 'Kajaani'),
        ('Joensuu', 'Joensuu'),
        ('Kuopio', 'Kuopio'),
        ('Mikkeli', 'Mikkeli'),
        ('Lappeenranta', 'Lappeenranta'),
        ('Jyväskylä', 'Jyväskylä'),
        ('Seinäjoki', 'Seinäjoki'),
        ('Vaasa', 'Vaasa'),
        ('Kokkola', 'Kokkola'),
        ('Tampere', 'Tampere'),
        ('Pori', 'Pori'),
        ('Lahti', 'Lahti'),
        ('Hämeenlinna', 'Hämeenlinna'),
        ('Kotka, Kouvola', 'Kotka, Kouvola'),
        ('Helsinki', 'Helsinki'),
        ('Vantaa', 'Vantaa'),
        ('Espoo', 'Espoo'),
        ('Turku', 'Turku'),
        ('Mariehamn', 'Mariehamn'),
    )

    year_choice = []
    for r in range(2000, (datetime.now().year+1)):
        year_choice.append((r,r))


    features_choices = (
        ('Cruise Control', 'Cruise Control'),
        ('Audio Interface', 'Audio Interface'),
        ('Sound system', 'Sound system'),
        ('Smartphone integration', 'Smartphone integration'),
        ('Head-Up display', 'Head-Up display'),
        ('Airbags', 'Airbags'),
        ('Air Conditioning', 'Air Conditioning'),
        ('Seat Heating', 'Seat Heating'),
        ('Alarm System', 'Alarm System'),
        ('ParkAssist', 'ParkAssist'),
        ('Power Steering', 'Power Steering'),
        ('Reversing Camera', 'Reversing Camera'),
        ('Front Camera', 'Front Camera'),
        ('Direct Fuel Injection', 'Direct Fuel Injection'),
        ('Auto Start/Stop', 'Auto Start/Stop'),
        ('Wind Deflector', 'Wind Deflector'),
        ('Bluetooth Handset', 'Bluetooth Handset'),
        ('Central locking', 'Central locking'),
        ('Keyless', 'Keyless'),
        ('Motor heater', 'Motor heater'),
        ('Traffic sign recognition', 'Traffic sign recognition'),
        ('Power windows', 'Power windows'),
        ('Roof Opening Mechanism', 'Roof Opening Mechanism'),
        ('Tire-pressure monitoring system', 'Tire-pressure monitoring system'),
        ('Heated steering wheel', 'Heated steering wheel'),
        ('Heated windshield', 'Heated windshield'),
        ('ABS brakes', 'ABS brakes'),
        ('Adaptive headlights', 'Adaptive headlights'),
        ('Collision avoidance system', 'Collision avoidance system'),
        ('Isofix-ready', 'Isofix-ready'),
        ('Curve lights', 'Curve lights'),
        ('LED-headlights', 'LED-headlights'),
        ('Traction control', 'Traction control'),
        ('Fog lights', 'Fog lights'),
        ('Xenon light', 'Xenon light'),
        ('Blind spot sensor', 'Blind spot sensor'),
        ('Immobilizer', 'Immobilizer'),
        ('Alloy wheels', 'Alloy wheels'),
        ('Rain Sensor', 'Rain Sensor'),
        ('Turbo', 'Turbo'),
        ('Trunk temp-control device', 'Trunk temp-control device'),
        ('Sun hatch', 'Sun hatch'),
        ('Plug-in charging for hybrid vehicles', 'Plug-in charging for hybrid vehicles'),
        ('Sunroof', 'Sunroof'),
        ('Air suspension', 'Air suspension'),
        ('Two sets of tyres', 'Two sets of tyres'),
        ('Driving assistant', 'Driving assistant'),
        ('Multiactive Steering Wheel', 'Multiactive Steering Wheel'),
    )

    door_choices = (
        ('2', '2'),
        ('3', '3'),
        ('4', '4'),
        ('5', '5'),
        ('6', '6'),
    )


    car_title = models.CharField(max_length=255)
    state = models.CharField(choices=state_choice, max_length=100)
    city = models.CharField(choices=city_choice, max_length=100)
    color = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField(('year'), choices=year_choice)
    condition = models.CharField(max_length=100)
    price = models.IntegerField()
    description = RichTextField()
    car_photo = models.ImageField(upload_to='photos/%Y/%m/%d/')
    car_photo_1 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_2 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_3 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    car_photo_4 = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    features = MultiSelectField(choices=features_choices, max_length=1000)
    body_style = models.CharField(max_length=100)
    engine = models.CharField(max_length=100)
    transmission = models.CharField(max_length=100)
    interior = models.CharField(max_length=100)
    miles = models.IntegerField()
    doors = models.CharField(choices=door_choices, max_length=10)
    passengers = models.IntegerField()
    vin_no = models.CharField(max_length=100)
    mileage = models.IntegerField()
    fuel_type = models.CharField(max_length=50)
    no_of_owners = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=datetime.now, blank=True)

    def __str__(self):
        return self.car_title

