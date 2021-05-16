## Building a Startup Categorizer with Blog
https://github.com/gurnitha/django-startup-categorizer-with-blog

## I. Django Core Features

### -------1/12--------


### 1 Starting a New Django Project: Building a Startup Categorizer with Blog 3

#### 1.1 Introduction
		PASS
#### 1.2 Website Basics
		PASS
#### 1.3 Understanding Modern Websites
		PASS
#### 1.4 Building Modern Websites: The Problems That Frameworks Solve and Their Caveats
		PASS
#### 1.5 Django: Python Web Framework
		PASS
#### 1.6 Defining the Project in Part I

		In Part I, we focus on the most basic features. We create the blog, startup, and tagging
		system in Django. The goal is to make Django’s core, features necessary to every website, as
		evident as possible.

		List the webpages we will build in Part I:

		1. A page to list tags
		2. A page for each tag
		3. A page to add a new tag

		4. A page to list startups
		5. A page for each startup
		6. A page to add a new startup

		7. A page to list blog posts
		8. A page for each blog post (which also lists news articles)
		9. A page to add a new blog post

		10. A page to add and connect news articles to blog posts	
	
#### 1.7 Creating a New Django Project and Django Apps

		(venv3922) ing| tree -L 2
		.
		├── blog
		│   ├── __init__.py
		│   ├── __pycache__
		│   ├── admin.py
		│   ├── apps.py
		│   ├── migrations
		│   ├── models.py
		│   ├── tests.py
		│   └── views.py
		├── db.sqlite3
		├── manage.py
		├── organizer
		│   ├── __init__.py
		│   ├── __pycache__
		│   ├── admin.py
		│   ├── apps.py
		│   ├── migrations
		│   ├── models.py
		│   ├── tests.py
		│   └── views.py
		└── suorganizer
		    ├── __init__.py
		    ├── __pycache__
		    ├── asgi.py
		    ├── settings.py
		    ├── urls.py
		    └── wsgi.py

#### 1.8 Put it all togather - added .gitignore and readme.md files		    

#### 1.9 Re-modified readme.md file


### -------2/12--------

### 2. Hello World: Building a Basic Webpage in Django

#### 2.1 Creating and Integrating a New App (helloworld)
#### 2.2 Removing the 'helloworld' app


### -------3/12--------


### 3. Programming Django Models and Creating a SQLite Database

#### 3.1 Specifying and Organizing Data in Django Using Models

		.Tag
			.tag name
			.slug
		.Startup
			.name of company
			.slug
			.description or purpose
			.date founded
			.contact email
			.website
		.News Link
			.title or headline
			.link to article
			.publication date
			.foreign key to Startup
		.Blog Post
			.post title
			.slug
			.post text or description
			.publication date
		.Many-to-Many Relationships
			.startup and tag
			.blog post and tag
			.blog posts and startup

#### 3.2 Creating models: blog/Post, organizer/Tag, organizer/Startup, organizer/NewsLink

#### 3.3 Adding Relational Fields to Our Models

		.A one-to-many relationship pointing news links to startups
		.A many-to-many relationship between startups and tags
		.A many-to-many relationship between blog posts and tags
		.A many-to-many relationship between blog posts and startups


		