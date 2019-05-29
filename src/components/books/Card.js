import React from 'react'

const Card = ({ title, author, genre, jacket }) => {

  return (
    <div className="card is-shady">
      <p>{jacket}</p>
      <p>{title}</p>
      <p>{author}</p>
      <p>{genre}</p>
    </div>
  )
}

export default Card
