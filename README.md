# OurNoticeBoardv2.0 (<a href="https://demo-ournoticeboard.herokuapp.com">Demo</a>)

An Upgraded version of OurNoticeBoard app (github.com/rajujha373/OutNoticeBoard) which can be used as a virtual notice board for you and your colleagues.
Now you can decide which note shall be visible to others and which shall be just for you.

# Requirements (that shall be installed in your system)
1. Git 
2. virtualenv

# How to run in your local machine?

1. Firstly, clone the repository using the git shell <br>
<code>$ git clone https://github.com/rajujha373/OurNoticeBoardv2.0.git</code> <br>
2. Goto the base directory of the project <br>
<code>cd OurNoticeBoardv2.0 </code> <br>
3. Create a virtual environment and activate it. <br>
<code>$ virtualenv notesenv</code> <br>
<code>$ notesenv\Scripts\activate</code> <br>
4. Install the requirements for the project <br>
<code>$ pip install requirements.txt</code>  <br>
5. Now start the localhost server<br>
<code>$ python manage.py runserver</code> <br>

# Deployment settings (for heroku)

1. Replace the files (settings.py and wsgi.py) in the /notepad/ folder by the contents of /production_settings/
2. Ready for deployment
3. If you again want to use the app in your local machine, then just replace the same files by the files in /localhost_settings/.

# Screenshots

<img src="/screenshots/login.png">
&nbsp;
<img src="/screenshots/all.png">
&nbsp;
<img src="/screenshots/public.png">
&nbsp;
<img src="/screenshots/private.png">
&nbsp;
<img src="/screenshots/detail.png">
