🎬 Movie Review API

A powerful Django + Django REST Framework API that allows users to create, manage, and explore movie reviews. This project is designed to mimic a real-world backend environment, complete with authentication, CRUD operations, pagination, and search features.

🚀 Overview
The Movie Review API enables authenticated users to add, update, delete, and view reviews for movies. It includes robust database models, permission handling, search and filtering capabilities, and deployment support for platforms like Heroku or PythonAnywhere.
This backend project challenges your skills in API architecture, database modeling, authentication, and production deployment.

✅ Features
⭐ Review Management (CRUD)

Create, Read, Update, Delete movie reviews
Each review includes:
Movie Title
Review Content
Rating (1–5)
User (Author)
Created Date
Validations for required fields (rating range, movie title, content)

👤 User Management (CRUD)

Users have: Username, Email, Password
Authentication required for creating, updating, or deleting reviews
Users can modify only their own reviews
Permissions enforced via DRF

🎥 View Reviews by Movie
Endpoint to list reviews for a specific movie
Pagination for large result sets
Optional sorting by rating or creation date

🔍 Review Search & Filtering
Search reviews by:
Movie Title
Rating
Filter reviews by rating (e.g., only 4⭐ and 5⭐ reviews)

🛠️ Technical Requirements

🗂️ Database (Django ORM)
Models for:
User (Django auth or custom)
Review
Allow multiple reviews per movie from different users

🔐 Authentication

Django’s built-in authentication system
Login required for review modifications
Optional JWT support for enhanced security

🌐 API Design (DRF)
Follows REST principles
Uses appropriate HTTP methods:
GET, POST, PUT, PATCH, DELETE

Robust error handling:
400 — Bad Input
401 — Unauthorized
404 — Not Found
403 — Forbidden

🚢 Deployment
Deployable on:
Heroku
PythonAnywhere
Configure:
Allowed hosts
Environment variables

Static files

Database settings

📊 Pagination & Sorting

Pagination enabled for review lists

Sorting available by:

Rating

Created Date
