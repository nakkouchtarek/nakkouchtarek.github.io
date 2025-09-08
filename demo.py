#!/usr/bin/env python3
"""
Demo script showing portfolio management capabilities.
This script demonstrates various features of the project manager.
"""

from project_manager import ProjectManager


def demo():
    """Run a demonstration of the portfolio management features."""
    print("🚀 Portfolio Management Demo")
    print("=" * 50)
    
    # Initialize manager
    manager = ProjectManager()
    
    # Extract data
    print("\n📊 Extracting project data from HTML...")
    projects = manager.extract_projects_from_html()
    print(f"   Found {len(projects)} projects!")
    
    # Show some statistics
    print("\n📈 Portfolio Statistics:")
    tech_count = {}
    total_projects = len(projects)
    
    for project in projects:
        for tech in project.get('technologies', []):
            tech_count[tech] = tech_count.get(tech, 0) + 1
    
    print(f"   • Total projects: {total_projects}")
    print(f"   • Unique technologies: {len(tech_count)}")
    
    # Top technologies
    top_tech = sorted(tech_count.items(), key=lambda x: x[1], reverse=True)[:3]
    print("   • Top 3 technologies:")
    for tech, count in top_tech:
        percentage = (count / total_projects) * 100
        print(f"     - {tech}: {count} projects ({percentage:.1f}%)")
    
    # Project categories
    print("\n🏷️ Project Categories:")
    categories = {
        'Security/Cybersecurity': ['CYBER', 'MALWARE', 'SPOOFER', 'SNIFFER', 'MISP'],
        'Web Development': ['WEB', 'MOVIE', 'INTERNSHIP', 'KAHOOT'],
        'Systems Programming': ['OS', 'PROCESS', 'VIRTUAL', 'LANGUAGE'],
        'Machine Learning/AI': ['DIGIT', 'RECOMMENDATION', 'AI', 'NEURAL']
    }
    
    for category, keywords in categories.items():
        count = 0
        for project in projects:
            if any(keyword in project['title'].upper() for keyword in keywords):
                count += 1
        if count > 0:
            print(f"   • {category}: {count} projects")
    
    # Show a sample project
    if projects:
        print(f"\n📝 Sample Project Details:")
        sample = projects[0]
        print(f"   Title: {sample['title']}")
        print(f"   Technologies: {', '.join(sample['technologies'][:3])}{'...' if len(sample['technologies']) > 3 else ''}")
        print(f"   Description: {sample['description'][:100]}...")
    
    # Validation check
    print(f"\n✅ Data Validation:")
    issues = manager.validate_projects()
    if issues:
        print(f"   Found {len(issues)} issues to review")
        for issue in issues[:3]:  # Show first 3 issues
            print(f"   - {issue}")
    else:
        print("   All projects pass validation!")
    
    # Save data
    print(f"\n💾 Data Export:")
    manager.save_projects_to_json("demo_projects.json")
    print("   Projects saved to demo_projects.json")
    
    print(f"\n🎉 Demo complete! Use 'python3 portfolio_cli.py --help' for more options.")


if __name__ == "__main__":
    demo()