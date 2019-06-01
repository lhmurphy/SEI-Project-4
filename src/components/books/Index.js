import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'
import Promise from 'bluebird'

import Card from './Card'

class Index extends React.Component {

  constructor() {
    super()

    this.state = {
      locationId: ''
    }

    this.handleChange = this.handleChange.bind(this)
  }

  componentDidMount() {
    Promise.props({
      books: axios.get('/api/books').then(res => res.data),
      locations: axios.get('/api/locations').then(res => res.data)
    })
      .then(data => this.setState({ books: data.books, locations: data.locations, reviews: data.reviews }))
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

  render() {
    if(!this.state.books) return null
    console.log(this.state.books)
    console.log(this.state.reviews)
    return (
      <main>
        <div className="book-button">
          <a className="button">Add a book</a>
        </div>
        <section className="section">
          <div className="container">
            <div className="columns is-multiline">
              <div className="field" id="books-index">
                <div className="control">
                  <div className="select">
                    <select
                      name="location"
                      onChange={this.handleChange}
                    >
                      <option value="">All
                      </option>
                      {this.state.locations.map(location =>
                        <option key={location.id} value={location.id}>{location.name}</option>
                      )}
                    </select>
                    <p> Featured reads...</p>

                  </div>
                  {this.filterBooks().map(book =>
                    <div key={book.id} className="column is-full-desktop is-full-tablet">
                      <Link to={`/books/${book.id}`}>
                        <Card {...book} />
                      </Link>
                    </div>
                  )}
                </div>
              </div>
            </div>
          </div>
        </section>
      </main>
    )
  }
}

export default Index
