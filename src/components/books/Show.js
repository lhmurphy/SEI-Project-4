import React from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'

class Show extends React.Component {

  constructor(props) {
    super(props)

    this.state = {
      books: null
    }

    this.handleDelete = this.handleDelete.bind(this)
  }

  componentDidMount() {
    axios.get(`/api/books/${this.props.match.params.id}`)
      .then(res => this.setState({ book: res.data }))
  }

  handleDelete() {
    axios.delete(`/api/books/${this.props.match.params.id}`, {
    })
      .then(() => this.props.history.push('/books'))
  }

  render() {
    if(!this.state.book) return null
    return (
      <section className="section">
        <div className="container">
          <h1 className="title is-1">{this.state.book.name}</h1>
          <Link to={`/books/${this.state.book.id}/edit`} className="button is-primary">Edit</Link>
          <button className="button is-danger" onClick={this.handleDelete}>Delete</button>
          <hr />
          <div className="card">
            <div className="card-image">
              <figure className="image">
                <div className="columns is-multiline">
                  <div className="column is-half-desktop is-full-tablet">

                    <img src={this.state.book.jacket} alt={this.state.book.title} />
                  </div>

                  <div className="column is-half-desktop is-full-tablet">
                    <h2 className="title is-2">{this.state.book.author}</h2>
                    <hr />
                    <h2 className="title is-2">Tasting Notes</h2>
                    <p className="is-size-4">{this.state.book.description}</p>
                  </div>
                </div>
              </figure>
            </div>
          </div>

        </div>
      </section>
    )
  }
}

export default Show
