import json

FILE_NAME = "tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)

def add_task(tasks):
    task = input("Digite a nova tarefa: ")
    tasks.append({"task": task, "completed": False})
    save_tasks(tasks)
    print("Tarefa adicionada com sucesso!")

def list_tasks(tasks):
    if not tasks:
        print("Nenhuma tarefa encontrada.")
    for i, task in enumerate(tasks, start=1):
        status = "✔" if task["completed"] else "✘"
        print(f"{i}. {task['task']} - {status}")

def mark_task(tasks):
    list_tasks(tasks)
    index = int(input("Digite o número da tarefa a marcar/desmarcar: ")) - 1
    if 0 <= index < len(tasks):
        tasks[index]["completed"] = not tasks[index]["completed"]
        save_tasks(tasks)
        print("Tarefa atualizada com sucesso!")
    else:
        print("Tarefa inválida.")

def delete_task(tasks):
    list_tasks(tasks)
    index = int(input("Digite o número da tarefa a excluir: ")) - 1
    if 0 <= index < len(tasks):
        tasks.pop(index)
        save_tasks(tasks)
        print("Tarefa excluída com sucesso!")
    else:
        print("Tarefa inválida.")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar/desmarcar tarefa")
        print("4. Excluir tarefa")
        print("5. Sair")
        choice = input("Escolha uma opção: ")
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            mark_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()
