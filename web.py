from streamlit import title, subheader, write, checkbox, text_input, session_state, rerun
from functions import get_todos, write_todos

todos = get_todos()

def add_todo():
    todo = session_state["new_todo"] + '\n'# session_state è un dictionary che ha key = "new_todo" e
                                           # value ciò che si è scritto in text_unput
    # print(todo) solo per vedere il dictionary nella web app
    todos.append(todo)
    write_todos(todos) #aggiorna la web app con la nuova lista

# print(todos) anche qui per debugging

title("My Todo app")
subheader("This is my to do web app! ... Corca")
write("Scrive anche testo normale ...")

for index, todo in enumerate(todos):
    item_is_checked = checkbox(todo, key=todo) # Questo ciclo for aggiorna la web app
    # Visualizza gli elementi di todos e ritorna lo stato True se è checkato o False se non lo è
    if item_is_checked:
        todos.pop(index) # rimuove l'elemento dalla lista
        write_todos(todos) # aggiorna il file
        del session_state[todo] # aggiorna il dictionary
        rerun() # Per refrashare la pagina modificata dai check boxes


# Quando l'utente scrive un nuovo todo e preme Enter, add_todo callback viene chiamata
text_input(label="", placeholder="Enter a todo:",
           on_change=add_todo, key="new_todo")

session_state