# drfapis

**Usage**

First set up the virtual environment and activate it.

Then execute following commands in virtual environment.

pip install -r requirements.txt

python manage,py makemigrations

python manage.py migrate

python manage.py runserver



# Approach followed

* **Override Django’s default Users Authentication** - for managing Users. 
  * Use Django User’s “is_staff” field to consider user as Admin 
  * The rest of all users are considered as Authors 
  * Email, Password and Full name fields are already provided by Django. 

* **Models** 
  * UserProfile model for storing additional fields by extending base User. 
    (Phone, Address, City, State, Country and Pincode) 
  * Content model for storing content with all fields mentioned in the above table and include User as the foreign key. 

* **APIs**
  * profile POST
  * login 
  * **Content** 
    * GET
    * POST
    * PUT
    * DELETE 
