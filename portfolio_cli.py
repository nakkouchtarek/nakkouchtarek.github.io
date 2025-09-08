#!/usr/bin/env python3
"""
Portfolio CLI Tool

Command-line interface for managing portfolio projects.
Provides easy commands to view, validate, and update project information.
"""

import argparse
import sys
from project_manager import ProjectManager


def cmd_list(args):
    """List all projects."""
    manager = ProjectManager()
    if manager.extract_projects_from_html():
        print(f"Found {len(manager.projects_data)} projects:\n")
        for i, project in enumerate(manager.projects_data, 1):
            print(f"{i:2d}. {project['title']}")
            if args.verbose:
                print(f"    ID: {project['id']}")
                print(f"    Tech: {', '.join(project['technologies'])}")
                print(f"    Description: {project['description'][:100]}{'...' if len(project['description']) > 100 else ''}")
                print()
    else:
        print("No projects found.")


def cmd_export(args):
    """Export projects to JSON."""
    manager = ProjectManager()
    if manager.extract_projects_from_html():
        manager.save_projects_to_json(args.output)
        print(f"Exported {len(manager.projects_data)} projects to {args.output}")
    else:
        print("No projects found to export.")


def cmd_validate(args):
    """Validate project data."""
    manager = ProjectManager()
    if manager.extract_projects_from_html():
        issues = manager.validate_projects()
        if issues:
            print("Validation issues found:")
            for issue in issues:
                print(f"  ❌ {issue}")
            return 1
        else:
            print("✅ All projects validated successfully!")
            return 0
    else:
        print("No projects found to validate.")
        return 1


def cmd_stats(args):
    """Show portfolio statistics."""
    manager = ProjectManager()
    if manager.extract_projects_from_html():
        manager.print_summary()
    else:
        print("No projects found.")


def cmd_tech(args):
    """Show technology usage statistics."""
    manager = ProjectManager()
    if manager.extract_projects_from_html():
        tech_count = {}
        for project in manager.projects_data:
            for tech in project.get('technologies', []):
                tech_count[tech] = tech_count.get(tech, 0) + 1
        
        if tech_count:
            print("Technology usage in portfolio:")
            sorted_tech = sorted(tech_count.items(), key=lambda x: x[1], reverse=True)
            for tech, count in sorted_tech:
                print(f"  {tech}: {count} project{'s' if count > 1 else ''}")
        else:
            print("No technologies found.")
    else:
        print("No projects found.")


def cmd_find(args):
    """Find projects by technology or keyword."""
    manager = ProjectManager()
    if manager.extract_projects_from_html():
        keyword = args.keyword.lower()
        matches = []
        
        for project in manager.projects_data:
            # Search in title, description, and technologies
            if (keyword in project['title'].lower() or 
                keyword in project['description'].lower() or
                any(keyword in tech.lower() for tech in project['technologies'])):
                matches.append(project)
        
        if matches:
            print(f"Found {len(matches)} project{'s' if len(matches) > 1 else ''} matching '{args.keyword}':")
            for project in matches:
                print(f"  • {project['title']}")
                if args.verbose:
                    print(f"    {project['description'][:100]}{'...' if len(project['description']) > 100 else ''}")
        else:
            print(f"No projects found matching '{args.keyword}'")
    else:
        print("No projects found.")


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Portfolio management CLI tool",
        epilog="Example: python portfolio_cli.py list --verbose"
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Available commands')
    
    # List command
    list_parser = subparsers.add_parser('list', help='List all projects')
    list_parser.add_argument('-v', '--verbose', action='store_true', 
                           help='Show detailed information')
    list_parser.set_defaults(func=cmd_list)
    
    # Export command
    export_parser = subparsers.add_parser('export', help='Export projects to JSON')
    export_parser.add_argument('-o', '--output', default='projects_data.json',
                             help='Output JSON file (default: projects_data.json)')
    export_parser.set_defaults(func=cmd_export)
    
    # Validate command
    validate_parser = subparsers.add_parser('validate', help='Validate project data')
    validate_parser.set_defaults(func=cmd_validate)
    
    # Stats command
    stats_parser = subparsers.add_parser('stats', help='Show portfolio statistics')
    stats_parser.set_defaults(func=cmd_stats)
    
    # Tech command
    tech_parser = subparsers.add_parser('tech', help='Show technology usage')
    tech_parser.set_defaults(func=cmd_tech)
    
    # Find command
    find_parser = subparsers.add_parser('find', help='Find projects by keyword')
    find_parser.add_argument('keyword', help='Keyword to search for')
    find_parser.add_argument('-v', '--verbose', action='store_true',
                           help='Show project descriptions')
    find_parser.set_defaults(func=cmd_find)
    
    args = parser.parse_args()
    
    if args.command is None:
        parser.print_help()
        return 1
    
    try:
        return args.func(args) or 0
    except Exception as e:
        print(f"Error: {e}")
        return 1


if __name__ == "__main__":
    sys.exit(main())