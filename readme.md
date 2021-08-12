# Milestone Project Four

## Manage My Web
![Manage My Web](media/logo.png)

Welcome to Manage My Web, an eCommerce website that offers web design, development and SEO products both as individual 
products, as well as subscription based services.

For this project, I wanted to create the MVP (minimum viable product) of a project I could possibly continue to develop after finishing my studies with 
Code Institute. 

Further specific information on this project can be found below:

### Table of contents:
1. [Description](#Description),
2. [UX](#UX)
    1. [Logo](#Logo)
    2. [Wireframes](#Wireframes)
    3. [User Stories](#User-Stories) 
    4. [Information Architectures](#Information-Architectures)
    5. [Responsive Design](#Responsive-Design)
    6. [Frameworks](#Frameworks)
    7. [Typography](#Typography)
    8. [Colors](#Colors)
    9. [Icons](#Icons)
3. [Features](#Features)
    1. [Existing Features](#Existing-Features)
    2. [Future Features](#Future-Features)
4. [Technologies Used](#Technologies-Used)
5. [Testing](#Testing)
6. [Deployment](#Deployment)
    1. [Local Deployment](#Local-Deployment)
    2. [Remote Deployment](#Remote-Deployment)
7. [Credits](#Credits)
    1. [Media](#Media)
    2. [Content](#Content)
    3. [Acknowledgments](#Acknowledgments)

## **Description**
Manage My Web is an eCommerce store with Stripe integrated payment processing. This web application currently allows members, 
and non members use the main sections of this website without the need for membership. This allows Manage My Web sell products 
to any user. 

Adding to the fundamentals of this website, several user focussed features have been added to help provide functionality that aims to provide a better user experience.
Features such as chatbot, modals & user dashboard are all aimed at keeping customers 
informed, and updated. 

### **The Concept**
The plan that created Manage My Web was the fact that a lot of web development agencies simply create websites, but do not offer hosting, domains. Agencies also do not normally provide SEO services, but rather outsource this or simply offload it. Manage My Web aims to target that gap in the market.

Although individual "products" such as landing pages, and basic front end websites can be purchased as an individual item. Package deals or "plans" are available whereby a user will get all of the required services in one location, from web design to SEO. 

Although the scope of this project includes automation, the website currently is at or above its identified MVP point. Future developments will offload tasks that can be completed via automation, such as SEO reports of a specific webpage, among others.

---------------
## **UX**

This project is highly focussed on the main principles of UX design, including ease of navigation, bounce rate (readily available information), and functionality to promote quality user experience. Further UX features are listed below:


### 5 Planes of UX:
#### ***1. Strategy:***
> The strategy for this project is to produce a recipe database that users can browse and also promote products via an online store. 
> 
> Users will be able to browse products by filter (Category, price, name).
>
> Users will be able to search for products.
>
> Users will be able to create a profile and edit that profile.
>
> Users will be able to communicate with admins.
>
> Users will be able to rate purchased products.
>
> Users will be able to view previously purchased products.
>
> Users will be able to see the stage of development of their purchase (from order confirmation to being delivered).

#### ***2. Scope:***

*Functional Requirements:*
> 1. A user must be able to browse the website regardless of membership.
> 2. A user must be able to sign up.
> 3. A member must have a profile dedicated to them.
> 4. A member must be able to track previous orders.
> 5. Any user must be able to purchase products.
> 6. Users must be provided with contact information, and contact forms.
> 7. Users must be able to search, sort, and filter products.
> 8. Users must be able to view more about individual products.
> 9. Users must be able to quickly add a product directly to their cart from the general products page.
> 10. Users must be able to view, edit, and remove items in their cart.
> 11. Users must be provided with receipts after checkout.
> 12. Users must be provided with a policy page.
> 13. Users must be provided with a cookie consent popup on initial visit.
> 14. Users must be able to view tax rates. (currently set to Ireland)
> 15. Users must not have to click more than 4 times to take them from the homepage, to buying a product.


*Content Requirements:*
> 1. Content must be targetted to specific products and or web design & SEO.
> 2. Subscription based products must provide subscription explainer content.
> 3. Users be able to see their data on their dashboard.

#### ***3. Structure:***
> * A standard navigation menu available across the entire website. With exceptions:
>   1. A user not logged in will have the option to sign in, or login.
>   2. A logged in user will be able to log out, or view their profile.
>   3. A main search bar will provide users with a quick way to search for products.
>   4. All main links will be provided in a global header, and footer section.
>
> * Each screen should provide a limited amount, but quality information to a user to decrease information overload and promote good UX.
>
> * All content should be contained in blocks that allow for distinction between certain areas. 

#### ***4. Skeleton:***
> To create a structure for this website, key areas were identified. These areas will provide certain functionality, as well as user facing apps.
>
> Key areas were defined for the operation of this website, these areas are:
>   1. Products (both overall views, and individual view).
>   2. Profile / User Dashboard.
>   3. About Section.
>   4. Contact Section & webhook.
>   5. Cart.
>   6. Checkout.
>   7. Subscription Section.
>   7. Policy Section.
> 
> Initial wireframes were created, but through the evolution of this project, several designs have been changed, either due to designs not 
> fitting with the surrounding pages, or due to new features being added.
>
> You can view the wireframes for this project [here](#Wireframes)


#### ***5. Surface:***
> This project aims to provide users with a positive user experience which is aided through functionality, feedback and ease of use. 
>
> Users are prompted with messages, to show successful, unsuccessful, or informative feedback when users perform certain tasks, such as adding products to their cart, sending messages etc.
>
> Users are provided with form clarification tools that will help them in the event of form regex errors.
>
> Members are provided with a dashboard. Within this dashboard, order history shows the current status of an order, as well as order date, and if an order has been delivered, an order completion date.


### <ins>**_Logo_**</ins>
The logo for this project is based simply on a photo that was available via [Pixabay](https://pixabay.com)

### <ins>**_Wireframes_**</ins>
You can view the wireframe designs [here](./wireframe.pdf)

The wireframes for this project served as an initial design idea. As more features developed designs have been altered, or 
changed completely.


### <ins>**_User Stories_**</ins>


Being an eCommerce website based on providing web solutions to users, the following user stories specific to this project are: 

| **As the creator I want to:** |
| ------------------------------------------------------- |
|1. *Allow users buy products.* |
|2. *Allow users to sign up.* |
|3. *Have a database of users who contact us.* |
|4. *Easily view, edit and delete orders.* |
|5. *Easily view, edit and delete products.* |
|6. *Easily view members.* |
|6. *Have a list of users for future upselling. (Leads)* |
|7. *Limit the quantity of sales on specific products. (To avoid possibility of unworkable quantity websites / products being ordered at the same time)* |

| **As a user I want to:** |
| ------------------------------------------------------- |
|1. *Search for products.* |
|2. *Browse all products.* |
|3. *Filter products.* |
|4. *Create an account.* |
|5. *Track my data.* |
|6. *Contact admins.* |
|7. *See more about who I'm buying from.* |
|8. *See policies for refunds etc.* |
|9. *See products that are on sale.*


### <ins>**_Information Architectures_**</ins>
For this project, I wanted to use a design that meets UX design goals as well as functioning in a similar way to what users would expect. 

I wanted members, and non members to have a similar experience, which is why the profile section is somewhat hidden away. I wanted all users to be provided with an easy to use, straight forward shopping experience. 

#### *Non Members:*
> Non members will have full access to all pages within ManageMyWeb other than a personal profile dashboard. This allows non members to have a straight forward shopping experience without the need to sign up, therefore skipping the entire validation process that is involved with that step.

#### *Members:*
> A user who is a member of Manage My Web will have access to their personal dashboard. This dashboard will allow users to Create, Read, Update and Delete profile information.
>
> Members will also be able to track previous orders. This profile section will also provide the platform where admins will upload messages and updated information for members to see regarding their websites.

### <ins>**_Responsive Design:_**</ins>
This project is fully responsive and has been tested on screen widths between 375px up to 3800px. For this, Bootstrap CSS was used throughout. - [GetBootstrap.com](https://getbootstrap.com/)

### <ins>**_Typography_**</ins>
This project uses 'Oswald' & 'Zen Dots'. These main fonts are provided by [Google Fonts](https://fonts.google.com/).


### <ins>**_Colors_**</ins>
There are 2 primary colors used in this project, as well as 3 secondary colours:
> Primary:
> 1. #0275d8 (Bootstrap Primary)
> 2. #5cb85c (Bootstrap Success)

> Secondary:
> 1. #000 - Black
> 2. #f5f5f5 - Off White
> 3. #292b2c - Bootstrap Dark


### <ins>**_Icons:_**</ins>
Icons are used throughout this website, and are used in an attempt to increase UX design where possible. Icons in use have been taken 
from [Font Awsome](http://fontawesome.com/)

--------------------
## **Features**

To create this website, specific apps were made to target certain user stories and enhance user experience. These apps provide the foundations for this website, and will continue to provide a platform to grow into the future, with increased automation. As the products for sale on this project are webdesign and SEO related, I had to create a way to limit the quantity of sales, this is explained below:

### <ins>**_Limiting Sales:_**</ins>
To avoid a scenario where a user, or a combination of users could order too many products to work with. I have included a product quantity, much like a product stock take. This enables me to disable the further purchase of this product, whilst keeping the product visible (with a sold out flag). Once a backlog has been cleared, the available products can be updated to continue accepting sales.

### <ins>**_Existing Features:_**</ins>

* Stripe Integration.
* User Authentication.
* Email Marketing List.
* Email Notifications.
* Webhooks.
* Automated Chat.
* Product Search.
* iFrame Product Previews (Websites - "Personal Portfolio Website" for example has this feature.)
* Product Sorting.
* Product Backlog Prevention.
* Admin Panel.
* Lead Generation.
* Interactive Feedback
* Error Handling 
* Interactive Forms
* Product Limits - Built in "Availability" with front end feedback (banner on product image)
* Payment Error Capturing - Checkout first creates an order instance in the database, before trying to checkout, this way a user will not get charged multiple times if checkout page is refreshed etc.
* User Dashboard.
* Automated Emails.


### <ins>**_Future Features:_**</ins>

Items that have been included in the scope of this project, but have not yet been implemented are:
    
    Meeting Room:

    Providing a browser based meeting room to meet with clients and discuss progress in their order, or discuss strategies with members.
<br>

    Automated Web Page Development:

    This feature is almost functional, and uses a rest api that I have created in an external flask application, to take in user data, such as website name and other features, before generating a website pack. This pack includes a static html document, as well as the relevant CSS and Javascript. 

    
------------------
## **Technologies Used**

This project uses multiple languages, libraries and frameworks which can be found below:


### Languages
> 1. HTML / HTML5

HTML makes up the foundation of this project, including all content.

> 2. CSS / CSS3

CSS3 is used for all styling throught this application.

> 3. JavaScript / jQuery

JavaScript is used to manipulate data prior to passing it to Python based frameworks. Javascript is also used to help add interactive features, such as showing and hiding information. This allows more content to be provided, in a UX friendly way and avoid information overload.


> 4. Python / Django

Django provides the framework of this entire project. Handling all urls, and specific functionality features is provided by Python. This allows Manage My Web the ability to manipulate, data and direct information in various directions. 

For example, all contact forms, as well as sending emails, will capture user credentials such as name and email, and populate a database of "leads" which may be used to market products and other services in the future.

### Frameworks, Libraries & Other
1. Gitpod
> GitPod was used to develop the project.
2. Git
> Git was used for version control to commit to Git and push to GitHub.
3. GitHub
> GitHub is used to host the project files.
4. cPanel
> cPanel is used to store all deployed files.
5. Google Fonts
> Google fonts is used to provide custom fonts to this project.
6. FontAwesome
> FontAwesome is used for all icons.
7. BOTUI
> The BOTUI javascript framework is used for automated chat functionality.

---------------------
## **Testing**

This project has passed through several phases of testing, these phases include:

1. [W3 Validator](https://validator.w3.org/) to check all HTML. 
    1. To avoid issus and Flask, individual pages source code was added to validator in order to get valid feedback.

2. [W3 'Jigsaw' Validator](https://jigsaw.w3.org/css-validator/) to check all CSS.

3. [JS Hint](https://jshint.com/) to check all JavaScript. 

4. [PEP 8](http://pep8online.com/) to check all Python code.

5. [Autoprefixer](https://autoprefixer.github.io/) to ensure web browser compatability in CSS code.

> Testing was important in this project, with multiple forms located on pages. A recurring bug seemed to be the submission of multiple forms at once. To fix this problem 
jQuery was used to change a submit buttons value, this paired with an if statement in Python gave the desired outcome.

**Console.Log:** 

As forms use a change in value as part of a submission plan. Console log was used to ensure the correct outcome when clicking on submit buttons.

**Dev Tools:** 

As a means to testing visual problems, dev tools was used to identify and fix styling issues.
Dev tools was also used to improve features such as accessability, SEO, and performance where possible.

**Google Chrome 'Lighthouse':**

Lighthouse (Google Chrome Dev Tools) was used to find and fix performance, accessability, best practices and SEO issues. 


**Responsive Design:**

To ensure responsive design I have used [Responsive Design](http://ami.responsivedesign.is/). This was used to compliment testing performed in Google dev tools.

### **Bugs & Issues**:

> ### *Categories & Sub-Categories:*
> 
> This problem relates to the hierarchical structure of products:
>
> I originally wanted to create for example the parent category, with sub categories which I found can be tricky with SQLite.
>
> #### **Solution:**
>* Manipulate categories using one to many / one to one etc. This allows for essentially the same hierarchical structure, without the added complexity of most solutions available on [Stack Overflow](https://stackoverflow.com/).

<br>

> ### *Accessing Line Items In Orders, To Edit Admin Page:*
>
> This problem relates mainly to the subscriptions / expiry part of my orders model. 
>
> I wanted to parse through order line items, and if one line item was a subscription based product, the order would be updated to a subscription service, this would then trigger the editing of the user profile, to update the expiry date of their subscription etc.
>
> #### **Solution:**
>* Not sure why the initial bug appeared in the first place, however, a fix was to access the order line item, get the product id. 
>* Now access the product, check for membership or single product.
>* If product is just a single product, skip to next order line item.
>* If product is a membership, update the order record.
>* Using relative time delta, add one year to the order date, and use this for the expiry in the order model.


--------------------
## **Deployment**

### Requirements To Deploy:
- Amazon AWS Account

### Cloning This Project:
To create a clone, follow the following steps.

1. Log in to GitHub and go to the repository.
2. Click on the button with the text “Code”.
3. Click “Open with GitHub Desktop” and follow the prompts in the GitHub Desktop Application or follow the instructions from [GitHub](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository#cloning-a-repository-to-github-desktop) to see how to clone the repository in other ways.

#### To Work With Your Local Clone:
1. A
2. b
3. c

3. Create environment variables (env.py):
    1. Create a .gitignore file in the root directory of the project.
    2. Create a file in the root directory called "env.py". This will contain all of your envornment variables. Your env.py file should look similar to the following:
> Import os
>
> os.environ.setdefault("IP", "<IP TO USE>")
>
> os.environ.setdefault("PORT", "<PORT TO USE>")
>
> os.environ.setdefault("SECRET_KEY", "<ADD YOUR SECRET KEY>")
>
> os.environ.setdefault("MONGO_URI", "<ADD YOUR MONGO URI>")
>
> os.environ.setdefault("MONGO_DBNAME", "<ADD YOUR DATABASE NAME>")

    3. Add "env.py" to your .gitignore file.
    4. Finally to run the app, open a terminal and type "python3 app.py" and run the application.

### Deploying To AWS (Amazon Web Services)

To deploy our application on Heroku, we are required to have a requirements.txt file as well as a Procfile. These files will allow Heroku understand 
what dependencies are required to run the application, as well as tell Heroku which file to run, to launch the application.

#### Create a procfile:
> Type "python app.py > Procfile"
**This new file if opened should look something like "web: python app.py"**
#### Create a requirements file:
> Type "pip freeze --local > requirements.txt"
**This new file should simply be a list of all dependencies required**

#### For Deployment:
1. Open [Heroku](http://heroku.com/).
2. Login or signup for Heroku.
3. Once logged in create a new app and select the desired region. 
4. Deployment method "GitHub" (if this section is accidentally missed, you can use the tab selection within your dashboard "DEPLOY")
5. Select "connect to GitHub" and follow the on screen instructions. Once connected to your Github:
    1. Search for your repository using the form provided.
6. Once you have connected your GitHub repository:
    1. Navigate to the "Settings" tab:
        1. Scroll to the section "Config Vars" here you will have to tell Heroku what these variables are:
            1. Input data from env.py in the key value section: (e.g. SECRET_KEY in the first box, <YOUR SECRET_KEY> in the second box)
            2. Input all data for IP, PORT, SECRET_KEY, MONGO_DBNAME & MONGO_URI
    2. Navigate back to the "Deploy" tab:
        1. Scroll to the "Manual Deploy" tab:
            1. Select the branch you wish to deploy (master is default)
            2. Click the "Deploy Branch" button. (This may take some time as Heroku uploads the app to their servers.) 

> *Once the build is complete, a "View App" button will appear just below the build progress box. You can click this to see immediately if the build was successful. If the app doesn't load first time, try refresh once prior to investigating further.*
> 
> *Common issues include outdated requirements.txt and/or missing Procfile, if errors occur, check these are both correct before investigating further.*

----------------------
## **Credits**
This project, although pieced together by myself, incorporates images, video, sound, and code from multiple sources. These include:
    

### <ins>**_Media:_**</ins>



### <ins>**_Content:_**</ins>
> All text content is my own, with the exception of:
1. Quotes in footer - All of which are cited, please check live website or source code for individual quotes & authors.
2. Mock websites - Websites contained within iFrames use template websites that are available for download via [FreeCSS](https://www.free-css.com/free-css-templates). These templates remain the property of their respective authors. 

### <ins>**Code:**</ins>
All code created in this project is my own, and has been created using prior knowledge, as well as picking ideas from [StackOverflow](stackoverflow.com)

Payment processing code is closely paired to the [Code Institute](https://codeinstitute.net/) Django tutorial, but changed to match the needs of this project.

*Any code that is a direct copy from W3Schools, or Stackoverflow will include the correct comments. This will be the case in all CSS, Javascript and Python files throughout this project*

### <ins>**_Acknowledgments:_**</ins>
I would like to acknowledge my mentor <ins>Caleb Mbakwe</ins> for his guidance and tips during this project.

## *Previews:*
Here are a few previews of Ripe Recipes (mockups from [Am I Responsive](http://ami.responsivedesign.is/))

