'use strict';

//HTTPS
const fs = require('fs');
const https = require('https');
const privateKey  = fs.readFileSync('/etc/ssl/private/server_key.key', 'utf8');
const certificate = fs.readFileSync('/etc/ssl/private/server_cert.cer', 'utf8');
const credentials = {key: privateKey, cert: certificate};

const express = require('express');
const app = express();

const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const path = require('path');
const { check, validationResult } = require('express-validator/check');

// Global Vars
app.use(function(req, res, next){
		res.locals.errors = null;
		next();
		});

//support parsing of application/json type post data
app.use(bodyParser.json());

//support parsing of application/x-www-form-urlencoded post data
app.use(bodyParser.urlencoded({ extended: true }));

const methodOverride = require('method-override');
app.use(methodOverride('_method', { methods: ['POST', 'GET'] }));
app.use(methodOverride(function (req, res) {
			if (req.body && typeof req.body === 'object' && '_method' in req.body) {
			// look in urlencoded POST bodies and delete it
			var method = req.body._method
			delete req.body._method
			return method
			}
			}))

// View Engine
app.set('view engine', 'ejs');
app.set('views', path.join(__dirname, 'views'));

//LOGS
var morgan = require('morgan');
app.use(morgan('combined'));
var winston = require('./config/winston');
app.use(morgan('combined', { stream: winston.stream }));

//User Model
var User = require('./models/user');

// Connect to MongoDB on VM
mongoose.connect('mongodb://10.92.128.52:27017/blogger', { useNewUrlParser: true });
const db = mongoose.connection;

//API ROUTES
//SHOW
app.get('/api/users', function(req, res) {
		User.getUsers(function(err, users) {
				if(err){
				throw err;
				}
				res.json(users);
				});
		});

app.get('/api/users/:_id', function(req, res) {
		User.getUserById(req.params._id, function(err, user) {
				if(err){
				throw err;
				}
				res.json(user);
				});
		});

//STORE
app.post('/api/users', function(req, res){
		var user = req.body;

		User.addUser(user, (err, user) => {
				if(err){
				throw err;
				}

				res.json(user);
				});
		});

//UPDATE
app.put('/api/users/:_id', function(req, res){
		var user = req.body;

		const options = {returnNewDocument:true};

		User.updateUser(req.params._id, user, options, (err, user) => {
				if(err){
				throw err;
				}

				res.json(user);
				});

		});

//DESTROY
app.delete('/api/users/:_id', function(req, res) {
		User.removeUser(req.params._id, function(err, user) {
				if(err){
				throw err;
				}
				res.json(user);
				});
		});

//WEB ROUTES
//INDEX root website/SHOW
app.get('/', function(req, res){
		User.getUsers(function(err, users){
				res.render('index', {
users: users
});
				})
		});
//EDIT
app.get('/users/edit/:_id', function(req, res) {
		User.getUserById(req.params._id, function(err, user) {
				if(err){
				throw err;
				}
				res.render('edit', {
user: user
});

				});
		});

//DESTROY
app.delete('/users/delete/:_id', function(req, res) {
		User.removeUser(req.params._id, function(err, user) {
				if(err){
				throw err;
				}
				res.redirect('/');
				});
		});

//STORE
app.post('/users/add', [check('name').not().isEmpty().withMessage('Name is a required field.'), check('email').not().isEmpty().withMessage('Email is a required field.'), check('email').isEmail().withMessage('Email field is not a valid email address.')], function(req, res){

		const errors = validationResult(req);

		if(!errors.isEmpty())
		{
		User.getUsers(function(err, users){
				res.render('index', {
users: users,
errors: errors.array()
})
				});
		}

		else
		{
		var newUser = {
name: req.body.name,
email: req.body.email
}

User.addUser(newUser, (err, user) => {
		if(err){
		throw err;
		}

		res.redirect('/');
		});
}//end of else

}
);

//UPDATE
app.put('/users/edit/:_id', [check('name').not().isEmpty().withMessage('Name is a required field.'), check('email').not().isEmpty().withMessage('Email is a required field.'), check('email').isEmail().withMessage('Email field is not a valid email address.')], function(req, res){

		const errors = validationResult(req);

		var newUser = {
_id: req.params._id,
name: req.body.name,
email: req.body.email
}

if(!errors.isEmpty())
{

res.render('edit', {
user: newUser,
errors: errors.array()
});

}//end of if errors

else
{
	const options = {returnNewDocument:true};
	User.updateUser(req.params._id, newUser, options, (err, user) => {
			if(err){
			throw err;
			}

			res.redirect('/');
			});
}//end of else

}
);

//
// Begin Programming Project 1
//
var Blog = require('./models/blog');

//API Routes

app.get('/api/blogs', function(req, res) {
	Blog.getBlogs(function(err, blogs) {
		if(err){ throw err; }
		res.json(blogs);
	});
});
app.get('/api/blogs/:_id', function(req, res) {
	Blog.getBlogById(req.params._id, function(err, blog) {
		if(err){ throw err; }
		res.json(blog);
	});
});
app.post('/api/blogs', function(req, res){
	var blog = req.body;
	Blog.addBlog(blog, (err, blog) => {
		if(err){ throw err; }
		res.json(blog);
	});
});
app.put('/api/blogs/:_id', function(req, res){
	var blog = req.body;
	const options = {returnNewDocument:true};
	Blog.updateBlog(req.params._id, blog, options, (err, blog) => {
		if(err){ throw err; }
		res.json(blog);
	});
});
app.delete('/api/blogs/:_id', function(req, res) {
	Blog.removeBlog(req.params._id, function(err, blog) {
		if(err){ throw err; }
		res.json(blog);
	});
});

// Web Routes

app.get('/blogs', function(req, res){
	Blog.getBlogs(function(err, blogs){
		User.getUsers(function(err, users){
			res.render('blogs', {
				blogs: blogs,
				users: users 
			});
		})
	})
});

app.get('/blogs/edit/:_id', function(req, res) {
	Blog.getBlogById(req.params._id, function(err, blog) {
		if(err){ throw err; }
		User.getUsers(function(err, users){
			res.render('editBlog', {
				blog: blog,
				users: users 
			});
		})
	})
});

app.delete('/blogs/delete/:_id', function(req, res) {
	Blog.removeBlog(req.params._id, function(err, blog) {
		if(err){throw err;}
		res.redirect('/blogs');
	});
});

//CREATE
app.post('/blogs/add', [
		check('title').not().isEmpty().withMessage('Title is a required field.'), 
		check('slug').not().isEmpty().withMessage('Slug is a required field.'),
		check('body').not().isEmpty().withMessage('Body is a required field.'),
		check('category').not().isEmpty().withMessage('Category is a required field.') ],
		function(req, res){

	const errors = validationResult(req);
	if(!errors.isEmpty()) {
		Blog.getBlogs(function(err, blogs){
			res.render('blogs', {blogs: blogs, errors: errors.array() })
		});
	} else {
		var newBlog = {
			title: req.body.title,
			slug: req.body.slug,
			author: req.body.author,
			body: req.body.body,
			comments:[{
				user_id: req.body.author,
				comment: req.body.comment,
				approved:true,
				created_at: Date() }],
			category: [{name: req.body.category}]
		}
		Blog.addBlog(newBlog, (err, blog) => {
			if(err){ throw err; }
			res.redirect('/blogs');
		});
	}//end of else
});

//UPDATE
app.put('/blogs/edit/:_id', [
	check('title').not().isEmpty().withMessage('Title is a required field.'), 
	check('slug').not().isEmpty().withMessage('Slug is a required field.'),
	check('body').not().isEmpty().withMessage('Body is a required field.'),
	check('comments').not().isEmpty().withMessage('Comments is a required field.'),
	check('category').not().isEmpty().withMessage('Category is a required field.') ],
	function(req, res){

	const errors = validationResult(req);
	var newBlog = {
		_id: req.params._id,
		title: req.body.title,
		slug: req.body.slug,
		author: req.body.author,
		body: req.body.body,
		comments:[{
			user_id: req.body.author,
			comment: req.body.comments,
			approved:true,
			created_at: Date() }],
		category: [{name: req.body.category}]
	}
	if(!errors.isEmpty()) {
		User.getUsers(function(err, users){
			res.render('editBlog', {
				blog: newBlog,
				users: users,
				errors: errors.array()
			});
		})

	} else {
		const options = {returnNewDocument:true};
		Blog.updateBlog(req.params._id, newBlog, options, (err, blog) => {
			if(err){ throw err; }
			res.redirect('/blogs');
		});
	}//end of else
});

const httpsServer = https.createServer(credentials, app);
httpsServer.listen(8443);
console.log('Running on port 8443...');