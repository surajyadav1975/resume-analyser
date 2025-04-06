import spacy
import re

nlp = spacy.load("en_core_web_sm")

def analyze_resume(text):
    doc = nlp(text.lower())
    text_lower = text.lower()

    # ✅ Extended keyword sets
    skills_keywords = [
        "swift", "objective-c", "xcode", "sqlite", "plist", "nsuserdefaults", "xml", "json", "rest", "soap",
        "python", "java", "c", "c++", "c#", "javascript", "typescript", "kotlin", "matlab", "r", "dart",
        "react", "next.js", "node.js", "express", "redux", "html", "css", "sass", "bootstrap", "tailwind", "wordpress",
        "flask", "django", "mongodb", "mysql", "postgresql", "sql", "firebase", "rest api", "graphql",
        "aws", "azure", "docker", "kubernetes", "jenkins", "nginx", "selenium", "git", "github",
        "pandas", "numpy", "scikit-learn", "tensorflow", "pytorch", "flutter"
    ]

    soft_skills_keywords = [
        "communication", "leadership", "problem-solving", "teamwork", "collaborate", "creative", 
        "analytical", "responsible", "organized", "adaptable", "debug", "design", "develop"
    ]

    strengths_keywords = [
        "excellent", "passionate", "dedicated", "motivated", "self-starter", "proactive", "fast learner"
    ]

    weaknesses_keywords = [
        "challenge", "struggle", "improve", "learning curve", "difficult", "weak", "lack"
    ]

    tools_keywords = [
        "xcode", "eclipse", "android studio", "genymotion", "invision", "axure", "adobe", "photoshop", 
        "illustrator", "indesign", "premiere pro", "after effects"
    ]

    # 🧠 Extracted info
    found_skills = set()
    found_soft_skills = set()
    found_tools = set()
    found_strength_traits = set()
    found_weakness_traits = set()

    # General word matching
    def keyword_matcher(keywords, destination_set):
        for kw in keywords:
            if re.search(rf'\b{re.escape(kw.lower())}\b', text_lower):
                destination_set.add(kw)

    keyword_matcher(skills_keywords, found_skills)
    keyword_matcher(soft_skills_keywords, found_soft_skills)
    keyword_matcher(tools_keywords, found_tools)
    keyword_matcher(strengths_keywords, found_strength_traits)
    keyword_matcher(weaknesses_keywords, found_weakness_traits)

    # 💪 Strength & ⚠️ Weakness Detection
    strengths = []
    weaknesses = []

    def detect(condition, strength_msg, weakness_msg):
        if condition:
            strengths.append(f"✅ {strength_msg}")
        else:
            weaknesses.append(f"⚠️ {weakness_msg}")

    detect(any(w in text_lower for w in ["team", "collaborated", "group", "teammates", "teamwork"]),
           "Mentions teamwork or collaboration",
           "No mention of teamwork")

    detect(any(w in text_lower for w in ["project", "built", "developed", "created", "engineered", "implemented"]),
           "Mentions projects or hands-on experience",
           "No specific project experience")

    detect(any(w in text_lower for w in ["led", "managed", "organized", "mentored", "headed"]),
           "Mentions leadership or initiative",
           "No leadership experience mentioned")

    detect(any(w in text_lower for w in ["solved", "debugged", "optimized", "troubleshooted", "problem-solving"]),
           "Mentions problem-solving skills",
           "No explicit problem-solving experience")

    detect(any(w in text_lower for w in ["communicated", "presented", "wrote", "documentation", "spoke", "client"]),
           "Mentions communication or documentation",
           "No communication skills highlighted")

    detect(any(w in text_lower for w in ["award", "achieved", "certification", "recognized", "honor"]),
           "Mentions certifications or achievements",
           "No achievements or certifications found")

    detect(any(w in text_lower for w in ["learned", "curious", "explored", "self-taught", "upskilled"]),
           "Mentions learning or self-improvement",
           "No learning or growth mindset evidence")

    detect(any(w in text_lower for w in tools_keywords),
           "Mentions relevant tools or design platforms",
           "No tools or platform usage highlighted")

    return {
        "skills": sorted(found_skills),
        "soft_skills": sorted(found_soft_skills),
        "tools": sorted(found_tools),
        "strength_traits": sorted(found_strength_traits),
        "weakness_traits": sorted(found_weakness_traits),
        "strengths_summary": strengths,
        "weaknesses_summary": weaknesses
    }
