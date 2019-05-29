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

  componentDidMount() {
    axios.get('/api/books')
      .then(res => this.setState({ books: res.data}))
  }

  handleChange({target: { name, value }}) {
    const data = {...this.state.data, [name]: value }
    const errors = { ...this.state.errors, [name]: '' }
    this.setState({ data, errors })
  }

  handleSubmit(e) {
    e.preventDefault()
    axios
      .post('/api/register', this.state.data)
      .then(() => this.props.history.push('/login'))
      .catch((err) => this.setState({errors: err.response.data}))
  }

  render() {
    return(
      <div className="home">
        <div className="container full-height">
          <div className="columns">
            <div className="column is-two-fifths">
              <Form
                handleChange={this.handleChange}
                handleSubmit={this.handleSubmit}
                data={this.state.data}
              />
            </div>
            <div className="column">Welcome to Wanderlist</div>
          </div>
        </div>
      </div>
    )
  }

}

export default Home
