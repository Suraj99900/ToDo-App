from flask import Blueprint, jsonify, render_template, request
import models.UserModel as user

rUserBp = Blueprint('user_bp', __name__, url_prefix='/')
oUser =  user.UserModel()
@rUserBp.route('/')
def index():
    return render_template('index.html')

@rUserBp.route('/addUser', methods=['POST'])
def add_user():
    data = request.get_json()
    user_name = data.get('name')
    user_email = data.get('email')
    userTask = data.get('userTask')
    

    new_user = oUser.insertUser(user_name,user_email,userTask)
    

    return jsonify({'success': True, 'message': 'User added successfully!', 'body': new_user}), 201

@rUserBp.route('/getAllUsers', methods=['GET'])
def get_all_users():
    all_users = oUser.fetchAllUsers()
    
    

    return jsonify({'success': True, 'message': 'Fetched all users successfully!', 'body': all_users}), 200

@rUserBp.route('/deleteUser/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):

    deleted = oUser.deleteUser(user_id)  
    
    if deleted:
        return jsonify({'success': True, 'message': 'User deleted successfully!'}), 200
    else:
        return jsonify({'success': False, 'message': 'User not found!'}), 404
    
@rUserBp.route('/getUserById/<int:user_id>', methods=['GET'])
def fetch_user_by_id(user_id):

    user_result = oUser.fetchUserById(user_id) 

    if user_result:
        return jsonify({'success': True, 'user': user_result}), 200
    else:
        return jsonify({'success': False, 'message': 'User not found'}), 404
    
@rUserBp.route('/updateUser/<int:user_id>', methods=['PUT'])
def update_user(user_id):
    data = request.get_json() 
    
    updated = oUser.updateUser(data['name'],data['email'],data['task'],user_id) 

    if updated:
        return jsonify({'success': True, 'message': 'User updated successfully!'}), 200
    else:
        return jsonify({'success': False, 'message': 'User not found or update failed!'}), 404

