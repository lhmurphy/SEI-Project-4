class Flash {
  static setMessage(type, content) {
    this.messages = this.messages || {}
    this.messages[type] = content
  }

  static getMessages() {
    return this.messages
  }

  static clearMessages() {
    this.messages = null
  }

}

export default Flash
