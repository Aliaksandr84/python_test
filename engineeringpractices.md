Engineering Practices
1. Code Style & Structure
PEP8 compliance is recommended for all Python code (use flake8 or black for checking and formatting).

Naming:

Functions and variables: lower_snake_case

Classes: UpperCamelCase

Modules and folders: lower_snake_case

Test files: prefix with test_ and use lower_snake_case

One function, one purpose: Write small, focused functions for maintainability and testability.

2. Configuration & Secrets
Place all configuration in YAML files or as environment variables.

Never hardcode credentials or secrets (e.g., email passwords) in source code.

Reference configuration using safe loaders (e.g., os.getenv, yaml config).

3. Imports & Dependencies
Group imports: standard library first, third-party packages next, local modules last.

List all requirements in requirements.txt.

4. Testing
Write unit tests for each major function.

Place tests in files starting with test_.

Use pytest for a modern test workflow, or standard unittest.

Use assertions for expected behavior and edge cases.

5. Documentation
Every module, function, and class should have a clear docstring explaining its intent, inputs, and outputs.

Update README.md with setup, usage, and troubleshooting sections.

6. Error Handling & Robustness
Raise explicit errors (e.g., FileNotFoundError, ValueError) for missing files or bad config/inputs.

Catch and log exceptions at the entry point (e.g., in main()).

Print helpful error messages indicating the source of failure.

7. Project Structure
Keep source code in logical modules within folders (e.g., data_quality/).

Separate test code from production code.

Store sample data in a dedicated folder (e.g., sample.csv in root).

Place all documentation and configs in clearly named directories (configs/, .md files).

8. Version Control
Commit changes frequently with descriptive commit messages.

Do not commit sensitive data (.gitignore for unwanted files like .pyc, credentials, or local settings).