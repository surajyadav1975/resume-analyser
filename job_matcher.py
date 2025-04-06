def suggest_matching_jobs(skills, resume_text=""):
    skills = set(skill.lower() for skill in skills)
    resume_text = resume_text.lower()

    job_roles = [
        {
            "title": "Android Developer",
            "required_keywords": ["android", "android studio", "android sdk", "java", "kotlin", "xml"],
        },
        {
            "title": "iOS Developer",
            "required_keywords": ["ios", "swift", "xcode", "objective-c"],
        },
        {
            "title": "Full Stack Developer",
            "required_keywords": ["react", "node.js", "express", "mongodb"],
        },
        {
            "title": "Frontend Developer",
            "required_keywords": ["react", "html", "css", "javascript"],
        },
        {
            "title": "Backend Developer",
            "required_keywords": ["node.js", "express", "sql", "mongodb", "django"],
        },
        {
            "title": "Machine Learning Engineer",
            "required_keywords": ["python", "tensorflow", "scikit-learn", "numpy"],
        },
        {
            "title": "Data Scientist",
            "required_keywords": ["pandas", "matplotlib", "python", "sql", "scikit-learn"],
        },
        {
            "title": "Data Analyst",
            "required_keywords": ["excel", "sql", "tableau", "python"],
        },
        {
            "title": "UI/UX Designer",
            "required_keywords": ["figma", "adobe", "photoshop", "illustrator"],
        }
    ]

    results = []

    for role in job_roles:
        role_skills = set(role["required_keywords"])
        matched_skills = role_skills & skills
        missing_skills = role_skills - skills

        keyword_boost = any(keyword in resume_text for keyword in role_skills)

        match_percent = (len(matched_skills) / len(role_skills)) * 100

        # Only include if there's at least one matched skill
        if matched_skills:
            total_score = match_percent + (10 if keyword_boost else 0)
            results.append({
                "role": role["title"],
                "matched_skills": list(matched_skills),
                "missing_skills": list(missing_skills),
                "match_percent": round(total_score),
                "message": "You're almost there! Learn these skills to boost your profile." if missing_skills else "Great fit! You're ready to apply."
            })

    results.sort(key=lambda x: x["match_percent"], reverse=True)
    return results
