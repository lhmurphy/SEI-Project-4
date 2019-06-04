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
  }

  render() {
    console.log(this.state.books)
    console.log(this.state.author)

    return(
      <div className="home">
        <div className="container full-height">
          <div className="columns">
            <div className="column">
              <div className="hero">

                <h1>Welcome to Wanderlist</h1>
                <div>
                  Travelling somewhere? Match your next read to your destination with Wanderlist. Books set in locations around the world!...
                  <br />
                  {!Auth.isAuthenticated() && <Link to="/register" className="button is-danger">Register</Link>}
                  {!Auth.isAuthenticated() && <Link to="/login" className="button is-danger">Login</Link>}
                  <br />
                  {Auth.isAuthenticated() && <Link to="/books" className="button is-danger"><h2>Discover Great Books</h2></Link>}
                </div>
              </div>
            </div>
          </div>
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
