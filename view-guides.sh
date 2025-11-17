#!/bin/bash
# Helper script to view all guides

echo "📚 DSA FAANG Preparation Guides"
echo "================================"
echo ""
echo "Choose a guide to view:"
echo ""
echo "GETTING STARTED:"
echo "  1) Python Essentials"
echo "  2) Absolute Beginner"
echo "  3) Quick Start"
echo "  4) Pattern Recognition"
echo "  5) How to Think"
echo "  6) Decision Tree"
echo "  7) Complexity Guide"
echo ""
echo "PLANNING:"
echo "  8) Study Planner"
echo "  9) Revision System"
echo " 10) Progress Tracker"
echo " 11) Common Mistakes"
echo " 12) Cheat Sheet"
echo ""
echo "FAANG PREP:"
echo " 13) System Design ⭐"
echo " 14) Behavioral Prep"
echo " 15) FAANG Roadmap"
echo " 16) Mock Questions (Real interviews!)"
echo " 17) Company Questions"
echo " 18) Advanced Strategies"
echo ""
read -p "Enter number (1-18): " choice

cd /home/user/dsa/neetcode

case $choice in
    1) cat 00-getting-started/PYTHON_ESSENTIALS.md ;;
    2) cat 00-getting-started/ABSOLUTE_BEGINNER.md ;;
    3) cat 00-getting-started/QUICK_START.md ;;
    4) cat 00-getting-started/PATTERN_RECOGNITION.md ;;
    5) cat 00-getting-started/HOW_TO_THINK.md ;;
    6) cat 00-getting-started/DECISION_TREE.md ;;
    7) cat 00-getting-started/COMPLEXITY_GUIDE.md ;;
    8) cat 00-planning/STUDY_PLANNER.md ;;
    9) cat 00-planning/REVISION_SYSTEM.md ;;
    10) cat 00-planning/PROGRESS_TRACKER.md ;;
    11) cat 00-planning/COMMON_MISTAKES.md ;;
    12) cat 00-planning/CHEAT_SHEET.md ;;
    13) cat 00-faang-prep/SYSTEM_DESIGN.md ;;
    14) cat 00-faang-prep/BEHAVIORAL_PREP.md ;;
    15) cat 00-faang-prep/FAANG_ROADMAP.md ;;
    16) cat 00-faang-prep/MOCK_QUESTIONS.md ;;
    17) cat 00-faang-prep/COMPANY_QUESTIONS.md ;;
    18) cat 00-faang-prep/ADVANCED_STRATEGIES.md ;;
    *) echo "Invalid choice" ;;
esac
