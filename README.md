# SEI-Project-3: Wanderlist
---

## Timeframe - 8 days in a group of 4 developers
***

## Technologies/ Frameworks used:
***
* HTML5
* SCSS
* Python
* Bulma
* React.js
* Webpack
* PonyORM
* Axios
* Promise
* Request-Promise
* Flask
* Marshmallow
* Git
* GitHub
* Heroku
* Insomnia
* Trello

## Overview
***
Wanderlist is a community-based book recommendation site for users to find their next read based on their travel destination.

![HOMEPAGE](https://user-images.githubusercontent.com/38182323/59762521-5412af00-928f-11e9-9696-80e039e2dfcc.png)

You can find a hosted version here ----> https://lauras-travel-books.herokuapp.com/

## Functionality
****

* As this is a community based website, users are only able to interact with the site after creating an account and logging in
* The landing page prompts the user to register or log in
* Once logged in, an Index page showcases all the books that have been uploaded by current users
* On the Index page, user can use the drop down to show books by specific locations
* The user can also submit a book on the Index page
* Books can be added, edited and deleted only by the user who created them
* Users can leave reviews on any book they like

## Development process

The initial planning phase included drawing out the relational database and models, wire framing the frontend and prioritising tasks on Trello.  

The backend was built with Python and PostgreSQL using SQLAlchemy for database interaction and Flask providing functionality for the API framework. Flask methods like Blueprint provided http requests for register and login routing. All API endpoints were tested in Insomnia before building the frontend:

![INSOMNIA](https://user-images.githubusercontent.com/38182323/59762353-00a06100-928f-11e9-8719-a80678fa4fb7.png)

### Database relationships

Books to Location: Many to many
Books to Reviews: One to many
Books to User: Many to one
User to Reviews: One to many

### Filtering by location

To be able to filter the books by location, I made two separate axios requests, one for the books and one for the locations. The handleChange then listens to what the user clicks onto whilst the filterBooks function shows all of the books if nothing has been selected, otherwise it executes a filter through each book and then maps through each location to return the books that have the matching location ID:

```javascript
componentDidMount() {
  Promise.props({
    books: axios.get('/api/books').then(res => res.data),
    locations: axios.get('/api/locations').then(res => res.data)
  })
    .then(data => this.setState({ books: data.books, locations: data.locations, reviews: data.reviews }))
    .catch(err => this.setState({ errors: err.response.data.errors}))
}

handleChange(e) {
  this.setState({ locationId: e.target.value })
}

filterBooks() {
  if(!this.state.locationId) {
    return this.state.books
  }
  return this.state.books.filter(book => {
    const locationIds = book.locations.map(location => location.id)
    return locationIds.includes(this.state.locationId)
  })
}
```

## Design
***

The frontend was built using React and Bulma, I wanted to keep the design clean and simple and make the book jackets the central focus.

![INDEX](https://user-images.githubusercontent.com/38182323/59763911-9093da00-9292-11e9-9c9f-e76ffb5e0290.png)

## Wins
***

When the user adds a new book or edits an existing book, I used React-Select for the locations field in the form. This feature enables the user to select a location from a list but to also type the first few letters of a location and autofill will give options for suggested places - I wanted this feature to prevent the user from misspelling a location and therefor adding incorrect data to the database.

![REACT-SELECT](https://user-images.githubusercontent.com/38182323/59762617-86241100-928f-11e9-8312-5283f9e822e6.png)

I learnt a lot about creating relationships between models, I had to ensure to include Set data type for all collections (lists) and to save them as Nested within the Schemas. To avoid recursion I had to made some exclusions:

```javascript
class Book(db.Entity):
    title = Required(str)
    author = Required(str)
    isbn = Required(str)
    genre = Required(str)
    date = Optional(int)
    jacket = Required(str)
    description = Required(str)
    fiction = Optional(bool)
    locations = Set('Location')
    reviews = Set('Review')
    user = Required('User')

class BookSchema(Schema):
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True)
    author = fields.Str(required=True)
    isbn = fields.Str(required=True)
    genre = fields.Str(required=True)
    date = fields.Int(required=False)
    jacket = fields.Str(required=True)
    description = fields.Str(required=True)
    fiction = fields.Bool(required=False)
    locations = fields.Nested('LocationSchema', many=True, exclude=('books', ), dump_only=True)
    location_ids = fields.List(fields.Int(), load_only=True)
    reviews = fields.Nested('ReviewSchema', many=True, dump_only=True, exclude=('book', ))
    user = fields.Nested('UserSchema', exclude=('books', 'reviews'))
```

## Challenges
***

React-Select posed one of the greatest challenges in this project (detailed above). However, the Edit form created another element of complication when sending back the data to the database, I was getting errors because the form was attempting to send back all of the data so I needed to delete these in the handleSubmit:   

```javascript
handleSubmit(e) {
  e.preventDefault()
  const token = Auth.getToken()
  const data = {...this.state.data}
  delete data.id
  delete data.user
  delete data.locations
  delete data.reviews
  axios.put(`/api/books/${this.props.match.params.id}`, data, {
    headers: { 'Authorization': `Bearer ${token}` }
  })
    .then(() => this.props.history.push('/books'))
    .catch(err => this.setState({ errors: err.response.data.errors }))
}
```

## Future features / Enhancement

* Additional filtering my title, author and genre
* Map to find local bookshops
* Use external API to retrieve data about local bookshops and link to map
* Add functionality so that users can like/upvote books
