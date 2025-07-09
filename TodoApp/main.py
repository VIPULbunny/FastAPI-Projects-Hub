from fastapi import FastAPI
import models
from database import engine

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

#(fastapienv) PS C:\Users\Vipul\Documents\fastapi> cd TodoApp
# (fastapienv) PS C:\Users\Vipul\Documents\fastapi\TodoApp> sqlite3 todos.db
# sqlite> .schema
# sqlite> insert into todos (title,description,priority,complete) values('Go  to the store','Pick up Eggs',5,False);
# sqlite> select * from todos;
# sqlite> insert into todos (title,description,priority,complete) values('Cut the Lawn','Grass is Getting long',3,False);
# sqlite> select * from todos;
# sqlite> insert into todos (title,description,priority,complete) values('Feed the dog','He is Getting Hungry',5,False);
# sqlite> select * from todos;
# sqlite> .mode column
# sqlite> .mode markdown
# sqlite> .mode box
# sqlite> .mode table
# sqlite> select * from todos;
# sqlite> insert into todos (title,description,priority,complete) values('Test element','He is Getting Hungry',5,False);
# sqlite> delete from todos where id =4;
# sqlite> select * from todos;
# sqlite> insert into todos (title,description,priority,complete) values('A new test element','He is Getting Hungry',5,False);
# sqlite> select * from todos;
# sqlite> delete from todos where id =4;
# sqlite> select * from todos;