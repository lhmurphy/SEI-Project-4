import React from 'react'
import axios from 'axios'

//import { Link } from 'react-router-dom'
import Form from './../books/Form'

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
              When you're planning your next trip...
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
