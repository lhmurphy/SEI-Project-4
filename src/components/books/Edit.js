import React from 'react'
import axios from 'axios'
import Promise from 'bluebird'

import Auth from '../../lib/Auth'

class Edit extends React.Component {

  constructor() {
    super()

    this.state = {
      book: '',
      allLocations: {},
      errors: {}
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.handleDelete = this.handleDelete.bind(this)
  }

  componentDidMount() {
    Promise.props({
      book: axios.get(`/api/books/${this.props.match.params.id}`).then(res => res.data),
      allLocations: axios.get('/api/locations').then(res => res.data)
    })
      .then(res => this.setState({ book: res.book, allLocations: res.allLocations }))
      .catch(err => this.setState({ errors: err.response.data.errors}))
  }

  handleChange(e) {
    const data = { ...this.state.data, [e.target.name]: e.target.value }
    this.setState({ data })
  }

  handleSubmit(e) {
    e.preventDefault()

    const token = Auth.getToken()

    axios.put(`/api/books/${this.state.data._id}`, this.state.data, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
      .then(() => this.props.history.push('/books'))
      .catch(err => this.setState({ errors: err.response.data.errors }))
  }

  handleDelete() {
    const token = Auth.getToken()
    axios.delete(`/api/books/${this.state.data._id}`, this.state.data,  {
      headers: { 'Authorization': `Bearer ${token}` }
    })
      .then(() => this.props.history.push('/books'))
  }

  // componentDidMount() {
  //   setInterval(() => {
  //     let currentQuote = this.state.currentQuote + 1
  //     currentQuote === this.state.quotes.length ? currentQuote = 0:null
  //     this.setState({ currentQuote })
  //   }, 4000)
  // }

  filterBooks() {
    return this.state.book.filter(book => {
      const bookLocationIds = book.location.map(bookLocation => bookLocation.id)
      const locationIds = this.allLocations.map(allLocation => allLocation.id)

      if(bookLocationIds.id === locationIds.userId) {
        return locationIds
      }
    })
  }


  render() {
    if(!this.state.book.locations) return null
    console.log(this.state.allLocations)
    console.log(this.state.book)


    return (
      <section className="section">
        <div className="container">
          <div className="columns is-centered">
            <div className="column is-half-desktop is-two-thirds-tablet">
              <form onSubmit={this.handleSubmit}>
                <div className="field">
                  <label className="label">Title</label>
                  <div className="control">
                    <input
                      className="input"
                      name="title"
                      placeholder="eg: Harry Potter"
                      onChange={this.handleChange}
                      value={this.state.book.title || ''}
                    />
                  </div>
                </div>
                <div className="field">
                  <label className="label">Author</label>
                  <div className="control">
                    <input
                      className="input"
                      name="author"
                      placeholder="eg: J.K. Rowling"
                      onChange={this.handleChange}
                      value={this.state.book.author || ''}
                    />
                  </div>
                </div>
                <div className="field">
                  <label className="label">ISBN</label>
                  <div className="control">
                    <input
                      className="input"
                      name="isbn"
                      placeholder="eg: 9847987438753"
                      onChange={this.handleChange}
                      value={this.state.book.isbn || ''}
                    />
                  </div>
                </div>
                <div className="field">
                  <label className="label">Genre</label>
                  <div className="control">
                    <input
                      className="input"
                      name="genre"
                      placeholder="eg: Fantasy"
                      onChange={this.handleChange}
                      value={this.state.book.genre || ''}
                    />
                  </div>
                </div>
                <div className="field">
                  <label className="label">Publication year</label>
                  <div className="control">
                    <input
                      className="input"
                      name="date"
                      placeholder="eg: 1990"
                      onChange={this.handleChange}
                      value={this.state.book.year || ''}
                    />
                  </div>
                </div>
                <div className="field">
                  <label className="label">Jacket Image</label>
                  <div className="control">
                    <input
                      className="input"
                      name="jacket"
                      placeholder="eg: https://images-na.ssl-images-amazon.com/images/I/51HSkTKlauL._SX346_BO1,204,203,200_.jpg"
                      onChange={this.handleChange}
                      value={this.state.book.image || ''}
                    />
                  </div>
                </div>
                <div className="field">
                  <label className="label">Book blurb</label>
                  <div className="control">
                    <textarea
                      className="textarea"
                      name="description"
                      placeholder="eg: Harry Potter is based in the UK..."
                      onChange={this.handleChange}
                      value={this.state.book.description || ''}
                    />
                  </div>
                </div>
                <div className="field">
                  <label className="label">Locations</label>
                  <div className="control">
                    <select
                      name="location"
                      onChange={this.handleChange}
                    >
                      <option value="">All
                      </option>

                      {this.state.allLocations.map(location =>
                        <option key={location.id} value={location.id}>{location.name}</option>
                      )}
                    </select>

                  </div>
                </div>
                <button className="button is-primary">Submit</button>
              </form>
            </div>
          </div>
        </div>
      </section>
    )
  }
}

export default Edit
