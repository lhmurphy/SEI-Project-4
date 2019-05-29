import React from 'react'
import axios from 'axios'
import { Link } from 'react-router-dom'

import Card from './Card'

class Index extends React.Component {

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

  render() {
    console.log(this.state.books)
    if(!this.state) return null
    return (
      <main>
        <section className="section">
          <div className="container">
            <div className="columns is-multiline">
              {this.state.books.map(book =>
                <div key={book.id} className="column is-full-desktop is-full-tablet">
                  <Link to={`/books/${book.id}`}>
                    <Card {...book} />
                  </Link>
                </div>
              )}
            </div>
          </div>
        </section>
      </main>
    )
  }
}

export default Index
