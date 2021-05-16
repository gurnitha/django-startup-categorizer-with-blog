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

#### 3.3 (Re-saving) Adding Relational Fields to Our Models

#### 3.4 Controlling Model Field Behavior with Field Options

#### 3.5 Adding Methods to Django Models

#### 3.6 Controlling Model Behavior with Nested Meta Classes

#### 3.7 Create database: run migration and createsuperuser

		(venv3922) ing| python3 manage.py sqlmigrate blog 0001
		BEGIN;
		--
		-- Create model Post
		--

		CREATE TABLE "blog_post" (
			"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
			"title" varchar(63) NOT NULL, 
			"slug" varchar(63) NOT NULL, 
			"text" text NOT NULL, 
			"pub_date" date NOT NULL
		);

		CREATE TABLE "blog_post_startups" (
			"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
			"post_id" bigint NOT NULL REFERENCES "blog_post" ("id") DEFERRABLE INITIALLY DEFERRED, 
			"startup_id" bigint NOT NULL REFERENCES "organizer_startup" ("id") DEFERRABLE INITIALLY DEFERRED
		);

		CREATE TABLE "blog_post_tags" (
			"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
			"post_id" bigint NOT NULL REFERENCES "blog_post" ("id") DEFERRABLE INITIALLY DEFERRED, 
			"tag_id" bigint NOT NULL REFERENCES "organizer_tag" ("id") DEFERRABLE INITIALLY DEFERRED
		);

		CREATE INDEX "blog_post_slug_b95473f2" ON "blog_post" ("slug");
		CREATE UNIQUE INDEX "blog_post_startups_post_id_startup_id_459561f9_uniq" ON "blog_post_startups" ("post_id", "startup_id");
		CREATE INDEX "blog_post_startups_post_id_b1153755" ON "blog_post_startups" ("post_id");
		CREATE INDEX "blog_post_startups_startup_id_a3e30c05" ON "blog_post_startups" ("startup_id");
		CREATE UNIQUE INDEX "blog_post_tags_post_id_tag_id_4925ec37_uniq" ON "blog_post_tags" ("post_id", "tag_id");
		CREATE INDEX "blog_post_tags_post_id_a1c71c8a" ON "blog_post_tags" ("post_id");
		CREATE INDEX "blog_post_tags_tag_id_0875c551" ON "blog_post_tags" ("tag_id");
		COMMIT;


		(venv3922) ing| python3 manage.py sqlmigrate organizer 0001

		BEGIN;
		--
		-- Create model Tag
		--
		CREATE TABLE "organizer_tag" (
			"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
			"name" varchar(31) NOT NULL UNIQUE, 
			"slug" varchar(50) NOT NULL UNIQUE
		);

		--
		-- Create model Startup
		--
		CREATE TABLE "organizer_startup" (
			"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
			"name" varchar(31) NOT NULL, 
			"slug" varchar(31) NOT NULL UNIQUE, 
			"description" text NOT NULL, 
			"founded_date" date NOT NULL, 
			"contact" varchar(225) NOT NULL, 
			"website" varchar(200) NOT NULL
		);

		CREATE TABLE "organizer_startup_tags" (
			"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
			"startup_id" bigint NOT NULL REFERENCES 
			"organizer_startup" ("id") DEFERRABLE INITIALLY DEFERRED, 
			"tag_id" bigint NOT NULL REFERENCES "organizer_tag" ("id") DEFERRABLE INITIALLY DEFERRED
		);
		--
		-- Create model NewsLink
		--
		CREATE TABLE "organizer_newslink" (
			"id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
			"title" varchar(63) NOT NULL, 
			"pub_date" date NOT NULL, 
			"link" varchar(225) NOT NULL, 
			"startup_id" bigint NOT NULL REFERENCES "organizer_startup" ("id") DEFERRABLE INITIALLY DEFERRED
		);
		CREATE INDEX "organizer_startup_name_0080733f" ON "organizer_startup" ("name");
		CREATE UNIQUE INDEX "organizer_startup_tags_startup_id_tag_id_982c6d9a_uniq" ON "organizer_startup_tags" ("startup_id", "tag_id");
		CREATE INDEX "organizer_startup_tags_startup_id_94e79a84" ON "organizer_startup_tags" ("startup_id");
		CREATE INDEX "organizer_startup_tags_tag_id_bcc66000" ON "organizer_startup_tags" ("tag_id");
		CREATE INDEX "organizer_newslink_startup_id_ad247707" ON "organizer_newslink" ("startup_id");
		COMMIT;

#### 3.8 Registering models: Post, Tag, Startup, NewsLink to admins


### -------4/12--------

#### 4.1 Rapidly Producing Flexible HTML with Django Templates













