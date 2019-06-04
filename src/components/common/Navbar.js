import React from 'react'
import { Link, withRouter } from 'react-router-dom'
import Auth from '../../lib/Auth'

class Navbar extends React.Component {

  constructor(props) {
    super(props)

    this.state = {
      active: false
    }

    this.logout = this.logout.bind(this)
    this.toggleActive = this.toggleActive.bind(this)
  }

  logout() {
    Auth.removeToken()
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
      <div className='nav'>
        <nav className="navbar is-danger">
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
              {Auth.isAuthenticated() && <Link to="/books" className="navbar-item">Books</Link>}
            </div>

            <div className={`navbar-menu${this.state.active ? ' is-active' : ''}`}>

              <div className="navbar-end">
                {Auth.isAuthenticated() && <a className="navbar-item" onClick={this.logout}>Logout</a>}
              </div>
            </div>
          </div>
        </nav>
      </div>
    )
  }
}

// `withRouter` gives the Navbar `history` via props
export default withRouter(Navbar)
