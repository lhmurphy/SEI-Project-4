import React from 'react'
import axios from 'axios'
import Select from 'react-select'


class Form extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      // is this the correct way to store each batch of data for the search fields?
      data: [],
      location: 'All',
      searchResults: null
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  componentDidMount() {
    axios.get('/api/books')
      .then(res =>  this.setState({ data: res.data}))

  }

  handleChange(e) {

  }

  handleSubmit(e) {
    e.preventDefault()

    axios.post('/api/locations', this.state.data)
      .then(res => {
        this.props.history.push('/books/${location.id}')
      })
      .catch(() => this.setState({ error: 'This location does not exist' }))
  }

  searchBooks() {




    // const books = this.searchBooks()
    // if(this.state.location === 'All') return this.props.data
    // return books.filter(book => {
    //   return book.location === this.state.location
    // })
    // get all book data from axios
    // if statement: if input from user matches book location id...
    // go to that page showing all books from that search
    // use https://github.com/lutangar/cities.json to search cities

  }

  render() {
    console.log(this.state.data)
    console.log(this.state.locations)
    return (
      <form onSubmit={this.state.handleSubmit}>
        <div className="field">
          <div className="control">
            <input id="form-Input"
              className="input"
              name="location"
              placeholder="Location..."
              onChange={this.handleChange}
            />
          </div>
        </div>
        <div className="field">
          <div className="control">
            <input id="form-Input"
              className="input"
              name="author"
              placeholder="Author..."
            />
          </div>
        </div>
        <div className="field">
          <div className="control">
            <input id="form-Input"
              className="input"
              name="genre"
              placeholder="Genre..."
            />
          </div>
        </div>
        <div className="field">
          <div className="control">
            <input id="form-Input"
              className="input"
              name="title"
              placeholder="Title..."
            />
          </div>
        </div>


        <button className="buttonNew">Submit</button>
      </form>
    )
  }
}

export default Form
