import React from 'react'
import axios from 'axios'
import Promise from 'bluebird'
import Select from 'react-select'

import Auth from '../../lib/Auth'

const locationOptions = [
  { value: 1, label: 'Amsterdam' },
  { value: 2, label: 'Paris' },
  { value: 3, label: 'Kansas' },
  { value: 4, label: 'Colombia' },
  { value: 5, label: 'Austria' },
  { value: 6, label: 'Azerbaijan' },
  { value: 7, label: 'Belgium' },
  { value: 8, label: 'Bhutan' },
  { value: 9, label: 'Chile' },
  { value: 10, label: 'Copenhagen' }
]

class Edit extends React.Component {

  constructor() {
    super()

    this.state = {
      data: {
        location_ids: [],
        book: ''
      },
      allLocations: {},
      errors: {}
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.handleDelete = this.handleDelete.bind(this)
    this.handleLocationChange = this.handleLocationChange.bind(this)

  }

  componentDidMount() {
    Promise.props({
      data: axios.get(`/api/books/${this.props.match.params.id}`).then(res => res.data),
      allLocations: axios.get('/api/locations').then(res => res.data)
    })
      .then(res => this.setState({ data: res.data, allLocations: res.allLocations }))
      .catch(err => this.setState({ errors: err.response.data.errors}))
  }

  handleChange(e) {
    const data = { ...this.state.data, [e.target.name]: e.target.value }
    this.setState({ data })
  }

  handleSubmit(e) {
    e.preventDefault()
    const token = Auth.getToken()
    const data = {...this.state.data}
    delete data['id']
    delete data['user']
    delete data['locations']
    delete data['reviews']
    axios.put(`/api/books/${this.props.match.params.id}`, this.state.data, {
      headers: { 'Authorization': `Bearer ${token}` }
    })
      .then(() => this.props.history.push('/books'))
      .catch(err => this.setState({ errors: err.response.data.errors }))
  }

  handleDelete() {
    const token = Auth.getToken()
    axios.delete(`/api/books/${this.props.match.params.id}`, this.state.data,  {
      headers: { 'Authorization': `Bearer ${token}` }
    })
      .then(() => this.props.history.push('/books'))
  }


  filterBooks() {
    return this.state.data.book.filter(book => {
      const bookLocationIds = book.location.map(bookLocation => bookLocation.id)
      const locationIds = this.allLocations.map(allLocation => allLocation.id)

      if(bookLocationIds.id === locationIds.userId) {
        return locationIds
      }
    })
  }

  handleLocationChange(selectedLocation) {
    const selectedLocations = selectedLocation.map(location => location.value)
    const data = { ...this.state.data, location_ids: [ ...selectedLocations ] }
    this.setState({ data })
  }


  render() {
    if(!this.state.data.locations) return null
    console.log(this.state.allLocations, 'all locations')
    console.log(this.state.data.id , 'id')
    console.log(this.state.data , 'data')


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
                      value={this.state.data.title || ''}
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
                      value={this.state.data.author || ''}
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
                      value={this.state.data.isbn || ''}
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
                      value={this.state.data.genre || ''}
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
                      value={this.state.data.year || ''}
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
                      value={this.state.data.image || ''}
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
                      value={this.state.data.description || ''}
                    />
                  </div>
                </div>
                <div className="field">
                  <label className="label">Locations</label>
                  <div className="control">
                    <Select
                      isMulti
                      clearValue
                      options={locationOptions}
                      onChange={this.handleLocationChange}
                      className="basic-multi-select"
                      classNamePrefix="select"
                      name="location_ids"
                      placeholder="eg: London"
                      key={location.label}
                    />
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

// componentDidMount() {
//   setInterval(() => {
//     let currentQuote = this.state.currentQuote + 1
//     currentQuote === this.state.quotes.length ? currentQuote = 0:null
//     this.setState({ currentQuote })
//   }, 4000)
// }
