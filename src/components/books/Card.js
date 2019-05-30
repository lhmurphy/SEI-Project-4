import React from 'react'

const Card = ({ title, author, genre, jacket, isbn }) => {

  return (
    <div className="card is-horizontal columns" id="index">
      <figure className="image is-128x128px">
        <img src={jacket} alt={title} />
      </figure>
      <div className="card-content">
        <p className="title is-4">{title}</p>
        <p>Author: {author}</p>
        <p>Genre: {genre}</p>
        <p>ISBN: {isbn}</p>

      </div>
    </div>
  )
}

export default Card
