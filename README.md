### Api service for library
***Simple but convenient solution for library management***
###  Install  and create db
```shell
git clone https://github.com/tkachuk2291/library_management_api
``` 
```shell
cd library_management_api
```
```shell
python3 -m venv venv  
``` 
```shell
source venv/bin/activate  
```
```shell
pip install -r requirements.txt  
```
### Setting up Environment Variables
```shell
touch .env  
```
### Example of environment variables
``` 
 .env.sample 
```
**Here you can generate your secret key** 
https://djecrety.ir/ 

**Here is dublicate  example for env file** 

``` 
SECRET_KEY='secret_key'
DB_NAME='db_name'
DB_USER='postgres'
DB_PASSWORD='password'
DB_HOST='localhost'
DB_PORT=5432
```


### Migrations & Server

```shell
   python manage.py makemigrations
```

```shell
   python manage.py migrate
```

```shell
   python manage.py runserver 8001
```

**Here is basic link for endpoints**
http://127.0.0.1:8001/


**Library endpoint**  

***"books-list" METHODS (GET, POST): http://127.0.0.1:8001/books/***
***"book-detail" METHODS (GET, PUT, PATCH, DELETE): http://127.0.0.1:8001/books/id/
(please changed id for id object 1, 2, 3 ....)***


***Please Note***  

***You can use the Django interface to try endpins more conveniently. To do this, simply follow the links in Readme.
Also, ask questions in case of any failure, I will be happy to help***  

***I also did not add authorization and authentication to avoid the complexity of launching the project; 
this was not included in those tasks; if you need to add it, let me know.***