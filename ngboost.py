"""
This is the script that will generate angular components based on a few inputs.
The generated files will be:
    - component_name.component.ts
    - component_name.component.html
    - component_name.component.scss
    - component_name.module.ts
    - component_name.route.ts
"""

import sys
import os
import re

def create_dir(name):
    """
    Create a directory with the given name.
    """
    try:
        os.mkdir(name)
        os.chdir(name)
    except FileExistsError:
        print("Directory already exists!")
        sys.exit(1)

def add_content():
    """
    Populate the component directory
    """
    files = ["component.ts", "component.html", "component.css", "module.ts", "route.ts"]
    for file in files:
        path = f"{os.path.dirname(os.path.abspath(__file__))}/templates/{file}"

        with open(path, "r", encoding="utf-8") as file_in:
            content = file_in.read()

        with open(f"{component_name}.{file}", "w", encoding="utf-8") as file_out:
            file_out.write(replace_content(content))

def replace_content(content):
    """
    Replace the content of the template files with the given component name.
    """
    content = content.replace("$SELECTOR$", component_name)
    content = content.replace("$COMPONENT_NAME$", component_name.replace("-", " ").title().replace(" ", "") + "Component")
    content = content.replace("$TEMPLATE_URL$", f"./{component_name}.component.html")
    content = content.replace("$STYLE_URL$", f"./{component_name}.component.css")
    content = content.replace("$COMPONENT_PATH$", f"./{component_name}.component")
    content = content.replace("$ROUTE_PATH$", f"./{component_name}.route")
    content = content.replace("$ROUTE_NAME$", ''.join([component_name.capitalize() if i > 0 else component_name for i, component_name in enumerate(component_name.split('-'))] + ["Route"]))
    content = content.replace("$MODULE_NAME$", component_name.replace("-", " ").title().replace(" ", "") + "Module")
    return content

if __name__ == "__main__":
    component_name = input("Enter component name: ")
    # Check if component name is valid (pattern: sth-sth)
    if not re.match(r"^[a-z]+(-[a-z]+)*$", component_name):
        print("Invalid component name!")
        sys.exit(1)
    dir_name = component_name.split("-")[1]
    create_dir(dir_name)
    add_content()
