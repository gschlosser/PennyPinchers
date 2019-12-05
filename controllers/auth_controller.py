from flask import Blueprint
from flask import Flask


'''register auth blueprint with prefix '/auth' so that auth_controller works'''
@auth_controller.route('/login', methods=['POST'])
def login():


@auth_controller.route('/register', methods=['POST'])
def register():


@auth_controller.route('/user_details', methods=['POST'])
def user_details():
    