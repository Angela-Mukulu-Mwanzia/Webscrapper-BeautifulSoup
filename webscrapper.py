#import beautifoulsoup
from bs4 import BeautifulSoup

# access website content, open then read as well as print
with open('samplewebsite.html','r') as html_file:
    Content = html_file.read()
    # print(Content)

#use beautifulsoup to make html website code pretty
    soup = BeautifulSoup(Content, 'lxml')
    # print(soup.prettify())

#grab specific information from website
    courses_html_tags =soup.find_all('h5')
    print(courses_html_tags)

#to display all courses names
    for course in courses_html_tags:
        print(course.text)

#to display course details
    course_cards =soup.find_all('div',class_='card')
    for course in course_cards:
        print(course.h5)
        course_name = course.h5.text
        course_price = course.a.text.split()[-1]

        print(course_name)
        print(course_price)

#makes details of the course into a sentence
        print(f'{course_name} costs {course_price}')