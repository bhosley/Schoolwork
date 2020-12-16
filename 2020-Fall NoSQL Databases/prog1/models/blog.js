const mongoose = require('mongoose');

// Blog Schema
const blogSchema = mongoose.Schema({
	title:{
		type: String,
		required: true
	},
	slug:{
		type: String,
		default: true
    },
    body:{
		type: String,
		default: true
    },
    author:{
		type: String,
		default: true
    },
    comments:{
		type: Array,
		user_id:{type: String},
		comment:{type: String},
		approved:{type: Boolean},
		created_at:{type: Date}
	},
    category:{
		type: Array,
		default: true
	}
});

const Blog = module.exports = mongoose.model('Blog', blogSchema);

module.exports.getBlogs = (callback, limit) => {
    Blog.find(callback).limit(limit);
}

module.exports.getBlogById = (id, callback, limit) => {
	Blog.findById(id, callback).limit(limit);
}

module.exports.addBlog = (blog, callback, limit) => {
	Blog.create(blog, callback);
}

module.exports.updateBlog = (id, blog, options, callback, limit) => {
	Blog.findOneAndUpdate({_id: id}, blog, options, callback);
}

module.exports.removeBlog = (id, callback, limit) => {
	Blog.deleteOne({_id: id}, callback).limit(limit);
}
