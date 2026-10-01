# Set of skills already known by the student
skills = {"Python", "Java", "HTML"}

# Add one new skill using add()
skills.add("CSS")

# Add several new skills using update()
skills.update({"SQL", "C++", "JavaScript"})

print("Student Skills:", skills)

# Another set of skills
new_skills = {"Python", "SQL", "React", "JavaScript"}

# Union
print("Union:", skills.union(new_skills))

# Intersection
print("Intersection:", skills.intersection(new_skills))

# Difference
print("Difference:", skills.difference(new_skills))
