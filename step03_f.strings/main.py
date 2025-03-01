name : str = "Sharjeel"
id : int = 29333    
percentage : float = 80.5
onSite : bool = True


Student : str = f"""
Name: {name}
ID: {id}
Percentage: {percentage}
OnSite: {onSite}
"""

print(Student)

student : str = """
ID: {}
Name: {}
Percentage: {}
OnSite: {}
""".format(id, name, percentage, onSite)

print(student)
