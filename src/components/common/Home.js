import React from 'react'
import Auth from '../../lib/Auth'
import { Link } from 'react-router-dom'
import axios from 'axios'

class Home extends React.Component{
  constructor(props) {
    super(props)

    this.state = {
      books: []
    }
  }

  componentDidMount() {
    axios.get('/api/books')
      .then(res => this.setState({ books: res.data }))

    setInterval(() => {
      let currentImg = this.state.currentImg + 1
      currentImg === this.state.images.length ? currentImg = 0:null
      this.setState({ currentImg })
    }, 4000)
  }

  render() {
    console.log(this.state.books)
    console.log(this.state.author)

    return(
      <div className="home">
        <div className="home-container">
          <h1>Welcome to Wanderlist</h1>
            Join the Wanderlist community to discover and share books that match your next travel destination.
          <br />
          {!Auth.isAuthenticated() && <Link to="/register" className="button is-danger">Register</Link>}
          {!Auth.isAuthenticated() && <Link to="/login" className="button is-danger">Login</Link>}
          <br />
          {Auth.isAuthenticated() && <Link to="/books" className="button is-danger"><h2>Find your next read</h2></Link>}
        </div>
      </div>
    )
  }

}

export default Home












// <Form
// handleChange={this.handleChange}
// handleSubmit={this.handleSubmit}
// data={this.state.data}
// />
