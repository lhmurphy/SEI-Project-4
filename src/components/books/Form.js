import React from 'react'
import axios from 'axios'

class Form extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      data: []
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  componentDidMount() {
    axios.get('/api/books')
      .then(res => this.setState({ data: res.data}))
  }

  handleChange({target: { name, value }}) {
    const data = {...this.state.data, [name]: value }
    this.setState({ data })
  }

  handleSubmit(e) {
    e.preventDefault()
    axios
      .then(() => this.props.history.push('/books'))
  }

  render() {
    return (
      <form onSubmit={this.state.handleSubmit}>
        <div className="field">
          <div className="control">
            <input id="form-Input"
              className="input"
              name="location"
              placeholder="Location..."
            />
          </div>
        </div>
        <div className="field">
          <div className="control">
            <input id="form-Input"
              className="input"
              name="author"
              placeholder="Author..."
            />
          </div>
        </div>
        <div className="field">
          <div className="control">
            <input id="form-Input"
              className="input"
              name="genre"
              placeholder="Genre..."
            />
          </div>
        </div>
        <div className="field">
          <div className="control">
            <input id="form-Input"
              className="input"
              name="title"
              placeholder="Title..."
            />
          </div>
        </div>

        <button className="buttonNew">Submit</button>
      </form>
    )
  }
}

export default Form
