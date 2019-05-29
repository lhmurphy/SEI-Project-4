import React from 'react'

const Card = ({ title, author, genre, jacket }) => {

  return (
    <div className="card is-shady">
      <figure className="image is-64x64">
        <img src={jacket} alt={title} />
      </figure>
      <p>{title}</p>
      <p>{author}</p>
      <p>{genre}</p>
    </div>
  )
}

export default Card
