# About EasyCharts
This web application was made in order to ease the task of opening an Excel sheet and manually putting in data and then making a graph afterwards, with my solution you can add data to a graph which then dynamically updates in real time. This causes for less stress when needing to visualize something quick and don't want to make a whole Excel form to then convert data to view a chart. Note that at the current version V1.0 the app is very barebones and limited in the input size but this will change with future iterations.

<a href="http://www.easychartsapp.com/"><img src="https://img.shields.io/badge/Link-Easy_Charts-2ea44f?style=for-the-badge" alt="Link - Easy Charts"></a>
## Technology Used :hammer_and_wrench:

Frontend :gear:| Description|
-------|------------|
CSS    | Everything within the pages were styled using CSS, the design again is very minimilistic but clean and easy to use. Also, used it as a way to make it responsive to phones and other devices. 
Django + Bootstrap| Visual aspects such as the textfield and button elements.
HTML   | Stores the Home/About pages, also used it to template tag all the necessary elements such as displaying the weather conditions which I defined via the Django application.
JavaScript | Used to implement the basic functionality of the graph when the user ineracts with it, the form is posted via a mthod which then appends the given data to the JavaScript chart to dynamically display the given infomation.

Backend :toolbox:| Description|
-------|------------|
Django | Django is a well known Python backend web framework which I used to gather all the necessary information. Mainly used for template tagging and connecting all the HTML pages as well as migrating my project to a database. Also used as a form of site/token protection from malicious intruders CSRF.
Python | All the script was written in Python alongside Django for backend implementation primarily functions regarding the logic for how the chart is displayed on the HTML while using Chart.JS - [https://www.chartjs.org](https://www.chartjs.org).
[ChartJS](https://www.chartjs.org/) | Used to display the accurate dynamic updates of different charts within its' database. I then used the provided data to take in custom values from user input.
SQLLite | Used SQL to save save user input within the database which can then be retrieved thus being able to see the dynamic graph changes in real time. The database can also be resetted using the "Reset" button within the input area.

Libraries :books:| Description|
-------|------------|
whitenoise| Due to the fact Django does not have a way of supporting static files into production, whitenoise clears this barrier by placing all the required information into it's own separate folder which the web host (Heroku) can read from and apply any new changes.
gunicorn| [Gunicorn](https://github.com/benoitc/gunicorn) known as 'Green Unicorn' is a Python specific web server gateway. I used it as a way to pass requests data to my web application all through Heroku.

Web-services :spider_web:| Description|
-------|------------|
Heroku | Heroku is a cloud platform for hosting and maintaining website information which I used to later connect the platform with GoDaddy. 
GoDaddy| Domain was registered from GoDaddy alongside all DNS setup.

# Visual Example
<img width="1260" alt="Screen Shot 2023-01-11 at 1 18 10 PM" src="https://user-images.githubusercontent.com/48189579/211886280-7d3e9966-9ef7-4826-840d-e1dfa9add071.png">

