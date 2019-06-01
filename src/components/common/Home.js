import React from 'react'
import Auth from '../../lib/Auth'
import { Link } from 'react-router-dom'


class Home extends React.Component{
  constructor(props) {
    super(props)

    this.state = {
      books: []
    }
  }

  render() {
    return(
      <div className="home">
        <div className="container full-height">
          <div className="columns">
            <div className="column is-two-fifths">
            </div>
            <div className="column">
              <h1>Welcome to Wanderlist</h1>
              <p>
                Travelling somewhere? Match your next read to your destination with Wanderlist. Books set in locations around the world!...
                <br />
                {!Auth.isAuthenticated() && <Link to="/register" className="button is-danger">Register</Link>}
                {!Auth.isAuthenticated() && <Link to="/login" className="button is-danger">Login</Link>}
                <br />
                {Auth.isAuthenticated() && <Link to="/books" className="button is-danger">Browse books...</Link>}

              </p>
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
