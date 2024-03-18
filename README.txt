Repo: https://github.com/Cyanides11/COMP3005B-a3
Video: https://youtu.be/Joi86sVXsFU

1. Application uses python and psycopg to interact with the database.
2. To install psycopg, enter the command "pip install psycopg2" with python installed.
3. Create the database in pgadmin and implement the database schema using students.sql.
4. You can find your db_params in pgadmin by selecting the properties from PostgreSQL under Servers in the tree in the left bar.
5. Complete the db_params field at the top of the app.py file.
6. To view the entries in the database in pgadmin enter the query "SELECT * FROM students;"
7. To run the application uncomment the function call to test each function.
8. Then open the terminal in the directory of the script and enter "python app.py".
9. To check if the function performed the expected operation, query repeat the pgadmin query.