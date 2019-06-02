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





@router.route('/entries', methods=['POST'])
@db_session
@secure_route
def create():
    entry_schema = EntrySchema()

    try:
        data = entry_schema.load(request.get_json())
        entry = Entry(**data, created_by=g.current_user)
        db.commit()
    except ValidationError as err:
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    return entry_schema.dumps(entry), 201








@router.route('/pools', methods=['POST'])
@db_session
@secure_route
def create():
    # This will deserialize the JSON from insomnia
    schema = PoolSchema()

    try:
        # attempt to convert the JSON into a dict
        data = schema.load(request.get_json())
        # Use that to create a pool object
        data['user'] = g.current_user
        pool = Pool(**data)
        # Store it in the database
        db.commit()
    except ValidationError as err:
        # if the validation fails, send back a 422 response
        return jsonify({'message': 'Validation failed', 'errors': err.messages}), 422

    # otherwise, send back the pool data as JSON
    return schema.dumps(pool), 201
