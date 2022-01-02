"""
@author: Dibyesh Mishra
@date: 30-12-2021 18:56
"""
from fastapi import FastAPI
from pydantic import BaseModel

from database_connection import DbConnection

connection = DbConnection.establish_connection()
my_cursor = connection.cursor(buffered=True)

app = FastAPI()
students = {
    'dibyesh': ["m.sc", "ballia"],
    'gyanesh': ["m.tech", "gwalior"],
    'prashant': ["post doctrate", "Indore"],
    'Abhay': ["M.B.B.S", "Pune"]
    }


@app.get("/get_student/{name}")
async def display_result(name):
    return students.get(name)


@app.get("/get_tables")
async def display_table():
    query = "select * from persons"
    my_cursor.execute(query)
    list=[]
    for i in my_cursor:
        list.append(i)
    return list


class Person(BaseModel):
    person_id: int
    last_name: str
    first_name: str
    city: str


def add_person_db(person_id, last_name, first_name, city):
    query = "insert into persons (PersonID, LastName, FirstName, City) values (%d, '%s', '%s', '%s')" % (
       person_id, last_name, first_name, city)
    my_cursor.execute(query)
    connection.commit()
    return "person added succesfully!"


@app.post("/add_person/")
def add_person(person: Person):
    """
    desc: created api to insert item in the database table
    """
    person = add_person_db(person.person_id, person.last_name, person.first_name, person.city)
    return person


def update_person_details(first_name, city):
    query = "update persons set city = '%s' where FirstName = '%s' " % (city, first_name)
    my_cursor.execute(query)
    connection.commit()
    return "updated successfully"


@app.put("/update_person_name/")
def update_person(person: Person):
    update = update_person_details(person.first_name, person.city)
    return update


def delete_person_by_id(person_id):
    query = "delete from persons where PersonID = %d" % person_id
    my_cursor.execute(query)
    connection.commit()
    return "person detail deleted"


@app.delete("/delete_person_by_id/")
def delete_person(person: Person):
    delete_id = delete_person_by_id(person.person_id)
    return delete_id
