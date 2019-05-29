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
          <h1>HELLOW!</h1>
        </div>
      </div>
    )
  }

}

export default Home
