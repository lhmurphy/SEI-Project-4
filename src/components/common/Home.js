import React from 'react'
//import { Link } from 'react-router-dom'

class Home extends React.Component{
  constructor() {
    super()

    this.state = {
      locations: []

    }
  }

  render() {
    return(
      <div className="home">
        <div className="container full-height">
          <div className="columns">
            <div className="column is-two-fifths">is-two-fifths</div>
            <div className="column">Auto</div>
          </div>
        </div>
      </div>
    )
  }

}

export default Home
