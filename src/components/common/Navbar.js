import React from 'react'
import { Link, withRouter } from 'react-router-dom'

class Navbar extends React.Component {

  constructor(props) {
    super(props)

    this.state = { active: false }

    this.logout = this.logout.bind(this)
    this.toggleActive = this.toggleActive.bind(this)
  }

  logout() {
    this.props.history.push('/')
  }

  toggleActive() {
    this.setState({ active: !this.state.active })
  }

  componentDidUpdate(prevProps) {
    if(prevProps.location.pathname !== this.props.location.pathname) {
      this.setState({ active: false })
    }

  }

  render() {
    return (
      <nav className="navbar is-dark">
        <div className="container">

          <div className="navbar-brand">
            {/* Branding and burger menu */}
            <Link to="/" className="navbar-item display is-size-4">Wanderlist</Link>

            <a
              role="button"
              className={`navbar-burger${this.state.active ? ' is-active' : ''}`}
              onClick={this.toggleActive}
            >
              <span aria-hidden="true"></span>
              <span aria-hidden="true"></span>
              <span aria-hidden="true"></span>
            </a>
          </div>

          <div className="navbar-start">
            <Link to="/books" className="navbar-item">Books</Link>
          </div>

          <div className={`navbar-menu${this.state.active ? ' is-active' : ''}`}>

            <div className="navbar-end">
              <Link to="/register" className="navbar-item">Register</Link>
              <Link to="/login" className="navbar-item">Login</Link>
              <a className="navbar-item" onClick={this.logout}>Logout</a>
            </div>
          </div>
        </div>
      </nav>
    )
  }
}

// `withRouter` gives the Navbar `history` via props
export default withRouter(Navbar)
