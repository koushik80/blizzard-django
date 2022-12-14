# Hi there<img src="https://media.giphy.com/media/l4S95aLS28TNZDlzbX/giphy.gif" width="50" height="50"/>! Here goes below my Project information

<div>
<h4 align="center"><a href="https://blizzard-car.herokuapp.com/">ßLIZZARD @ Accelerate the excitement</a></h4>
</div>
<h4 align="center">Note: It’s a matter of regret that unfortunately, this application might not work as live as Heroku implemented paid service from 28th November for deployment. I am trying to find out a possible solution to deploy in another hosting service. Thanks for realizing it.</h4>
<br>

---

<div>
<h3 align="left">Project Gallery: :oncoming_automobile:</h3>

<img width="1300" alt="g" src="https://user-images.githubusercontent.com/89943976/193223030-a6d96080-d810-4e80-874e-802d6879164c.gif">

<img width="1400" alt="g" src="https://user-images.githubusercontent.com/89943976/196051242-011c460d-9a68-477d-aa86-42476077b958.gif">

</div>

---

---

<div>
<img width="1716" alt="admin-panel3" src="https://user-images.githubusercontent.com/89943976/193468087-f3bfcca5-ab09-4dcf-97eb-85fb7bf1c221.png">
<img width="1718" alt="admin-panel2" src="https://user-images.githubusercontent.com/89943976/193468088-69988afe-45f9-446b-a5a4-313d0116ecd9.png">
<img width="1720" alt="admin-panel" src="https://user-images.githubusercontent.com/89943976/193468091-e3f8ec1a-c0cb-4021-942e-fb30fe35a35b.png">
</div>

---

<h3 align="left">Abstract: :speech_balloon:</h3>

<div align="left">This application is built to learn and implement as a part of an internship where the main target is to gain deeper knowledge about web development. And the goal is to analyse and learn tools for web back-end development such as Python programming Language and Django web framework, practice building complex systems using them, and learn to design server architecture. The challenge made my skills stronger. The implementation strives to be simple.<br>
</div>

---

<h3 align="left">Target Group: :family_man_woman_girl_girl:</h3>

<ul>
<li>A new entrepreneur who wants to start car selling business.</li>
<li>A person who wants to start an exchange car business in a small range.</li>
<li>A person who knows repairing old or faulty cars and wishes to sell after repair at the desired price.</li>
<li>A car garage can also use this app for selling tuned cars and parts.</li>
</ul>

---

<h3 align="left">User Stories: :bust_in_silhouette:</h3>

<ol type="1">
<li>Users can select a car by Name, Model, Location and Type of Car.</li>
<li>Users have the option to search by Price range.</li>
<li>Users can check the Latest and Featured cars.</li>
<li>When the user clicks the Read more button on the home page, he will be redirected to the services page.</li>
<li>Users are able to send messages by clicking Get in Touch button form the home page.</li>
<li>Users can connect to any team members by their social media link.</li>
<li>If the user clicks on one specific model, he or she can check the description of the car, more pictures, and features.</li>
<li>If a user is interested in any specific model, then he or she can send an inquiry to know more details by clicking send message button.</li>
<li>Users can register and login.</li>
<li>Users can also login with Facebook and Google accounts.</li>
<li>After login to the site users will be redirected to the dashboard and see their previous inquiries.</li>
<li>Users can send messages by clicking Get in Touch button on the home page.</li>
<li>Dealers can use the Admin panel to create their own accounts and update & remove data from the database.</li>
<li>Dealers can receive emails or inquiries from the clients</li>
<li>Working on dashboard functionality, customer review,Inquiry form,Contact page, sending email, Forcing user to login, Checking for existing inquiry... </li>
</ol>

---

<h3 align="left">Technologies: :computer:</h3>

<ul>
<li>HTML</li>
<li>Bootstrap</li>
<li>Material design</li>
<li>JavaScript</li>
<li>Python: Django</li>
<li>PostgreSQL</li>
<li>Git</li>
<li>GitHub</li>
<li>Heroku</li>
<li>VS Code</li>
</ul>

---

<h3 align="left">Learning Objective: :books:</h3>

<ul>
<p>Make a real project according to the client’s requirements</p>
<p>Implement HTML/Bootstrap template & Customize Django Admin Panel</p>
<p>PostgreSQL Database & Deploy it into Production Server</p>
<p>Setup Virtual Environment</p>
<p>Creating Django Apps</p>
<p>Implementing HTML and Bootstrap</p>
<p>PostgreSQL Database Setup</p>
<p>Django Static Files & Media Files</p>
<p>Django Admin Customization</p>
<p>Database Schema, Models and Migrations</p>
<p>Implementing RichText Editor & Multi-Select Fields on Admin Backend</p>
<p>Fetching Database Objects</p>
<p>Pagination</p>
<p>Search Functionality</p>
<p>User Authentication</p>
<p>Login with Facebook & Google</p>
<p>Send Emails</p>
<p>Database Dump Data & Load Data (local & remote)</p>
<p>Deploy on Heroku Server (Gunicorn, Whitenoise)</p>
<p>Add Custom Domain</p>
</ul>

---

<h3 align="left"> Prerequisites: :gear:</h3>
<p align="left">To be able to set up and run the project needed to install in local computer</p>
<ul>
<li>python3</li>
<li>pip</li>
<li>virtualenv</li>
</ul>

---

<h3 align="left">Instruction: :pager:</h3>
<p align="left">This is the guide on how to setup, run and deploy ßLIZZARD back-end server.To install run...</p>
<ul>
<li>sudo apt-get update</li>
<li>sudo apt-get install python3</li>
<li>sudo apt-get install python-pip</li>
<li>python3 -m pip install -upgrade pip </li>
<li>pip install virtualenv</li>
<li>source env/bin/activate</li>
<li>pip install django==4.1.1</li>
<li>python -m pip install Pillow</li>
<li>pip install django-ckeditor</li>
<li>pip install django-multiselectfield</li>
<li>pip install django-allauth</>
<li>pip install django-likert-field</li>
<li>pip install python-decouple</li>
<li>pip install django-star-ratings</li>
<li>pip install django-material==0.5.1</li>
<li>pip freeze > requirements.txt</li>
<li>pip install gunicorn psycopg2-binary</li>
<li>pip install dj-database-url</li>
<li>pip install whitenoise</li>
</ul>

---

<h4 align="left">Collecting data from static: :green_book:</h4>

<ul>
<li>python manage.py collectstatic</li>
</ul>

<h4 align="left">Create Django model: :green_book:</h4>
<ul>
<li>python manage.py createsuperuser</li>
</ul>

<h4 align="left">Migrate Django models: :arrows_clockwise:</h4>
<ul>
<li>python manage.py makemigrations</li>
<li>python manage.py migrate</li>
</ul>

<p align="left">By default, the project runs with DEBUG=True.</p>

<h4 align="left">Should be able to run and test the project locally: :man_technologist:</h4>
<ul>
<li>python manage.py runserver</li>
<li>python manage.py test</li>
</ul>
<p align="left">The server should be running on localhost: 8000</p>

---

<h3 align="left"> Error-Handling: :gear:</h3>
<p align="left">I faced plenty of errors during the development.I mentioned a few of those errors and how I was able to fix them.</p>

<p align="left">After installing MultiSelectField(django-multiselectfield) I faced this error - "IndexError: list assignment index out of range".
Incorrect:

```
self.validators[0] = MaxValueMultiFieldValidator(self.max_length)
```
```
features = MultiSelectField(choices=features_choices)
```

I solved this issue by adding max_length=100.Ref: cars-models.py

```
features = MultiSelectField(choices=features_choices, max_length=100)
```
</p>
<p align="left">In my localhost contact and inquiry features were working well. But if I send the same request from my heroku app then it was triggering this error – get() returned more than one User – it returned 2!
Ref: contact & pages app - views.py. Previously I used the get() method:

```
admin_info = User.objects.get(is_superuser=True)
```

Then I used the filter() method:

```
admin_info = admin_info = User.objects.filter(is_superuser=True)
```

After that I was still facing another error. But if I use filter then localhost also triggered the same error: "QuerySet object has no attribute 'email' ".  But with the get() method local host is working fine. The solution I found this way:

```
admin_email = User.objects.filter(is_superuser=True).values_list('email', flat=True)
```
```
send_mail(email_subject,message_body,'myemailaddress@gmail.com'admin_email,fail_silently=False)
```
</p>
<p align="left">When I was trying to deploy the app in Heroku server I run the command  heroku run python manage.py shell and followed the procedure to register the domain and getting id for Heroku:

```
>>>from django.contrib.sites.models import Site >>> site = Site() >>> site.domain = 'my_heroku_domain.com' >>> site.name = 'my_heroku_domain.com' >>> site.save() >>> print(Site.objects.get(name='my_heroku_domain.com').id)
```

After I got the id no I added it to the settings.py file and then added, committed and push to  heroku server. Unfortunately, the admin panel was unable to recognize the id and password. And also google and FB logins were not working. I added my_heroku_domain.com manually in the admin panel site by running the local server. The situation remains unchanged.

The Admin login problem was solved on the Heroku site by creating another admin account by running this command:  heroku run python manage.py createsuperuser. And ran the command

```
heroku config:set DISABLE_COLLECTSTATIC=1
```

and added in settings.py

```
ALLOWED_HOSTS = ['blizzard-car.herokuapp.com', 'blizzardauto.fi', 'www.blizzardauto.fi' ]
```
</p>

<p align="left">I installed ckeditor. I was facing an error importing ckeditor.fields in the  models.py  and also warning like:

```
cars.Car: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
```
```
pages.Team: (models.W042) Auto-created primary key used when not defining a primary key type, by default 'django.db.models.AutoField'.
```
Ref: cars-models.py

For the warning, I added this to settings.py

```
DEFAULT_AUTO_FIELD='django.db.models.AutoField'

```

For the error I corrected Field in lower case

```
from ckeditor.Fields import RichTextField
```

```
from ckeditor.fields import RichTextField
```

</p>


----

<h3 align="left">References: :paperclips:</h3>

<ul>
<li><a href="https://docs.djangoproject.com/en/4.1/" target="_blank">django</a></li>
<li><a href="https://www.udemy.com/" target="_blank">Udemy</a></li>
<li><a href="https://unsplash.com/s/photos/jpg" target="_blank">Unsplash</a></li>
<li><a href="https://www.youtube.com/watch?v=QaZrWIvAFsA" target="_blank">Recoding</a></li>
<li><a href="https://postgresapp.com/" target="_blank">Postgres.app</a></li>
<li><a href="https://pypi.org/project/django-likert-field/" target="_blank">Likert field</a></li>
<li><a href="https://support.google.com/mail/answer/185833?hl=en-GB" target="_blank">Gmail Help</a></li>
<li><a href="https://console.cloud.google.com/" target="_blank">Google Cloud</a></li>
<li><a href="https://developers.facebook.com/" target="_blank">Meta</a></li>
<li><a href="https://test-driven-django-development.readthedocs.io/en/latest/02-models.html" target="_blank">Test-Driven Django Development</a></li>
<li><a href="https://www.youtube.com/watch?v=GBgRMdjAx_c" target="_blank">Learn Django</a></li>
<li><a href="https://www.youtube.com/watch?v=hA_VxnxCHbo&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=3" target="_blank">Django Testing Tutorial-The Dumbfounds</a></li>
</ul>

---
