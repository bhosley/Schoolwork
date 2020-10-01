// 1. Create a new database named “blogger”:
use blogger

// 2. Create 3 users with _id = **
//    The users collection should contain the fields name and email. 
//    For the field _id, use ObjectId instead of String.  
//    Ex:  "_id" : ObjectId("5bb26043708926e438db6cad")

//    "5bb26043708926e438db6cad", 
db.users.insert({
    _id:ObjectId("5bb26043708926e438db6cad"),
    name:"John Doe",
    email:"John.D@mail.site" 
})
//    "5bb26043708926e438db6cae", 
db.users.insert({
    _id:ObjectId("5bb26043708926e438db6cae"),
    name:"Johnny Dough",
    email:"JohnnyDoughGood@mail.site" 
})
//    "5bb26043708926e438db6caf" 
db.users.insert({
    _id:ObjectId("5bb26043708926e438db6caf"),
    name:"Jeremy Do",
    email:"JD@mail.site" 
})

// 2.1. List the contents of the users collection in pretty form
db.users.find().pretty()

// 2.2. Search for user 5bb26043708926e438db6cad
db.users.find({"_id":ObjectId("5bb26043708926e438db6cad")})

// 3. Create 3 blogs with fields: 
//      title, body, slug, author, 
//      comments (array with objects containing user_id, comment, approved, created_at), 
//      and category (array with objects containing name)
db.blogs.insert({
    title:"",
    body:"",
    slug:"",
    author:"",
    comments:[
        {
            user_id:ObjectId(""),
            comment:"",
            approved:true,
            created_at:ISODate()
        },
    ],
    category:[
        {name:""}
        {name:""}
    ]
})
// The user_id and author fields should be one of the 3 users _id found above
db.blogs.insert({
    title:"",
    body:"",
    slug:"",
    author:"",
    comments:[
        {
            user_id:ObjectId(""),
            comment:"",
            approved:true,
            created_at:ISODate()
        },
    ],
    category:[
        {name:""}
        {name:""}
    ]
})
// One of the posts should contain the word "framework" in the body
db.blogs.insert({
    title:"",
    body:"",
    slug:"",
    author:"",
    comments:[
        {
            user_id:ObjectId(""),
            comment:"",
            approved:true,
            created_at:ISODate()
        },
    ],
    category:[
        {name:""}
        {name:""}
    ]
})
// 3.1 Get all comments by User 5bb26043708926e438db6caf across all posts displaying only the title and slug

// 4. Select a blog via a case-insensitive regular expression containing the word Framework in the body displaying only the title and body
db.blogs.find()