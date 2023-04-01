import streamlit as st
import functions

todo_list = functions.get_todos()

def add_todo():
    new_todo = st.session_state["new_todo"] + "\n"
    todo_list.append(new_todo)
    functions.write_text_file(todo_list)


st.title("My Todo App")
st.subheader("This is my todo app")
st.write("To increase my productivity")

for index, todo in enumerate(todo_list):
    todo = todo.strip("\n")
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todo_list.pop(index)
        functions.write_text_file(todo_list)
        del st.session_state[todo]
        st.experimental_rerun()


st.text_input(label="Add todo", placeholder="Enter a todo...",
              on_change=add_todo, key="new_todo")

