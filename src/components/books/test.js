import React from 'react'

import Select from 'react-select'
import defaultAreasOfLondon from '../../lib/areasOfLondon'
const areasOfLondon = [
  { name: 'areaOfLondon', value: 'All', label: 'All' },
  ...defaultAreasOfLondon
]


class LocationIndex extends React.Component {

  constructor(props){
    super(props)

    this.state = {
      activeLocation: null,
      area: 'All'
    }

    this.handleChange = this.handleChange.bind(this)
  }

  handleChange(inputValue) {
    this.setState({ area: inputValue.value })
  }

  // Provides and A-Z sort to the location data==============
  sortedLocations() {
    return this.props.data.sort((a, b) => {
      if (a.name === b.name) return 0
      return a.name < b.name ? -1 : 1
    })
  }

  //Filters the sorted locations on dropdown select==========
  filteredLocations() {
    const locations = this.sortedLocations()
    if (this.state.area === 'All') return this.props.data
    return locations.filter(location => {
      return location.areaOfLondon === this.state.area
    })
  }

  render() {

}


export default LocationIndex


// Map over comments
// {comments.map(comment => {
//    return(
//      <div key={comment._id}>
//        <p><strong>{comment.name}</strong></p>
//        <StarRatings width={comment.rating} />
//        <p className="comment-body">{comment.body}</p>
//        <hr />
//      </div>
//    )
//   })}



{comments.map(comment =>
                <article key={comment.id} className="media">
                  <figure className="media-left">
                    <p className="image is-64x64">
                      <img src={comment.user.image} />
                    </p>
                  </figure>
                  <div className="media-content">
                    <div className="content">
                      <p className="commentText">
                        <strong>{comment.user.username}</strong>  <small>{comment.created_at.substring(0, comment.created_at.length - 8)}</small>
                        <br />
                        {comment.content}
                      </p>
                    </div>
                  </div>
                </article>}
