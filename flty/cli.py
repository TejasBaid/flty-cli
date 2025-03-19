import os
import sys

def create_flutter_structure(project_name, is_stateful):
    """Creates a Flutter project structure with the specified name."""
    
    base_path = os.path.join(os.getcwd(), project_name)
    folders = ["models", "widgets", "providers", "views"]
    
    os.makedirs(base_path, exist_ok=True)
    for folder in folders:
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)
    
    view_file = os.path.join(base_path, "views", f"{project_name}_view.dart")
    
    class_name = f"{project_name.capitalize()}View"

    if is_stateful:
        dart_template = f"""
import 'package:flutter/material.dart';

class {class_name} extends StatefulWidget {{
  const {class_name}({{super.key}});

  @override
  State<{class_name}> createState() => _{class_name}State();
}}

class _{class_name}State extends State<{class_name}> {{
  @override
  Widget build(BuildContext context) {{
    return Scaffold(
      appBar: AppBar(title: Text('{class_name}')),
      body: Center(child: Text('Welcome to {class_name}!')),
    );
  }}
}}
        """
    else:
        dart_template = f"""
import 'package:flutter/material.dart';

class {class_name} extends StatelessWidget {{
  const {class_name}({{super.key}});

  @override
  Widget build(BuildContext context) {{
    return Scaffold(
      appBar: AppBar(title: Text('{class_name}')),
      body: Center(child: Text('Welcome to {class_name}!')),
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
