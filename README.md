## Desc

Django Postgresql multi-tenant app starter

### Includes

Django admin site for superuser to be able to manage the public schema tables

To be able to manage the migrations used [django-tenant-schemas package](https://django-tenant-schemas.readthedocs.io/en/latest/)


### migration commands

#### migrate_schemas --shared

The command ```$ python manage.py migrate_schemas --shared``` will create the shared apps on the public schema.
> Note: database should be empty if this is the first time it is run this command

#### migrate_schemas

migrate_schemas command is very handy. first it will create migrations for shared apps after that will create for tenant_apps

#### Warning
> never directly should be called migrate. this command will create all the migrations in public

## Installation
```git
git clone
```
```python venv
python3 -m virtualenv venv
source venv/bin/activate
```
```requirements
pip install -r ./requirements.txt
```
```env
cp main/.env.example main/.env # fill db credentials
```
```migrations
python manage.py makemigrations
python manage.py migrate_schemas
```

```runserver
python manage.py runserver
```

## Useful Resources

[django-tenant-schemas](https://django-tenant-schemas.readthedocs.io/en/latest/)

