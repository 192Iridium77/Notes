GOOGLE CLOUD:

$ gcloud components install app-engine-python
$ gcloud components remove COMPONENT_ID
$ gcloud components update
$ gcloud config list
$ gcloud init # use to tie new distribution to your google cloud
$ gcloud auth login # use if gcloud permission is denied
$ gcloud compute ssh instance-1 # accesses cloud by ssh, passphrase empty
$ gcloud compute instances create instance-1 --address [IP_ADDRESS] # create new address
$ gcloud compute instances describe instance-1 # checks instance config
$ gcloud compute instances delete-access-config instance-1 --access-config-name External\ NAT
$ exit # if this doesn't work, try CTRL-D

GCLOUD UPLOAD:
$ echo '<!doctype html><html><body><h1>Hello World!</h1></body></html>' | sudo tee /var/www/html/index.html
$ gcloud compute copy-files [LOCAL_FILE_PATH] [INSTANCE_NAME]:~/
$ cd /var/www
$ git clone <your-git-url>

INSTALL:

$ sudo apt-get install python-pip
$ pip install --user Flask
$ sudo apt-get install apache2
$ sudo apt-get install libapache2-mod-wsgi # Web Server Gateway Interface
$ sudo apt-get install git

NOTES:

Adress: 104.154.166.62 (ephemeral)
** When creating a VM instance, please make sure you tick allow HTTP access...

GITHUB:

url: https://github.com/192Iridium77/firstapp
$ cd FirstFlaskApp
$ git init # initialize new repos
# create a new repo on git!
$ git remote add origin <your-git-url> # link repos to remote git repos
# origin is the alias for the repo on your system
$ git config --global user.email "matt.martin0108@gmail.com"
$ git config --global user.name "195Iridium77" pw inf.
$ git add hello.py # adds new or modified files to repos
$ git commit -m "Initial commit" # commit takes snapshot of project to local machine
$ git push -u origin master # make sure to commit before you push
# -u option: set up-stream tracking reference for up to date / sucessfully pushed branches
# master is the branch name
$ git pull origin master --allow-unrelated-histories # used in VPS, also used to pull new readme, the tag is now needed since there was an update
$ cd /var/www
$ git clone <your-git-url>
$ git stash save --keep-index  # remove all local changes from your working copy
# save is the default action if you use git stash
$ git stash drop
$ git status  # display information
$ git checkout -- <file>  # discard file changes

$ git stash pop  # takes the stashed work, and applies it ontop of your workign directory (opposite of save)
$ get stash apply  # same as pop but doesn't take from the stash stack
$ git stash show  # to see what's in your stash

GIT BRANCHES:

$ git branch post-requests  # create new branch with given name
$ git checkout post-requests # switch branch
$ git checkout-b post-requests # does both the above in one step
# To revert changes:
$ git add headlines.py
$ git add templates/home.html
$ git commit –m "POST requests"
$ git checkout master


WSGI:

$ vim hello.wsgi  # in /var/www/firstapp
> import sys
> sys.path.insert(0, "/var/www/firstapp") # imports application into PATH system
> from hello import app as application

APACHE:

$ sudo service apache2 restart
$ cd /etc/apache2/sites-available
$ nano hello.conf

# allows to serve multiple sites from a single server

<VirtualHost *>
        ServerName example.com

        WSGIDaemonProcess hello user=matt group=matt threads=5
        WSGIScriptAlias / /var/www/firstapp/hello.wsgi
        <Directory /var/www/firstapp>
                WSGIProcessGroup hello
                WSGIApplicationGroup %{GLOBAL}
                require all granted
        </Directory>
</VirtualHost>


for help: http://flask.pocoo.org/docs/0.10/deploying/mod_wsgi/.

$ sudo a2dissite 000-default.conf # disables original apache site
$ sudo a2ensite hello.conf # enables yours
$ sudo service apache2 reload
# make sure you use sudo...
# if failed:
$ sudo tail -fn 20 /var/log/apache2/error.log

VIRTUALENV:

$ sudo virtualenv venv
$ source venv/bin/activate
$ deactivate

STEPS:

1. Create ubuntu instance with google cloud
2. gcloud compute ssh instance-1
3. install software
4. write Flask application on local machine (eg. hello.py)
5. Test local Flask and VPS apache2
6. Make github account and repository
7. link local app to github
8. clone repository into VPS directory: /var/www
9. configure wsgi in /var/www
10. point apache2 to wsgi file using /etc/apache2/sites-available/hello.conf
11. Configure apache to serve flask app
12. restart apache2 server and hope it works

RSS:

Scientific American: http://rss.sciam.com/ScientificAmerican-Global?format=xml
New Atlas: http://feeds.feedblitz.com/newatlas&x=1 
Real Clear Science: http://www.realclearscience.com/index.xml
Live Science: http://www.livescience.com/home/feed/site.xml

JINJA:

# create a templates folder, place .html file within it
> from flask import render_template
# change function return statement:
> return render_template("home.html")
> render_template("home.html",title=first_article.get("title"),
published=first_article.get("published"),summary=first_article.get("summary"))
# Add double braces to html, seems like they need to be made 'safe' too:
    <h1>Headlines</h1>
    <strong>{{title}}</strong><br>
    <em>{{published}}</em><br>
    <p>{{summary | safe}}</p>
# Use Jinja Objects:
> render_template("home.html", article=first_article)
# access title and such:
    <h1>Headlines</h1>
    <strong>{{article.title | safe}}</strong><br>
    <em>{{article.published | safe}}</em><br>
    <p>{{article.summary | safe}}</p>

INPUT FUNCTIONALITY

+ from flask import request
- @app.route("/<publication>")
- def get_news(<parameters>)
+     if not query or query.lower() not in RSS_FEEDS:
        publication = "newatlas"
    else:
        publication = query.lower()
# the above lines are added to the get_news function
# enter localhost:5000/?publication=bbc into browser
# To change to POST:
- request.args.get("publication")
+ request.form.get("publication")
- @app.route("/")
+ @app.route("/", methods=['GET','POST'])  # decorators specify how the function gets
# accessed, either GET, POST or both. Only GET is enable by default
# change home.html's form parameters:
	<form action="/" method="POST">
	<input type='text' name='publication' placeholder="search" />
          <input type='submit' value='Submit' /><br>
        </form>

### From here on, refer to the headlines.py file for weather, currency, cookies and css

# XAMPP

$ sudo /opt/lampp/lampp start # runs apache and mysql, stop also works
# to start GUI:
$ cd /opt/lampp
$ sudo ./manager-linux.run (or manager-linux-x64.run)
# enter http://localhost to see if it's working
# note XAMPP is open, good for dev, not good for production environment
# must add MySQL root password, deny access to MYSQL daemon via network
# and change ProFTPD password from "lampp"
$ sudo /opt/lampp/lampp security
# if errors present:
$ tail -2 /opt/lampp/logs/error_log
# to keep XAMPP running on startup:
$ sudo ln -s /opt/lampp/lampp /etc/init.d/lampp
$ sudo update-rc.d lampp start 80 2 3 4 5 . stop 30 0 1 6 .
# you can improve PHP server speed with eAccelerator
# pwhints: phpMyAdmin - root | disp1right, mySQLroot - disp1right
# FTP pw, user daemon, pwhint -disp1right
# localhost/security dne anymore, it was destroying people's installation
# use security method above
# inside /opt/lampp folder, htdocs is where php and html files will be stored
# htdocs == www
# go to your phpMyAdmin on localhost, navigate to Databases tab and do your thing
# Can also write SQL commands in SQL tab
CREATE DATABASE members;
GRANT ALL
ON members.*
TO 'adrian'
IDENTIFIED BY 'stapler12';
# hit go, select the members database, go back to SQL
CREATE TABLE users (
user_id MEDIUMINT (6) UNSIGNED
AUTO_INCREMENT,
fname VARCHAR(30) NOT NULL,
lname VARCHAR(40) NOT NULL,
email VARCHAR(50) NOT NULL,
psword CHAR(40) NOT NULL,
registration_date DATETIME,
PRIMARY KEY (user_id)
);
# use above to create new table for this database

# MYSQL

$ mysql --help
# make sure mysql-server is installed, user: root, pw hint: disp1right
$ mysql -h localhost -u root -p
# you may omit localhost if the server is on your local machine
$ mysql  # connects to server anonymously
# CTRL-D to disconnect
SELECT VERSION(), CURRENT_DATE;
SELECT SIN(PI()/4), (4+1)*5;
SELECT NOW();
# works a lot like IPython
QUIT
SELECT USER() \c
# \c cancels a command, useful for multiple line commands
# '> "> `> indicates you've missed an end quote, you should probably \c
SHOW DATABASES;
# mysql database shows user privileges
https://github.com/nitso/colour-mysql-console
CREATE DATABASE menagerie;
USE menagerie
# or try:
$ mysql -h host -u user -p menagerie
SELECT DATABASE(); # shows which database you have selected
SHOW TABLES;
CREATE TABLE pet (name VARCHAR(20), owner VARCHAR(20), species VARCHAR(20), sex CHAR(1), birth DATE, death DATE);
DESCRIBE pet;
# make a pet.txt file containing one record per line, values separated by tabs
# dates entered in 'YYYY-MM-DD' format
# \N to provide Null values
LOAD DATA LOCAL INFILE '~/pet.txt' INTO TABLE pet;
SELECT * FROM pet;
# SELECT FROM WHERE is the pattern, WHERE may be ommited
DELETE FROM pet;
# deletes everything, use LOAD DATA... to input changed data
UPDATE pet SET birth = '1996-06-24' WHERE name = 'Bandit';
SELECT * FROM pet WHERE species = 'Cat';
# WHERE specifies which rows to display
SELECT * FROM pet WHERE (birth >= '2000-01-01' AND owner = 'Dad'); 
# the above works with OR aswell
SELECT name, species, owner FROM pet;
# displays columns
SELECT DISTINCT species FROM  pet;
# outputs only unique items
SELECT name, birth FROM pet ORDER BY birth;
# you can enforce case-senstive sort for a column:
SELECT name, birth FROM pet ORDER BY BINARY name;
SELECT name, birth FROM pet ORDER BY birth DESC; # sort descending
SELECT name, species, birth FROM pet ORDER BY species, birth DESC;
# this sorts by species and then birth order
SELECT name, birth, CURDATE(), TIMESTAMPDIFF(YEAR,birth,CURDATE()) AS age FROM pet;
SELECT name, birth, death, TIMESTAMPDIFF(YEAR,birth, death) AS age FROM pet WHERE death IS NOT NULL ORDER BY age;
SELECT name, birth, MONTH(birth) FROM pet;
# similar functions: YEAR() DAYOFMONTH()
SELECT name, birth FROM pet WHERE MONTH(birth) = MOD(MONTH(CURDATE()), 12) + 1;;
# MOD(_, 12) returns a number between 0 and 11
# CTRL+L clears the screen!
system clear;
SELECT 1 IS NULL, 1 IS NOT NULL;
# can't use ><= operators to test for NULL

$ mysqldump <login> <databasename> > file.sql  # use to export database

Domain reg:
username: em.live
pw:Omomo(
pin: mo

50.63.202.46
