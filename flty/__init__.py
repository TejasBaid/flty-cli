import os
import sys

def create_flutter_structure(project_name, is_stateful):
    """Creates a Flutter project structure with the specified name."""
    
    # Define project path
    base_path = os.path.join(os.getcwd(), project_name)
    folders = ["models", "widgets", "providers", "views"]
    
    # Create main directory and subdirectories
    os.makedirs(base_path, exist_ok=True)
    for folder in folders:
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)
    
    # Create the view file
    view_file = os.path.join(base_path, "views", f"{project_name}_view.dart")
    
    widget_type = "StatefulWidget" if is_stateful else "StatelessWidget"
    constructor = f"{project_name.capitalize()}View({is_stateful and '{super.key}' or 'Key? key'});" 
    
    dart_template = f"""
import 'package:flutter/material.dart';

class {project_name.capitalize()}View extends {widget_type} {{
  {constructor}
  
  @override
  Widget build(BuildContext context) {{
    return Scaffold(
      appBar: AppBar(title: Text('{project_name.capitalize()}')),
      body: Center(child: Text('Welcome to {project_name.capitalize()} View!')),
    );
  }}
}}
    """
    
    with open(view_file, "w") as f:
        f.write(dart_template.strip())

    print(f"✅ Flutter project '{project_name}' created successfully!")


def main():
    """CLI entry point."""
    if len(sys.argv) < 3 or sys.argv[1] != "create":
        print("Usage: flty create <project_name> [stful]")
        return

    project_name = sys.argv[2]
    is_stateful = len(sys.argv) > 3 and sys.argv[3] == "stful"

    create_flutter_structure(project_name, is_stateful)


if __name__ == "__main__":
    main()
