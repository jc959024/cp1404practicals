import datetime
from project import Project


def load_projects(filename):
    projects = []
    in_file = open(filename, 'r')
    next(in_file)  # Skip header line
    for line in in_file:
        name, start_date, priority, cost_estimate, completion_percentage = line.strip().split('\t')
        projects.append(Project(name, start_date, int(priority), float(cost_estimate), int(completion_percentage)))
    in_file.close()
    return projects

def save_projects(filename, projects):
    out_file = open(filename, 'w')
    out_file.write("Name\tStart Date\tPriority\tCost Estimate\tCompletion Percentage\n")
    for project in projects:
        out_file.write(
            f"{project.name}\t{project.start_date.strftime('%d/%m/%Y')}\t{project.priority}\t{project.cost_estimate}\t{project.completion_percentage}\n")
    out_file.close()
def display_projects(projects):


def add_new_project(projects):


def update_project(projects):


def filter_projects_by_date(projects, date):


def main_menu():
    return input(
        "- (L)oad projects\n- (S)ave projects\n- (D)isplay projects\n- (F)ilter projects by date\n- (A)dd new project\n- (U)pdate project\n- (Q)uit\n>>> ").lower()
def main():
    projects = []
    choice = main_menu()
    while choice != 'q':
        if choice == 'l':
            filename = input("Enter filename to load: ")
            projects = load_projects(filename)
        elif choice == 's':
            filename = input("Enter filename to save: ")
            save_projects(filename, projects)
        elif choice == 'd':
            display_projects(projects)
        elif choice == 'a':
            add_new_project(projects)
        elif choice == 'u':
            update_project(projects)
        elif choice == 'f':
            date_string = input("Show projects that start after date (dd/mm/yy): ")
            filter_projects_by_date(projects, date_string)
        choice = main_menu()

    print("Thank you for using custom-built project management software.")


if __name__ == "__main__":
    main()
