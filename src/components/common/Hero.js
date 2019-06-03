import React from 'react'
import quotes from './quotes'

class Navbar extends React.Component {

  constructor(props) {
    super(props)

    this.state = {
      currentQuote: 0,
      quotes: quotes
    }
  }

  // componentDidMount() {
  //   setInterval(() => {
  //     let currentQuote = this.state.currentQuote + 1
  //     currentQuote === this.state.quotes.length ? currentQuote = 0:null
  //     this.setState({ currentQuote })
  //   }, 4000)
  // }

  render() {
    console.log(this.state.quotes)
    return (
      <section className="section" id="quote">
        <div className="quotes" style={{
          currentQuote: `<h1>${quotes[this.state.currentQuote]}</h1>`
        }}>
        </div>
      </section>
    )
  }
}

export default Navbar
