# **Grocery Shopping List**

[Live Site]()

![Responsive view of Nourish and Lift on all devices](")

## **Introduction**
Welcome to Grocery Shopping List.

Grocery Shopping List is my fourth and second to last project, part of the Code Institute, Full Stack Web Developer Course.

The purpose of this website is to make a smart and easy to use shopping list that the user can modify to suit their shopping behaviours.
The technologies used for this project are HTML, CSS, JavaScript, Python, and Django. Allauth handles the user registration and login, and ElephantSQL as a relational database.
---

## **UXD - User Experience Design**

The planning that went into this project largely emerged from my own dissatisfaction with shopping apps.

So with that in mind and with some interviews i made the choice to design a easy to use app.

The planning of the project is broken into 5 planes,

- The Strategy Plane
- The Scope Plane
- The Structure Plane
- The Skeleton Plane
- The Surface Plane
---

## **The Strategy Plane**

### **Creator Goals**
- As a creator, I want the site to be easy to navigate.
- As a creator, I want to allow users to sort the list after their needs.

#### **User Stories**
- As a user, I want to be able to sign up, so that I can have my personal shopping list and categories.
- As a user, I want to be able to see confirmations when tasks are done, so that I can confirm that they were successful.
- As a user, I want to be able to add multiple items, so that i don't need to return to the list page everytime and save time.
- As a user, I want to be able to add a brand to my item, so that i specify what item i want.
- As a user, I want to be able to add a quantity to my item, so that know how much i need.
- As a user, I want to be able to edit items, so that i can change it without deleting.
- As a user, I want to be able to add my own categories, so that i personalize it after my needs.
- As a user, I want to be able to manage my categories, so that i add more and delete the ones i don't want anymore.
- As a user, I want to be able to toggle the items as i pick them up, so that i can see what items are left to pick.
- As a user, I want to be able to sort my list the way i want, so that i can specialize it after my needs.
- As a user, I want to be able to delete the list, so that i can start from scratch the next time.

My user stories where obtained from my own personal experiences and interviews. 

---

## **The Scope Plane**

To be sure that my project where launched with a ready to use site i opted to divide my project into three phases.

**Phase 1**
- A project that would be good enough to use.
    - Home Page with an introduction .
    - Navbar allowing the user to navigate to different pages.
    - Shopping list view to see the items. 
    - Page to add and edit items.
    - The ability to delete items and list.
    - Sign up and log in function

**Phase 2**
- Building upon the Phase 1 project with additional features.
    - User specific categories
    - Modals to ensure the user are sure to delete items
    - Keep picked items under a new header to separate the items

**Phase 3**
- My final planned phase would focus on user registration and accounts
    - Sign up with social media accounts
    - Password recovery
---

## **The Structure Plane**

#### **Colors**

For this project i choosed to only work with two different colors. This because i wanted the site to feel clean and focus should be on the functionality.

#212529
- I choosed this color for all all details on the page, such as navbar, footer, buttons and the headings of the tables. I like the dark grey blueish color. 
The color is taken from the bootstrap dark color the the table head. 

#FAFAFA
- The off-white color was used for the background color and for text. The off-white color have a nice contrast to my other color without being to bright as a background. 

#### **Fonts**

- For this project i opted to go with the standard font. This because it suited the easy and minimalistic approach i went in this project.

#### **Images**


#### **Key Models**

**ShoppingItem**
- The Shopping item model is the main model to add items to the shopping list.
- It hold all the important information about the item. 
- The item is connected to the imported user model.

**Category**
- The category model holds the information about the category
- The category is connected to the imported user model, to make sure that the user have their own categories.
---

## **The Skeleton Plane**

I made some changes as the project advanced, but this was my plan going into the project. 
I wanted the computer and mobile version to be as close to eachother as possible. 

So this is my basic layout before starting the project.

![Site Wireframe](docs/wireframes.JPG "Image of the wireframes")
---

## **The Surface Plane**

### **Features**

*Features present across the project,*

**Navigation Bar**
- Navbar is implemented on every page and is fully responsive across all resolutions.
- Users can navigate across the site freely as long as they are signed in.

![Project Navigation Bar](docs/navbar.png "Image of the navigation bar")

**Introduction**
- Home page features an introduction to notify users to welcome them and explain the purpose of the site.

![Project Introduction](docs/intro.png "Image of the Introduction")

**Add item page**
- Add item page, where the user insert all the information about the item they want to add to the list.

![Add Item](docs/additem.png "Image of add item page")

**Edit item page**
- Users can edit already added items to the list.

![Edit Item](docs/edititem.png "Image of the edit item page")

**Category**
- Users can add and manage their categories in this page

![Category](docs/categories.png "Image of category page")

**Shopping List**
- The user can view their added items in this list view.
- The user can easy see what items they have picked and what is left to pick.
- All the table heads are sortable.
- A button to reset the list when the user are done.

![Shopping List](docs/shoppinglist.png "Image of Shopping List page.")

**Delete Modal**
- A modal to ensure that the user are sure to delete the item or list.

![Delete Modal](docs/modal.png "Image of the delete modal")

**Footer**
- Footer with social media links that opens in new tabs.

![Footer](docs/footer.png "Image of the footer")
---

## **Technologies Used**

- [Python](https://www.python.org/) 
    - The following Python modules were used on this project, 
    - asgiref==3.5.2
    - cloudinary==1.30.0
    - dj-database-url==1.0.0
    - dj3-cloudinary-storage==0.0.6
    - Django==3.2.16
    - django-allauth==0.51.0
    - django-filter==22.1
    - gunicorn==20.1.0
    - oauthlib==3.2.2
    - psycopg2==2.9.5
    - PyJWT==2.6.0
    - python3-openid==3.2.0
    - pytz==2022.6
    - requests-oauthlib==1.3.1
    - sqlparse==0.4.3

- [ElephatnSQL](https://www.elephantsql.com/)

- [Allauth](https://django-allauth.readthedocs.io/en/latest/)
 
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)

- [CSS](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/CSS_basics)

- [Bootstrap](https://getbootstrap.com/)

- [jQuery](https://jquery.com/)

- [Font Awesome](https://fontawesome.com/)

- [Google Developer Tools](https://developers.google.com/web/tools/chrome-devtools)

- [Github](https://github.com/)

- [Gitpod](https://www.gitpod.io/)

- [Balsamiq](https://balsamiq.com/)

- [Grammarly](https://www.grammarly.com/)

---

## **Testing**

Link to the Testing Document
- [TESTING.md](https://github.com/Harry-Leepz/Nourish-and-Lift/blob/main/docs/TESTING.md)
---

## **Deployment**

The master branch of this repository is the most current version and has been used for the deployed version of the site.

The Code Institiue student template was used to create this project.

[Code Institute Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)

- Click the *Use This Template* button.
- Give your repository a name, and description if you wish.
- Click the *Create Repository from Template* to create your repository. 
- Click the *Gitpod* button to create a gitpod workspace, this can take a few minutes.
- When working on project using Gitpod, please open the workspace from Gitpod, this will open your previous workspace rather than creating a new one.
Use the following commands to commit your work, 
- `git add . ` - adds all modified files to a staging area.
- `git commit -m "A short message exlaining your commit"` - commits all changes to a local repository.
- `git push` - pushes all your commited changes to your Github repository.


**Creating a Clone**

1. From the repository, click *Code*
2. In the *Clone >> HTTPS* section, copy the clone URL for the repository
3. In your local IDE open Git Bash
4. Change the current working directory to the location where you want the cloned directory to be made
5. Type `git clone`, and then paste the URL you copied in Step 2 - ``git clone https://github.com/Harry-Leepz/Nourish-and-Lift.git``
6. Set the following values in a `env.py` file.
```
import os

os.environ.setdefault("SECRET_KEY", "<app secret key of your choice>")
os.environ.setdefault("DEVELOPMENT", "True")
os.environ["CLOUDINARY_URL"] = "cloudinary key"
```

7. Install the project requirements - `pip3 install requirements.txt`
8. Apply database migrations - `python manage.py migrate`
9. Create a superuser - `python manage.py createsuperuser`
10. The project can be run with the following - `python manage.py runserver`

**Heroku Deployment**

1. Log into Heroku
2. Create a new app, choose a location closest to you
3. Search for Heroku Postgres from the resources tab and add to your project
4. Make sure to have `dj_database_url` and `psycopg2` installed.
```
pip3 install dj_database_url
pip3 install psycopg2
```
5. Login to the Heroku CLI - `heroku login -i`
6. Run migrations on Heroku Postgres - `heroku run python manage.py migrate`
7. Create a superuser - `python manage.py createsuperuser`
8. Install `gunicorn` - `pip3 install gunicorn`
9. Create a requirements.txt file - `pip3 freeze > requirements.txt`
10. Create a `Procfile` (note the capital P), and add the following,
```
web: gunicorn moose_juice.wsgi:application
```
11. Disable Heroku from collecting static files - `heroku config:set DISABLE_COLLECTSTATIC=1 --app <your-app-name>`
12. Add the hostname to project settings.py file
```
ALLOWED_HOSTS = ['<you-app-name>.herokuapp.com', 'localhost']

```
13. Connect Heroku to you Github, by selecting Github as the deployment method and search for the github repository and pressing `connect`
14. In Heroku, within settings, under config vars select `Reveal config vars`
15. Add the following, 
```
DATABASE_URL =	<added by Heroku when Postgres installed>
DISABLE_COLLECTSTATIC =	1 
SECRET_KEY = <your variable here>
```
16. Go back to the Deploy tab and under Automatic deploys choose `Enable Automatic Deploys`
17. Back in your CLI add, commit and push your changes and Heroku will automatically deploy your app
```
git add .
git commit -m "Initial commit"
git push
```
18. Your deployed site can be launched by clicking `Open App` from its page within Heroku.

---