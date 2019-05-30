import React from 'react'

const Card = ({ title, author, genre, jacket }) => {

  return (
    <div className="card is-horizontal columns">
      <figure className="image is-128x128px">
        <img src={jacket} alt={title} />
      </figure>
      <div className="card-content">
        <p className="card-header-title">{title}</p>
        <p>{author}</p>
        <p>{genre}</p>

      </div>
    </div>
  )
}

export default Card
