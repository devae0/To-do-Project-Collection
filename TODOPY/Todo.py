import json
import os

FILENAME = "tasks.json"


def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as f:
            return json.load(f)
    return []


def save_tasks(tasks):
    with open(FILENAME, "w") as f:
        json.dump(tasks, f, indent=4)


def main():
    tasks = load_tasks()
    print("--- 📝 ADVANCED TERMINAL TODO ---")

    while True:
        print(
            f"\nTotal Tasks: {len(tasks)} | 1:Add 2:View 3:Del 4:Done 5:Exit")
        choice = input("Select: ")

        if choice == '1':
            name = input("Task: ").strip()
            if name:
                tasks.append({"task": name, "status": "pending"})
                save_tasks(tasks)
                print("Saved!")

        elif choice == '2':
            if not tasks:
                print("List empty.")
            else:
                for i, t in enumerate(tasks, 1):
                    mark = "✔" if t['status'] == "done" else " "
                    print(f"{i}. [{mark}] {t['task']}")

        elif choice == '3':
            try:
                idx = int(input("Delete # : "))
                tasks.pop(idx-1)
                save_tasks(tasks)
                print("Removed.")
            except:
                print("Invalid number.")

        elif choice == '4':
            try:
                nums = map(int, input(
                    "Complete # (space separated): ").split())
                for n in nums:
                    if 1 <= n <= len(tasks):
                        tasks[n-1]['status'] = "done"
                save_tasks(tasks)
                print("Updated!")
            except:
                print("Input error.")

        elif choice == '5':
            print("Goodbye!")
            break


if __name__ == "__main__":
    main()
