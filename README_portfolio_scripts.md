# Portfolio Management Scripts

This repository contains Python scripts to help manage and analyze the portfolio website data.

## Scripts Overview

### 1. `project_manager.py`
A comprehensive project management library that can:
- Extract project data from the HTML file
- Export project information to JSON format
- Validate project data for completeness
- Generate HTML sections for projects
- Provide portfolio statistics

### 2. `portfolio_cli.py` 
A command-line interface tool for easy portfolio management.

## Requirements

- Python 3.6 or higher
- No external dependencies required (uses only standard library)

## Usage

### Basic Project Manager

```bash
# Extract and analyze all projects from projects.html
python3 project_manager.py
```

This will:
- Extract project data from `projects.html`
- Save the data to `projects_data.json`
- Display a summary with statistics
- Show validation results

### Command Line Interface

#### List all projects
```bash
python3 portfolio_cli.py list
```

#### List projects with details
```bash
python3 portfolio_cli.py list --verbose
```

#### Show technology usage statistics
```bash
python3 portfolio_cli.py tech
```

#### Find projects by keyword
```bash
python3 portfolio_cli.py find Python
python3 portfolio_cli.py find "machine learning"
```

#### Validate project data
```bash
python3 portfolio_cli.py validate
```

#### Export to JSON
```bash
python3 portfolio_cli.py export -o my_projects.json
```

#### Show portfolio statistics
```bash
python3 portfolio_cli.py stats
```

## Features

### Data Extraction
- Automatically parses project sections from HTML
- Extracts titles, descriptions, and technologies
- Handles various HTML formatting patterns

### Validation
- Checks for required fields (title, description, technologies)
- Validates content length
- Reports missing or problematic data

### Technology Analysis
- Counts technology usage across projects
- Identifies most common skills/tools
- Helps with portfolio optimization

### Export/Import
- JSON format for easy editing
- Preserves all project metadata
- Compatible with external tools

## Project Data Structure

Each project in the JSON file has the following structure:

```json
{
  "id": "project1",
  "title": "PROJECT TITLE",
  "description": "Detailed description of the project...",
  "technologies": ["Python", "JavaScript", "HTML"]
}
```

## Use Cases

1. **Portfolio Maintenance**: Keep project data organized and validate completeness
2. **Technology Tracking**: Analyze which technologies are most prominent
3. **Content Management**: Easy search and filtering of projects
4. **Data Export**: Extract data for use in other applications or analysis
5. **Quality Assurance**: Ensure all projects have proper descriptions and tech stacks

## Example Output

```
Portfolio Summary:
Total projects: 17

Most used technologies:
  Python: 8 projects
  C++: 5 projects
  JavaScript: 3 projects
  HTML: 2 projects
  CSS: 2 projects

No validation issues found!
```

## Contributing

To add new functionality:
1. Extend the `ProjectManager` class for new features
2. Add new commands to `portfolio_cli.py` for CLI access
3. Update this README with new usage examples

## License

This project is part of Tarek Nakkouch's portfolio website.