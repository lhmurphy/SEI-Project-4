import React from 'react'
import ReactDOM from 'react-dom'

import { HashRouter, Route, Switch } from 'react-router-dom'

import 'bulma'
import './style.scss'

import Show from './components/books/Show'
import New from './components/books/New'
import Index from './components/books/Index'
import Navbar from './components/common/Navbar'
import Home from './components/common/Home'
import Register from './components/auth/Register'
import Login from './components/auth/Login'

class App extends React.Component {
  render() {
    return (
      <HashRouter>
        <Navbar />
        <main>
          <Switch>
            <Route path="/books/new" component={New} />
            <Route path="/books/:id" component={Show} />
            <Route path="/books" component={Index} />
            <Route path="/register" component={Register} />
            <Route path="/login" component={Login} />
            <Route exact path="/" component={Home} />
          </Switch>
        </main>
      </HashRouter>
    )
  }
}

ReactDOM.render(
  <App />,
  document.getElementById('root')
)
