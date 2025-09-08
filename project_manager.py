#!/usr/bin/env python3
"""
Portfolio Project Manager

This script helps manage project data for the Tarek Nakkouch portfolio website.
It can extract project information from the HTML file, validate data, and 
generate project sections for easy maintenance.
"""

import json
import re
from typing import List, Dict, Any
from pathlib import Path


class ProjectManager:
    """Manages portfolio projects data and HTML generation."""
    
    def __init__(self, html_file: str = "projects.html"):
        self.html_file = Path(html_file)
        self.projects_data = []
        
    def extract_projects_from_html(self) -> List[Dict[str, Any]]:
        """Extract project information from the existing HTML file."""
        if not self.html_file.exists():
            print(f"HTML file {self.html_file} not found!")
            return []
            
        with open(self.html_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        projects = []
        
        # Find all project sections
        project_pattern = r'<section class="project-section" id="([^"]+)">(.*?)</section>'
        project_matches = re.findall(project_pattern, content, re.DOTALL)
        
        for project_id, project_content in project_matches:
            # Extract title
            title_match = re.search(r'<div class="warning-title">\s*([^<]+)', project_content)
            title = title_match.group(1).strip() if title_match else "Unknown"
            
            # Extract description
            desc_match = re.search(r'<p>([^<]+)</p>', project_content)
            description = desc_match.group(1).strip() if desc_match else ""
            
            # Extract technologies
            tech_pattern = r'<span class="tech-item">.*?>\s*([^<]+)</span>'
            technologies = re.findall(tech_pattern, project_content)
            technologies = [tech.strip() for tech in technologies]
            
            project = {
                "id": project_id,
                "title": title,
                "description": description,
                "technologies": technologies
            }
            projects.append(project)
        
        self.projects_data = projects
        return projects
    
    def save_projects_to_json(self, filename: str = "projects_data.json"):
        """Save extracted project data to JSON file."""
        output_file = Path(filename)
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.projects_data, f, indent=2, ensure_ascii=False)
        print(f"Project data saved to {output_file}")
    
    def load_projects_from_json(self, filename: str = "projects_data.json"):
        """Load project data from JSON file."""
        input_file = Path(filename)
        if not input_file.exists():
            print(f"JSON file {input_file} not found!")
            return False
            
        with open(input_file, 'r', encoding='utf-8') as f:
            self.projects_data = json.load(f)
        print(f"Loaded {len(self.projects_data)} projects from {input_file}")
        return True
    
    def generate_project_html(self, project: Dict[str, Any]) -> str:
        """Generate HTML for a single project."""
        tech_items = []
        for tech in project['technologies']:
            # Simple mapping for common technologies to icons
            icon_map = {
                'Python': 'fab fa-python',
                'JavaScript': 'fab fa-js-square',
                'React': 'fab fa-react',
                'HTML': 'fab fa-html5',
                'CSS': 'fab fa-css3-alt',
                'TensorFlow': 'fas fa-brain',
                'ML': 'fas fa-brain',
                'AI Analysis': 'fas fa-robot',
                'Neural Networks': 'fas fa-project-diagram',
                'WebSockets': 'fas fa-network-wired',
                'Scapy': 'fas fa-network-wired',
                'NLP': 'fas fa-brain',
                'Bluetooth': 'fab fa-bluetooth',
                'Wireshark': 'fas fa-network-wired'
            }
            
            icon = icon_map.get(tech, 'fas fa-code')
            tech_items.append(f'<span class="tech-item"><i class="{icon}"></i> {tech}</span>')
        
        tech_html = '\n                                    '.join(tech_items)
        
        return f"""
                <!-- {project['title']} -->
                <section class="project-section" id="{project['id']}">
                    <div class="content-wrapper">
                        <div class="warning-box warning-active">
                            <div class="warning-content">
                                <div class="warning-title">
                                    {project['title']}
                                </div>
                                <p>{project['description']}</p>
                                <div class="tech-list">
                                    {tech_html}
                                </div>
                            </div>
                        </div>
                    </div>
                </section>"""
    
    def validate_projects(self) -> List[str]:
        """Validate project data and return list of issues."""
        issues = []
        
        for i, project in enumerate(self.projects_data):
            # Check required fields
            if not project.get('title'):
                issues.append(f"Project {i+1}: Missing title")
            if not project.get('description'):
                issues.append(f"Project {i+1}: Missing description")
            if not project.get('technologies'):
                issues.append(f"Project {i+1}: No technologies listed")
            
            # Check for reasonable lengths
            if len(project.get('description', '')) < 10:
                issues.append(f"Project {i+1}: Description too short")
            if len(project.get('description', '')) > 500:
                issues.append(f"Project {i+1}: Description might be too long")
        
        return issues
    
    def print_summary(self):
        """Print a summary of the projects."""
        print(f"\nPortfolio Summary:")
        print(f"Total projects: {len(self.projects_data)}")
        
        # Technology frequency
        tech_count = {}
        for project in self.projects_data:
            for tech in project.get('technologies', []):
                tech_count[tech] = tech_count.get(tech, 0) + 1
        
        if tech_count:
            print("\nMost used technologies:")
            sorted_tech = sorted(tech_count.items(), key=lambda x: x[1], reverse=True)
            for tech, count in sorted_tech[:5]:
                print(f"  {tech}: {count} projects")
        
        # Validation issues
        issues = self.validate_projects()
        if issues:
            print(f"\nValidation issues found:")
            for issue in issues:
                print(f"  - {issue}")
        else:
            print("\nNo validation issues found!")


def main():
    """Main function to demonstrate the script functionality."""
    print("Portfolio Project Manager")
    print("=" * 30)
    
    manager = ProjectManager()
    
    # Extract projects from HTML
    print("Extracting projects from projects.html...")
    projects = manager.extract_projects_from_html()
    
    if projects:
        print(f"Successfully extracted {len(projects)} projects!")
        
        # Save to JSON for easy editing
        manager.save_projects_to_json()
        
        # Print summary
        manager.print_summary()
        
        # Show first project as example
        if projects:
            print(f"\nExample project data:")
            print(f"Title: {projects[0]['title']}")
            print(f"Technologies: {', '.join(projects[0]['technologies'])}")
    else:
        print("No projects found in HTML file.")


if __name__ == "__main__":
    main()