#!/usr/bin/env python3
"""
Upload analysis sections to Archon MCP server
"""

import json
from pathlib import Path

# Document mappings
documents = [
    {
        "file": "01_executive_summary.md",
        "title": "Part 1: Executive Summary",
        "summary": "Overview of cursor-memory-bank analysis and Pydantic AI replication strategy"
    },
    {
        "file": "02_van_mode_workflow.md",
        "title": "Part 2: VAN Mode Workflow",
        "summary": "Detailed analysis of VAN mode initialization, complexity detection, and forced transitions"
    },
    {
        "file": "03_plan_creative_modes.md",
        "title": "Part 3: PLAN and CREATIVE Modes",
        "summary": "Analysis of planning and creative design workflows with lazy loading"
    },
    {
        "file": "04_lazy_loading_implementation.md",
        "title": "Part 4: Lazy Loading Deep Dive",
        "summary": "Technical deep dive into hierarchical rule loading and 78% token reduction"
    },
    {
        "file": "05_pydantic_ai_complete_code.md",
        "title": "Part 5: Pydantic AI Complete Code",
        "summary": "Full implementation code for all agents, orchestrator, and lazy loader"
    },
    {
        "file": "06_implementation_guide.md",
        "title": "Part 6: Implementation Guide",
        "summary": "Step-by-step setup guide, testing, and deployment instructions"
    },
    {
        "file": "07_comparison_conclusion.md",
        "title": "Part 7: Comparison & Conclusion",
        "summary": "Feature comparison, use case recommendations, and final analysis"
    }
]

# Project ID
PROJECT_ID = "0df6b7ed-4fef-4d1b-9b37-1e496099042b"

# Sections directory
SECTIONS_DIR = Path("analysis_sections")

# Generate MCP tool calls for each document
for doc in documents:
    filepath = SECTIONS_DIR / doc["file"]
    content = filepath.read_text()

    # Create structured content with markdown embedded
    content_json = {
        "markdown_content": content,
        "summary": doc["summary"],
        "part": doc["file"].split("_")[0],
        "file_reference": str(filepath)
    }

    print(f"Document: {doc['title']}")
    print(f"File: {doc['file']}")
    print(f"Size: {len(content)} characters")
    print(f"Content keys: {list(content_json.keys())}")
    print("-" * 60)

print("\nTo upload these to Archon, call manage_document for each with the content_json structure above.")
print(f"\nTotal documents: {len(documents)}")
