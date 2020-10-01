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
// The user_id and author fields should be one of the 3 users _id found above
db.blogs.insert({
    title:"How to Say a Lot Without Saying Anything; In Latin",
    body:"Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    slug:"Lorem-Ipsum",
    author:ObjectId("5bb26043708926e438db6cad"),
    comments:[
        {
            user_id:ObjectId("5bb26043708926e438db6caf"),
            comment:"Great post! I will be sure to use this in my daily life!",
            approved:true,
            created_at:ISODate("2020-09-10")
        }
    ],
    category:[
        {name:"culture"},
        {name:"linquistics"}
    ]
})
db.blogs.insert({
    title:"Another Post with Pictures of my Cat",
    body:"In this post I will present even more pictures of my cat....",
    slug:"Cat-Pics-10",
    author:ObjectId("5bb26043708926e438db6cae"),
    comments:[
        {
            user_id:ObjectId("5bb26043708926e438db6cad"),
            comment:"catterino doin me a heckin scur.",
            approved:true,
            created_at:ISODate("2020-09-21")
        }
    ],
    category:[
        {name:"photojournalism"},
        {name:"travel"}
    ]
})
// One of the posts should contain the word "framework" in the body
db.blogs.insert({
    title:"Thoughts on HTML as a Programming Language",
    body:"I used to think HTML programmers inferior until a unique illness befell me...",
    slug:"HTML-Programming",
    author:ObjectId("5bb26043708926e438db6caf"),
    comments:[
        {
            user_id:ObjectId("5bb26043708926e438db6cae"),
            comment:"Interesting concept. I will have to do more research.",
            approved:true,
            created_at:ISODate("2020-10-01")
        },{
            user_id:ObjectId("5bb26043708926e438db6caf"),
            comment:"WhAt A gReAt FrAmEwOrK",
            approved:false,
            created_at:ISODate("2020-10-03")
        }
    ],
    category:[
        {name:"op-ed"},
        {name:"controversial"}
    ]
})
// 3.1 Get all comments by User 5bb26043708926e438db6caf across all posts displaying only the title and slug
db.blogs.find({'comments.user_id':ObjectId("5bb26043708926e438db6caf")},
    {title:1,body:0,slug:1,author:0,comments:0,category:0})

// 4. Select a blog via a case-insensitive regular expression containing the word Framework in the body displaying only the title and body
db.blogs.find({body:/Framwork/i},
    {title:1,body:1,slug:0,author:0,comments:0,category:0})