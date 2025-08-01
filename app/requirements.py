# Package requirements
requirements = {
    'Babel': '2.12.1',
    'bcrypt': '4.0.1',
    'bleach': '6.1.0',
    'blinker': '1.6.2',
    'cffi': '1.16.0',
    'click': '8.1.7',
    'colorama': '0.4.6',
    'cryptography': '42.0.2',
    'datatables': '0.4.9',
    'dnspython': '2.4.2',
    'email-validator': '2.0.0.post2',
    'Flask': '2.3.3',
    'Flask-BabelEx': '0.9.4',
    'Flask-Login': '0.6.2',
    'Flask-Mail': '0.9.0',
    'flask-mailman': '1.0.0',
    'Flask-Principal': '0.4.0',
    'Flask-Security': '3.0.0',
    'Flask-Security-Too': '5.3.0',
    'Flask-SQLAlchemy': '3.0.2',
    'Flask-WTF': '1.1.1',
    'greenlet': '2.0.2',
    'idna': '3.4',
    'importlib-resources': '6.1.0',
    'iniconfig': '2.0.0',
    'itsdangerous': '2.1.2',
    'Jinja2': '3.1.2',
    'MarkupSafe': '2.1.3',
    'mkdocs-material-extensions': '1.2',
    'packaging': '23.2',
    'passlib': '1.7.4',
    'pip': '24.0',
    'pluggy': '1.4.0',
    'pycparser': '2.21',
    'PyMySQL': '1.1.0',
    'pytest': '8.0.0',
    'python-dateutil': '2.8.2',
    'pytz': '2023.3.post1',
    'setuptools': '65.5.0',
    'six': '1.16.0',
    'speaklater': '1.3',
    'SQLAlchemy': '2.0.21',
    'sqlalchemy-datatables': '2.0.1',
    'typing_extensions': '4.8.0',
    'webencodings': '0.5.1',
    'Werkzeug': '2.3.7',
    'WTForms': '3.0.1'
}

# Generate requirements.txt
with open('requirements.txt', 'w') as f:
    for package, version in requirements.items():
        f.write(f"{package}=={version}\n")
