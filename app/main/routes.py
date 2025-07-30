from app.main import bp
from functools import wraps
from flask_security import login_required,lookup_identity,roles_required
from app.models.auth import User,Role,RolesUsers,FolderPermission  
from app.extensions import db
from flask import request,g
from flask_security.utils import hash_password
from flask import flash
from flask import render_template, request, url_for, redirect
from sqlalchemy import join
from flask import jsonify
from flask_security import roles_accepted
from flask import session
# from flask_mail import Message
# from flask_login import current_user


ACCESS = {'admin': 'admin'}


def requires_access_level(access_level):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if 'email' not in session:
                return redirect(url_for('security.login'))  # Update endpoint to 'security.login'

            user = User.find_by_email(session['email'])
            if not user or not user.allowed(access_level):
                return redirect(url_for('users.profile', message="You do not have access to that page. Sorry!"))
            return f(*args, **kwargs)
        return decorated_function
    return decorator


@bp.route('/')
@login_required
def index():
    return render_template('index.html')


# @bp.route('/users/list', methods=["GET", "POST"])
# @requires_access_level(ACCESS['admin'])
# @login_required 
# def users():
#     try:
#         me_users = db.session.query(User).all()
#         return render_template('main/users.html', users=me_users)
#     except Exception as e:
#         return str(e)
    

@bp.route('/users/list', methods=["GET", "POST"])
# @requires_access_level(ACCESS['admin'])
@login_required
def users():
    try:
        users = User.query.all()
        return render_template('main/users.html', users=users)
    except Exception as e:
        return str(e)



@bp.route('/roles/list', methods=["GET"])
@login_required
def roles():
    try:
        b=Role
        roles = db.session.query(b.id,b.name,b.description).all()
         
        return render_template('main/roles.html', roles=roles)
    except Exception as e:
        return str(e)
    

    

@bp.route('/role_permissions/list', methods=["GET", "POST"])
@login_required
# @roles_accepted('admin')
def role_permissions():
    try:
        # Perform a join query to get role permissions with user details
        role_permissions = db.session.query(RolesUsers, User, Role). \
            join(User, RolesUsers.user_id == User.id). \
            join(Role, RolesUsers.role_id == Role.id).all()
        
        return render_template('main/role_permissions.html', role_permissions=role_permissions)
    except Exception as e:
        return str(e)

    

@bp.route('/create', methods=['GET', 'POST'])
def create():
    if request.method == 'POST':
        data = request.form

        # Fetch roles from the database
        roles = Role.query.all()

        new_user = User(
            username=data['username'],
            email=data['email'],
            password=hash_password(data['password'])
        )

        # Check if a role is selected in the form data
        if 'role' in data:
            # Find the selected role from the roles fetched from the database
            selected_role = next((role for role in roles if role.id == int(data['role'])), None)
            if selected_role:
                #new_user.role.append(RolesUsers(role=selected_role))
                new_user.roles.append(RolesUsers(role=selected_role))

        # Check if there is already a user with this email
        user = lookup_identity(data["email"])
        if not user:
            db.session.add(new_user)
            db.session.commit()

        flash("Success: User created successfully.", "success")
        return redirect(url_for("main.users"))

    # If it's a GET request, render the create user form with roles
    # Fetch roles from the database
    roles = Role.query.all()
    return render_template('main/create.html', roles=roles)





# @bp.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
# def update_user(user_id):
#     user = User.query.get_or_404(user_id)
#
#     roles = Role.query.all()
#
#     if request.method == 'POST':
#         data = request.form
#         user.username = data.get('username', user.username)  # Use get method to avoid key error
#         user.email = data.get('email', user.email)  # Use get method to avoid key error
#
#         # Update the password only if it's provided
#         if 'password' in data and data['password']:
#             user.password = hash_password(data['password'])
#
#         # Clear existing roles before updating
#         user.role.clear()
#
#         if 'role' in data:
#             selected_role_id = int(data.get('role'))
#
#             selected_role = next((role for role in roles if role.id == selected_role_id), None)
#             if selected_role:
#                 user.role.append(selected_role)
#
#         db.session.commit()
#         flash("Success: User data updated successfully.")
#         return redirect(url_for("main.users"))
#
#     return render_template('main/update.html', user=user, roles=roles)


# @bp.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
# def update_user(user_id):
#     user = User.query.get_or_404(user_id)
#
#     roles = Role.query.all()
#
#     if request.method == 'POST':
#         data = request.form
#         user.username = data.get('username', user.username)  # Use get method to avoid key error
#         user.email = data.get('email', user.email)  # Use get method to avoid key error
#
#         # Update the password only if it's provided
#         if 'password' in data and data['password']:
#             user.password = hash_password(data['password'])
#
#         # Clear existing roles before updating
#         user.roles.clear()  # Use user.roles.clear() instead of user.role.clear()
#
#         if 'role' in data:
#             selected_role_id = int(data.get('role'))
#
#             selected_role = next((role for role in roles if role.id == selected_role_id), None)
#             if selected_role:
#                 user.roles.append(selected_role)  # Use user.roles.append() instead of user.role.append()
#
#         db.session.commit()
#         flash("Success: User data updated successfully.")
#         return redirect(url_for("main.users"))
#
#     return render_template('main/update.html', user=user, roles=roles)

@bp.route('/update_user/<int:user_id>', methods=['GET', 'POST'])
def update_user(user_id):
    user = User.query.get_or_404(user_id)
    roles = Role.query.all()

    if request.method == 'POST':
        data = request.form
        user.username = data.get('username', user.username)
        user.email = data.get('email', user.email)

        # Update the password only if it's provided
        if 'password' in data and data['password']:
            user.password = hash_password(data['password'])

        # Retrieve the selected role IDs from the form data
        selected_role_ids = request.form.getlist('roles')

        # Clear existing roles
        user.roles.clear()

        # Append selected roles
        selected_roles = Role.query.filter(Role.id.in_(selected_role_ids)).all()
        user.roles.extend(selected_roles)

        db.session.commit()
        flash("Success: User data updated successfully.")
        return redirect(url_for("main.users"))

    return render_template('main/update.html', user=user, roles=roles)




@bp.route('/create_role', methods=['GET', 'POST'])
def create_role():
    if request.method == 'POST':
        data = request.form
        new_role = Role(name=data['name'], description=data['description'])
        db.session.add(new_role)
        db.session.commit()
        flash("Success: Role created successfully.", "Success")
        return redirect(url_for("main.roles"))
    
    return render_template('main/create_role.html',Role=Role)


### Update Role
@bp.route('/update_role/<int:role_id>', methods=['GET','POST'])
def update_role(role_id):
    role = Role.query.get_or_404(role_id)
    if request.method == 'POST':
      
        data = request.form
        role.name = data['name']
        role.description = data['description']
        db.session.commit()
        flash("Success: role updated successfully.")
        return redirect(url_for("main.roles"))

    return render_template('main/update_role.html', role=role)


### Delete User
@bp.route('/delete_user/<int:user_id>', methods=['GET', 'POST'])
def delete_user(user_id):
    user = User.query.get_or_404(user_id)
    if request.method == 'POST':
        db.session.delete(user)
        db.session.commit()
        flash("Success: User deleted successfully.")
        return redirect(url_for("main.users"))

    return render_template('main/delete.html', user=user)


@bp.route('/delete_role/<int:role_id>', methods=['GET', 'POST'])
def delete_role(role_id):
    role = Role.query.get_or_404(role_id)
    
    if request.method == 'POST':
        db.session.delete(role)
        db.session.commit()
        flash("Success: role deleted successfully.")
        # Redirect to a different page after successful deletion 
        return redirect(url_for('main.roles'))

    return render_template('main/delete_role.html', role=role)



@bp.route('/permissions', methods=['GET', 'POST'])
@login_required
def permissions():
    try:
        roles = Role.query.all() 
        role_id = None
        role = Role.query.first()
        if role:
            role_id = role.id
        return render_template('main/permissions.html', roles=roles, role_id=role_id)  # Pass roles and role_id to the template
    except Exception as e:
        return str(e)
    
    


@bp.route('/assign_folder_permissions/<int:role_id>', methods=['POST'])
def assign_folder_permissions(role_id):
    try:
        role = Role.query.get(role_id)
        if role:
            folder_path = request.form.get('folder_path')
            if folder_path:
                # Here you can add further validation if needed
                permission = FolderPermission(role_id=role_id, folder_path=folder_path)
                db.session.add(permission)
                db.session.commit()
                flash("Folder permission assigned successfully.", "success")
            else:
                flash("Error: Folder path is required.", "error")
        else:
            flash("Error: Role not found.", "error")
    except Exception as e:
        flash(f"Error: {str(e)}", "error")

    return redirect(url_for('main.admin_panel'))


@bp.route('/admin_panel')
#@roles_accepted('Admin', 'Teacher')
def admin_panel():
    try:
        roles = Role.query.all()
        folder_permissions = FolderPermission.query.all()
        return render_template('main/admin_panel.html', roles=roles, folder_permissions=folder_permissions)
    except Exception as e:
        flash(f"Error: {str(e)}", "error")
        return redirect(url_for('main.index'))



