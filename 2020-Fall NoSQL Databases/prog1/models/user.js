const mongoose = require('mongoose');

// User Schema
const userSchema = mongoose.Schema({
	name:{
		type: String,
		required: true
	},
	email:{
		type: String,
		default: true
	}
});

const User = module.exports = mongoose.model('User', userSchema);

// Get All Users - find method
module.exports.getUsers = (callback, limit) => {
        User.find(callback).limit(limit);
}

// Get User - findById method
module.exports.getUserById = (id, callback, limit) => {
		User.findById(id, callback).limit(limit);
}

// Add User - create method
module.exports.addUser = (user, callback, limit) => {
		User.create(user, callback);
}

// Update User - findOneAndUpdate method
module.exports.updateUser = (id, user, options, callback, limit) => {
	User.findOneAndUpdate({_id: id}, user, options, callback);
}

// Delete User - deleteOne method
module.exports.removeUser = (id, callback, limit) => {
	User.deleteOne({_id: id}, callback).limit(limit);
}
