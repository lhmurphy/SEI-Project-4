import React from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'


class Show extends React.Component {

  constructor() {
    super()

    this.state = {
      books: null
    }

    this.handleDelete = this.handleDelete.bind(this)
  }

  componentDidMount() {
    axios.get(`/api/books/${this.props.match.params.id}`)
      .then(res => this.setState({ books: res.data }))
  }

  handleDelete() {
    axios.delete(`/api/books/${this.props.match.params.id}`, {
    })
      .then(() => this.props.history.push('/books'))
  }

  render() {
    if(!this.state.books) return null
    console.log(this.state.reviews)

    return (
      <section className="section">
        <div className="container">
          <div className="card is-horizontal columns" id="books-show">
            <figure className="image is-128x128px">
              <img src={this.state.books.jacket} alt={this.state.books.title} />
            </figure>
            <div className="card-content">
              <p className="title is-2">{this.state.books.title}</p>
              <p>{this.state.books.author}</p>
              <p>{this.state.books.genre}</p>
              <p>{this.state.books.review}</p>
              <Link to={`/books/${this.state.books.id}/edit`} className="button is-primary">Edit</Link>
              <button className="button is-danger" onClick={this.handleDelete}>Delete</button>
              <br />
              <button className="button" onClick={this.handleDelete}>Review this book</button>

            </div>
          </div>
          <div className="card is-horizontal columns" id="books-show">
            <p>{this.state.books.description}</p>
          </div>
          <div className="card is-horizontal columns" id="books-show">
            <p className="card-header-title">Reviews</p>
            {this.state.books.reviews.map(review =>
              <option key={review.id} value={review.id}>{review.content}</option>
            )}

          </div>
        </div>
        <article className="media">
          <figure className="media-left">
            <p className="image is-64x64">
              <img src="https://bulma.io/images/placeholders/128x128.png" />
            </p>
          </figure>
          <div className="media-content">
            <div className="field">
              <p className="control">
                <textarea className="textarea" placeholder="Add a comment..."></textarea>
              </p>
            </div>
            <nav className="level">
              <div className="level-left">
                <div className="level-item">
                  <a className="button is-info">Submit</a>
                </div>
              </div>
            </nav>
          </div>
        </article>
      </section>
    )
  }
}

export default Show
