(1) Instructions for Running Code: 

**The commands are for a windows operating system
1. Open the GitHub repository and download the files
2. You can optionally create a virtual environment and download Djanjo using the following commands (https://docs.djangoproject.com/en/3.0/topics/install/#installing-official-release)
  python -m venv tutorial-env
  tutorial-env\Scripts\activate.bat
  python -m pip install Django
3. In the directory structures there are 2 mysite folders, I will be referring to the outer level as the outer mysite folder and the inner level as the inner mysite folders
Using the command prompt console, enter (cd) into the outer mysite folder, here is an example of the path, (where virtualPenn is the name of the running virutal environment):
  (virtualPenn) C:\Users\anush\Documents\GitHub\DjangoInstagram\ActualPennInstaApp\mysite> 
4. Run the server using the following command:
  python manage.py runserver
5. Open a web browser, and type the following address: 
http://localhost:8000/accounts/login/

(2) Known Bugs - There are no known bugs that I could identify!

(3) Functionality - I was able to complete the signup, login, and create post functionalities. I also created the page that allows a user to view all of the posts on the blog. Due to time constraint I was unable to finish the functionality to view all of the user's own posts and the functionality that allows them to delete their own posts. 

(4) Any Additional Challenges - I did not finish any of the listed additional challenges. 

(5) General Thoughts - As someone who has never used Python or Django before I thought it was very interesting working with a framework and the SQLite Database! 