import React from 'react'
import axios from 'axios'

class Form extends React.Component {
  constructor(props) {
    super(props)

    this.state = {
      locations: []
    }
  }

  componentDidMount() {
    axios.get('/api/locations')
      .then(res => this.setState({ locations: res.data}))
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
              onChange={this.state.handleChange}
              value={this.state.location || ''}
            />
          </div>
        </div>
        <div className="field">
          <div className="control">
            <input id="form-Input"
              className="input"
              name="author"
              placeholder="Author..."
              onChange={this.state.handleChange}
              value={this.state.author || ''}
            />
          </div>
        </div>
        <div className="field">
          <div className="control">
            <input id="form-Input"
              className="input"
              name="genre"
              placeholder="Genre..."
              onChange={this.state.handleChange}
              value={this.state.genre || ''}
            />
          </div>
        </div>
        <div className="field">
          <div className="control">
            <input id="form-Input"
              className="input"
              name="title"
              placeholder="Title..."
              onChange={this.state.handleChange}
              value={this.state.title || ''}
            />
          </div>
        </div>

        <button className="buttonNew">Submit</button>
      </form>
    )
  }
}

export default Form
