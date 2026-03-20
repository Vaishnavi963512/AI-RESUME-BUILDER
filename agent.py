def resume_agent(data):

    skills = data.get("skills", "").lower()
    experience = data.get("experience", "").lower()

    if "python" in skills or "developer" in skills:
        return "developer"

    elif "design" in skills:
        return "colorful"

    elif "manager" in experience:
        return "professional"

    elif "student" in experience:
        return "modern"

    else:
        return "minimal"