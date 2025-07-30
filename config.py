
class Config:
    SECRET_KEY = 'asdfghjklqwertyuiop'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:Rover#123@localhost:3306/register'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # flask security password salt
    SECURITY_PASSWORD_SALT = 'zxcvbnm1234567890lkjhgfdsapoiuytrewq'

    









'''{% if user[9] == "True" %}
    {{ "Active" }}
    {% else %}
    {{ "In-Active" }}
    {% endif %}'''

'''
        default_role = Role.query.filter_by(name='user').first()
        if default_role:
            new_user.roles.append(RolesUsers(role=default_role))
'''
'''print(new_user)
        user = User.query.filter_by(id=1).first()
        role = Role.query.filter_by(name='user').first()

        # Create an entry in the roles_users table
        new_roles_users_entry = RolesUsers(user_id=user.id, role_id=role.id)

        # Add the entry to the database
        db.session.add(new_roles_users_entry)
        db.session.commit()'''




'''
{% extends 'base.html' %}

{% block content %}
    <div class="card">
        <div class="card-header">
            <h5>{% block title %} Users {% endblock %}</h5>
        </div>
        <div class="card-body">
            {% if current_user.is_authenticated %}
                <div class="table-responsive table-responsive-sm">
                    <a href="{{ url_for('main.create') }}"><button title="Create User" type="button" class="btn btn-primary"><i class="bi bi-person-plus-fill"></i></button></a>                    
                    <table id="user_table" class="table table-striped table-bordered">
                        <thead>
                            <tr>
                                <th>ID</th>
                                <th>Email</th>
                                <th>Username</th>
                                <th>Active</th>
                                <th>Roles</th>
                                <th>Action</th>
                            </tr>
                        </thead>
                        <tbody>
                            {% for user in users %}
                            <tr>
                                <td>{{ user[0] }}</td>
                                <td>{{ user[1] }}</td>
                                <td>{{ user[2] }}</td>
                                <td>{{ user[9] }}</td>
                                <td>{{ user[13] }}</td>  
                                                                                 
                                <td>
                                    <a title="Update" class="btn btn-primary btn-sm" href="{{ url_for('main.update_user', user_id=user[0]) }}">
                                        <i class="bi bi-pencil-square"></i>
                                    </a>
                                    
                                    <a title="Delete" class="btn btn-danger btn-sm" href="{{ url_for('main.delete_user', user_id=user[0]) }}" style="display: inline;">
                                        <i type="submit" class="bi bi-trash3"></i>
                                        
                                    </a>
                                </td>
                            </tr>
                            {% endfor %}
                        </tbody>
                    </table>
                </div>
            {% endif %}
        </div>
    </div>
{% endblock %}'''