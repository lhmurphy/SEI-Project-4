import React from 'react'
import { Link } from 'react-router-dom'
import axios from 'axios'
import Auth from '../../lib/Auth'

class Show extends React.Component {

  constructor() {
    super()

    this.state = {
      book: null,
      data: {}
    }

    this.handleDelete = this.handleDelete.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
    this.handleChange = this.handleChange.bind(this)

  }

  componentDidMount() {
    axios.get(`/api/books/${this.props.match.params.id}`)
      .then(res => this.setState({ book: res.data }))
  }

  handleChange(e) {
    const data = { ...this.state.data, [e.target.name]: e.target.value }
    this.setState({ data })
  }

  handleSubmit(e) {
    e.preventDefault()

    axios.post(`/api/books/${this.props.match.params.id}/reviews`, this.state.data, {
      headers: { 'Authorization': `Bearer ${Auth.getToken()}`}
    })
      .then(res => this.setState({ book: res.data }))

      .then(() => this.setState({ content: '' }))

  }

  handleDelete() {
    axios.delete(`/api/books/${this.props.match.params.id}`, {
      headers: { 'Authorization': `Bearer ${Auth.getToken()}`}
    })
      .then(() => this.props.history.push('/books'))
  }

  render() {
    if(!this.state.book) return null
    if(!this.state.data) return null
    console.log(this.state.book)

    return (
      <section className="section">
        <div className="container">
          <div className="card is-horizontal columns" id="books-show">
            <figure className="image is-128x128px">
              <img src={this.state.book.jacket} alt={this.state.book.title} />
            </figure>
            <div className="card-content">
              <p className="title is-2">{this.state.book.title}</p>
              <p>{this.state.book.author}</p>
              <p>{this.state.book.genre}</p>
              <p>{this.state.book.review}</p>
              <Link to={`/books/${this.state.book.id}/edit`} className="button is-primary">Edit</Link>
              <button className="button is-danger" onClick={this.handleDelete}>Delete</button>
              <br />
              <button className="button" onClick={this.handleDelete}>Review this book</button>

            </div>
          </div>
          <div className="card is-horizontal columns" id="books-show">
            <p>{this.state.book.description}</p>
          </div>
        </div>
        {this.state.book.reviews.map(review =>
          <article key={review.id} className="media">
            <figure className="media-left">
              <p className="image is-64x64">
                <img src={review.user.image} />
              </p>
            </figure>
            <div className="media-content">

              <div className="content">
                <p className="commentText">
                  <strong>{review.user.username}</strong>  <small>{review.created_at.substring(0, review.created_at.length - 8)}</small>
                  <br />
                  {review.content}
                </p>
              </div>
            </div>
          </article>)}

        <article className="media">
          <figure className="media-left">
            <p className="image is-64x64">
              <img src="https://bulma.io/images/placeholders/128x128.png" />
            </p>
          </figure>
          <div className="media-content">
            <div className="field">
              <p className="control">
                <textarea className="textarea" name="content" onChange={this.handleChange} placeholder="Add a comment..." />
              </p>
            </div>
            <nav className="level">
              <div className="level-left">
                <div className="level-item">
                  <button className="button is-info" onClick={this.handleSubmit}>Submit</button>

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
