## Extract Json Data
This contains a Python App that extracts json data from a file and inserts it into the  postgres DB

### Clone the repo 
### How to setup
1.Cd into the Directory and create a virtual environment `virtualenv venv`and activate the env 
2. Activate the Virtual environment `source venv/bin/activate`
3. Install Dependencies `pip install -r requirements.txt`
4.Create a Postgres DB and add the configuration necessary configs in the config file
`postgresql://username:password@localhost:5432/database_name`
5. To initilize the DB run 
`python db migrate.py init`
6.To create migration files
`python db migrate.py migrate`
7. To create tables in your DB
`python db  migrate.py upgrade`

### To start server
`python run.py`

To test the URL on postman perform a Post Request this populates the database with the extracted Data

http://127.0.0.1:5000/api/


