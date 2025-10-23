### Hexlet tests and linter status:
[![Actions Status](https://github.com/GLEXD/python-project-83/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/GLEXD/python-project-83/actions)
[![PythonCI](https://github.com/GLEXD/python-project-83/actions/workflows/CI.yml/badge.svg)](https://github.com/GLEXD/python-project-83/actions/workflows/CI.yml)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=GLEXD_python-project-83&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=GLEXD_python-project-83)

# Project was made for Hexlet by Gleb Burimov
The program checking two files for changes between them

# Page analyser
### App for analyse web pages. The application checks the aviability of websites and getting their headers, descriptions and H1 tags.

## Features
* URL aviability check
* Analysis of title and description tag
* Display check results on the user interface

### You can view application on the website: [Page Analyzer](https://pageanalyzer-40ad.onrender.com)

## Libraries:
* flask
* bs4
* flake8
* gunicorn
* psycopg2
* pytest
* python-dotenv
* requests
* validators

## Installation and Setup
1. Clone the repository:
```bash
git clone https://github.com/GLEXD/python-project-83.git
cd python-project-83
```
2. Create `.env` file:
```bash
DATABASE_URL=postgresql://username:password@localhost:5432/dbname
SECRET_KEY=your_secret_key_here
```
3. Install dependencies:
```bash
make build
```
4. Start application in production mode:
```bash
make start
```
5. For development with hot reload:
```bash
make dev
```

## Linting
```bash
make lint
```

## How to Use 
1. Enter website URL
2. Get SEO analysis
3. View detailed report
4. Check analysis history