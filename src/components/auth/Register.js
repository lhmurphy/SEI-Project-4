import React from 'react'
import axios from 'axios'

import { Link } from 'react-router-dom'
import Auth from '../../lib/Auth'

class Register extends React.Component {

  constructor() {
    super()

    this.state = {
      data: {},
      error: {}
    }

    this.handleChange = this.handleChange.bind(this)
    this.handleSubmit = this.handleSubmit.bind(this)
  }

  handleChange({target: { name, value }}) {
    const data = {...this.state.data, [name]: value }
    const error = { ...this.state.error, [name]: '' }
    this.setState({ data, error })
  }

  handleSubmit(e) {
    e.preventDefault()
    axios
      .post('/api/register', this.state.data)
      .then(() => this.props.history.push('/login'))
      .catch((err) => this.setState({error: err.response.data.error}))
  }

  render() {
    return (
      <section className="section">
        <div className="container">
          <div className="columns is-centered">
            <div className="column is-half-desktop is-two-thirds-tablet">
              <p className="title is-4">Register</p>
              <hr />
              <form onSubmit={this.handleSubmit}>
                <div className="field">
                  <label className="label">Username</label>
                  <div className="control">
                    <input
                      className="input"
                      name="username"
                      placeholder="eg: book123"
                      onChange={this.handleChange}
                    />
                  </div>

                </div>
                <div className="field">
                  <label className="label">Email</label>
                  <div className="control">
                    <input
                      className="input"
                      name="email"
                      placeholder="eg: book@book.com"
                      onChange={this.handleChange}
                    />
                  </div>
                  {this.state.error.email && <div className="help is-danger">{this.state.error.email}</div>}
                </div>

                <div className="field">
                  <label className="label">Password</label>
                  <div className="control">
                    <input
                      className="input"
                      name="password"
                      type="password"
                      placeholder="eg: ••••••••"
                      onChange={this.handleChange}
                    />
                  </div>
                  {this.state.error.password && <div className="help is-danger">{this.state.error.password}</div>}
                </div>
                <div className="field">
                  <label className="label">Password Confirmation</label>
                  <div className="control">
                    <input
                      className="input"
                      name="password_confirmation"
                      type="password"
                      placeholder="eg: ••••••••"
                      onChange={this.handleChange}
                    />
                  </div>
                  {this.state.error.password_confirmation && <div className="help is-danger">{this.state.error.password_confirmation}</div>}
                </div>
                <button className="button is-danger">Submit</button>
              </form>

              <p>Already have an account? {!Auth.isAuthenticated() && <Link to="/login">login</Link>} here</p>

            </div>
          </div>
        </div>
      </section>
    )
  }
}

export default Register
