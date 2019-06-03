import React from 'react'
import axios from 'axios'
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

class BooksNew extends React.Component {


  constructor() {
    super()

    this.state = {
      data: {
        location_ids: []
      },
      books: '',
      errors: {}
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.handleLocationChange = this.handleLocationChange.bind(this)

  }

  componentDidMount() {
    axios.get('/api/books')
      .then(res => this.setState({ books: res.books }))
      .catch(err => this.setState({ errors: err.response.data.errors}))
  }


  handleChange(e) {
    const data = { ...this.state.data, [e.target.name]: e.target.value }
    this.setState({ data })
  }

  handleSubmit(e) {
    e.preventDefault()

    axios.post('/api/books', this.state.data, {
      headers: { 'Authorization': `Bearer ${Auth.getToken()}`}
    })
      .then(() => this.props.history.push('/books'))
      .catch(err => this.setState({ errors: err.response.data.errors }))
  }

  handleLocationChange(selectedLocation) {
    const selectedLocations = selectedLocation.map(location => location.value)
    const data = { ...this.state.data, location_ids: [ ...selectedLocations ] }
    this.setState({ data })
  }

  render() {
    console.log('this.state.books', this.state.books)
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

export default BooksNew
