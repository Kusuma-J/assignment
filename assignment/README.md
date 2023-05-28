# Download and setup

Step-1: Creating a db in mysql
create a table named students(with columns firstname, lastname, age, grade) in your schema
and run the following query to insert data
``` 
INSERT INTO students (first_name, last_name, age, grade)
VALUES
    ('John', 'Doe', 18, 'A'),
    ('Jane', 'Smith', 17, 'B'),
    ('Michael', 'Johnson', 16, 'C'),
    ('Emily', 'Williams', 18, 'A'),
    ('Daniel', 'Brown', 17, 'B'),
    ('Olivia', 'Jones', 16, 'C'),
    ('Matthew', 'Garcia', 18, 'A'),
    ('Emma', 'Davis', 17, 'B'),
    ('Alexander', 'Rodriguez', 16, 'C'),
    ('Sophia', 'Martinez', 18, 'A'),
    ('William', 'Anderson', 17, 'B'),
    ('Ava', 'Taylor', 16, 'C'),
    ('Joseph', 'Thomas', 18, 'A'),
    ('Isabella', 'Hernandez', 17, 'B'),
    ('James', 'Moore', 16, 'C'),
    ('Oliver', 'Martin', 18, 'A'),
    ('Mia', 'Jackson', 17, 'B'),
    ('Benjamin', 'Lee', 16, 'C'),
    ('Amelia', 'White', 18, 'A'),
    ('Lucas', 'Harris', 17, 'B'),
    ('Evelyn', 'Clark', 16, 'C'),
    ('Alexander', 'Young', 18, 'A'),
    ('Harper', 'Lewis', 17, 'B'),
    ('Charlotte', 'Walker', 16, 'C'),
    ('Daniel', 'Hall', 18, 'A'),
    ('Sophia', 'Green', 17, 'B'),
    ('Avery', 'Adams', 16, 'C'),
    ('Matthew', 'Baker', 18, 'A'),
    ('Isabella', 'King', 17, 'B'),
    ('Joseph', 'Scott', 16, 'C'),
    ('Jackson', 'Bailey', 18, 'A'),
    ('Abigail', 'Lopez', 17, 'B'),
    ('Samuel', 'Gonzalez', 16, 'C'),
    ('Elijah', 'Nelson', 18, 'A'),
    ('Elizabeth', 'Hill', 17, 'B'),
    ('David', 'Rivera', 16, 'C'),
    ('Henry', 'Mitchell', 18, 'A'),
    ('Sofia', 'Carter', 17, 'B'),
    ('Victoria', 'Perez', 16, 'C'),
    ('Sebastian', 'Roberts', 18, 'A'),
    ('Scarlett', 'Turner', 17, 'B'),
    ('Aria', 'Phillips', 16, 'C'),
    ('Joseph', 'Campbell', 18, 'A'),
    ('Grace', 'Parker', 17, 'B'),
    ('Carter', 'Evans', 16, 'C'),
    ('Julia', 'Edwards', 18, 'A'),
    ('Liam', 'Collins', 17, 'B'),
    ('Madison', 'Stewart', 16, 'C'),
    ('Samuel', 'Morris', 18, 'A'),
    ('Ella', 'Sanchez', 17, 'B'),
    ('Ethan', 'Cook', 16, 'C');
```

Step-2: Installing Dependencies
    ```pip install -r requirements.txt```

Step-3: Running application
Powershell
```
  > $env:FLASK_ENV = "development"
  > flask run
```
step-4: using the api
visit localhost:5000 on your browser
with 
```http://127.0.0.1:5000//student/page/<pno>/limit/<limit>```
```example: http://127.0.0.1:5000//student/page/3/limit/5```
