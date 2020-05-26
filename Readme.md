# CVMaker

Database for building CV

This application allows you to create an account in which you can add data to several CVs and then generate a pdf with the selected template.

Technologies stack:

- Database: MongoDB Atlas
- Technology Python, django

## Setup

```bash
pip install -r requirements.txt
```
Download [wkhtmltopdf](https://wkhtmltopdf.org/downloads.html) or follow instruction from [here](https://github.com/worlduniting/bookshop/wiki/Installing-wkhtmltopdf)

Make sure on windows wkhtmltopdf is in PATH, you can check that by typing in terminal 
```bash
wkhtmltopdf --version
```
## Description

To connect your MongoDB Atlas cluster you need to create file in CVMaker folder, where there is a settings.py file
 
 #### **`CVMaker/config.py`**
 ```python
DB_CONNECTION = 'your connection string'
DB_NAME = 'name od database user'
DB_PASSWORD = 'password string'
```

To get create database connection data follow a tutorial [here](https://docs.atlas.mongodb.com/connect-to-cluster/)

## Structure

Database models can be found at
[models.py](./home/models.py)

Forms for creating and saving to database objects 
[forms.py](./accounts/forms.py)

[Settings](./CVMaker/settings.py)

File where are declared urls which can be accessed on website
[urls.py](./CVMaker/urls.py)

Views, where single pages are rendered and pdf generation logic is used
[accounts views.py](./accounts/views.py),
[home views.py](./home/views.py)

Auxiliary functions
[utils.py](./home/utils.py)

Html files 
[templates](./templates)

## Database

Each user in the database has a collection of data named *UserData*.

UserData contains fields like:
* name
* surname
* several CVs called *current_cvs*

Every CV contains:
* contact_info (basic information about you like city, country, phone, email, etc.)
* education (schools, universities which you have attended)
* experience (work experience)
* skills
* languages
* interests
* projects (projects which you have participated in)
* organizations (organizations you are or have been a member of)
* description (short description about who you are, for example "Computer Science Student")
* name (name of CV for your own knowledge)
* quotation (quotation that describe you)

There is also a collection called *Universities* in the database.
Every university has a name and address which include city, street, street number and zip code.
When you add education to your CV, you can use the universities in this collection or add your own if it is not in this collection.

## Roadmap

- [x] podlączenie bazy atlas
- [x] logowanie/rejestracja
- [x] lista dodanych danych do cv
- [x] dodawanie danych do cv
- [x] wygeneruj i pobierz

## Contributors ✨

<table>
  <tr>
    <td align="center"><a href="https://github.com/Wokstym"><img src="https://avatars2.githubusercontent.com/u/44115112?s=460&u=2fea6d808fb949060aa499dad3e3365608bb5c40&v=4" width="100px;" alt=""/><br /><sub><b>Grzegorz Poręba</b></sub></a><br />
    </td>
    <td align="center"><a href="https://github.com/alexmaz99"><img src="https://avatars2.githubusercontent.com/u/56346754?s=460&u=a0c3bd4ae7860a0694db0110f7b10d80434fecd4&v=4" width="100px;" alt=""/><br /><sub><b>Aleksandra Mazur</b></sub></a><br /></td>
  </tr>
</table>
