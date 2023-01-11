# About Easy Charts
This web application was made in order to ease the task of opening an Excel sheet and manually putting in data and then making a graph afterwards, with my solution you can add data to a graph which then dynamically updates in real time. This causes for less stress when needing to visualize something quick and don't want to make a whole Excel form to then convert data to view a chart. Note that at the current version V1.0 the app is very barebones and limited in the input size but this will change with future iterations.

[![Link - Easy Charts](https://img.shields.io/badge/Link-Easy_Charts-3693F3?style=for-the-badge&logo=<svg+role%3D"img"+viewBox%3D"0+0+24+24"+xmlns%3D"http%3A%2F%2Fwww.w3.org%2F2000%2Fsvg"><title>iCloud<%2Ftitle><path+d%3D"M13.762+4.29a6.51+6.51+0+0+0-5.669+3.332+3.571+3.571+0+0+0-1.558-.36+3.571+3.571+0+0+0-3.516+3A4.918+4.918+0+0+0+0+14.796a4.918+4.918+0+0+0+4.92+4.914+4.93+4.93+0+0+0+.617-.045h14.42c2.305-.272+4.041-2.258+4.043-4.589v-.009a4.594+4.594+0+0+0-3.727-4.508+6.51+6.51+0+0+0-6.511-6.27z"%2F><%2Fsvg>)](https://www.easychartsapp.com/)
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
<img width="1674" alt="Screen Shot 2023-01-11 at 2 39 35 PM" src="https://user-images.githubusercontent.com/48189579/211901900-3e9e9a9d-0556-42aa-946a-906f368a5f71.png">

<img width="1674" alt="Screen Shot 2023-01-11 at 2 40 45 PM" src="https://user-images.githubusercontent.com/48189579/211902144-3feea4f3-d990-4a23-9031-76513f4f1b52.png">

