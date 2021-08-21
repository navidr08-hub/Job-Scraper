class JobCard:
    def __init__(self, title='something', location = 'something', company='something', type='something', description='something'):
        self.title = title
        self.location = location
        self.company = company
        self.type = type
        self.description = description

    #setters
    def set_title(self, title):
        self.title = title
    
    def set_location(self, location):
        self.location = location

    def set_company(self, company):
        self.company = company

    def set_type(self, type):
        self.type = type
    
    def set_description(self, description):
        self.description = description

# import os

# name = input('Please enter the name of the resume file you want to use\n(Must be a text file): ')

# os.chdir('C:\\Users\\Navid Rahman\\Desktop\\Web Scraping Project\\Resume_folder\\')

# print(os.getcwd())

# for file in os.listdir():
#     if file == name:
#         print('found!')
#         contents = open(name, 'r').readlines()

# class Resume:
#     def __init__(self, name, contents, skills, education):
#         self.name = name
#         self.contents = contents 
#         self.skills = skills
#         self.education = education

#     def set_name(self, name):
#         self.name = name
    
#     def set_contents(self, contents):
#         self.contents = contents

#     def set_skills(self, skills):
#         self.skills = skills

#     def set_education(self, education):
#         self.education = education
