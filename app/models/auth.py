# from flask_security import UserMixin, RoleMixin
# from sqlalchemy import Boolean, DateTime, Column, Integer, String, ForeignKey
# from sqlalchemy.orm import relationship
# from app.extensions import db
# import uuid
#
# class User(db.Model, UserMixin):
#     __tablename__ = "user"
#     id = db.Column(Integer(), primary_key=True)
#     email = Column(String(255), unique=True)
#     username = Column(String(255), unique=True, nullable=True)
#     password = Column(String(255), nullable=False)
#     last_login_at = Column(DateTime())
#     current_login_at = Column(DateTime())
#     last_login_ip = Column(String(100))
#     current_login_ip = Column(String(100))
#     login_count = Column(Integer)
#     active = Column(Boolean(), default=True)
#     premium = Column(Boolean())
#     fs_uniquifier = Column(String(255), unique=True, nullable=False, default=uuid.uuid4().hex)
#     confirmed_at = Column(DateTime())
#
#     roles = db.relationship('Role', secondary='roles_users', backref=db.backref('assigned_users', lazy='dynamic'))
#
# class RolesUsers(db.Model):
#     __tablename__ = "roles_users"
#     id = Column(Integer, primary_key=True)
#     user_id = Column(Integer, ForeignKey("user.id"))
#     role_id = Column(Integer, ForeignKey("role.id"))
#
#     user = relationship("User", backref="user_roles")
#     role = relationship("Role", backref="role_users")
#
# # class Role(db.Model, RoleMixin):
# #     __tablename__ = "role"
# #     id = Column(Integer(), primary_key=True)
# #     name = Column(String(80), unique=True)
# #     description = Column(String(255))
# #     folder_permissions = relationship('FolderPermission', backref='role', lazy='dynamic')
# #     users = relationship("RolesUsers", back_populates="role")
#
# class Role(db.Model, RoleMixin):
#     __tablename__ = "role"
#     id = Column(Integer(), primary_key=True)
#     name = Column(String(80), unique=True)
#     description = Column(String(255))
#     folder_permissions = relationship('FolderPermission', backref='role', lazy='dynamic')
#     users = relationship("RolesUsers", back_populates="role")
#
#
# class FolderPermission(db.Model):
#     id = Column(Integer, primary_key=True)
#     role_id = Column(Integer, ForeignKey('role.id'))
#     folder_path = Column(String(255))


from flask_security import UserMixin, RoleMixin
from sqlalchemy import Boolean, DateTime, Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.extensions import db
import uuid

class User(db.Model, UserMixin):
    __tablename__ = "user"
    id = db.Column(Integer(), primary_key=True)
    email = Column(String(255), unique=True)
    username = Column(String(255), unique=True, nullable=True)
    password = Column(String(255), nullable=False)
    last_login_at = Column(DateTime())
    current_login_at = Column(DateTime())
    last_login_ip = Column(String(100))
    current_login_ip = Column(String(100))
    login_count = Column(Integer)
    active = Column(Boolean(), default=True)
    premium = Column(Boolean())
    fs_uniquifier = Column(String(255), unique=True, nullable=False, default=uuid.uuid4().hex)
    confirmed_at = Column(DateTime())

    roles = db.relationship('Role', secondary='roles_users', backref=db.backref('assigned_users', lazy='dynamic'))

class RolesUsers(db.Model):
    __tablename__ = "roles_users"
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("user.id"))
    role_id = Column(Integer, ForeignKey("role.id"))

    user = relationship("User", backref="roles_users")
    role = relationship("Role", backref="roles_users")

class Role(db.Model, RoleMixin):
    __tablename__ = "role"
    id = Column(Integer(), primary_key=True)
    name = Column(String(80), unique=True)
    description = Column(String(255))
    folder_permissions = relationship('FolderPermission', backref='role', lazy='dynamic')
    users = relationship("User", secondary='roles_users', back_populates="roles")

class FolderPermission(db.Model):
    id = Column(Integer, primary_key=True)
    role_id = Column(Integer, ForeignKey('role.id'))
    folder_path = Column(String(255))

