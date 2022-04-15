# drfapis

**Usage**

1. First set up the virtual environment and activate it.
2. Then execute following commands in virtual environment.
   1. `pip install -r requirements.txt`
   2. `python manage,py makemigrations`
   3. `python manage.py migrate`
   4. `python manage.py runserver`



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
