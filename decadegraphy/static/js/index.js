import { BrowserRouter as Router, Route } from 'react-router-dom'
import React from 'react'
import ReactDOM from 'react-dom'
import createBrowserHistory from 'history/createBrowserHistory'
import * as Campaign from './Campaign'

import '../css/main.scss'

// Global JSONP handle
window.jsonp = new Proxy({}, {
  get: (self, key) => {
    return (data) => { window[key] = data }
  }
})

const history = createBrowserHistory()

if (document.getElementById('app')) {
  ReactDOM.render((
    <Router>
      <div>
        <Route exact path="/campaigns/signup(/)?(\d+)?" component={Campaign.SignUp} />
        <Route exact path="/campaigns/signup/:message" component={Campaign.Message} />
      </div>
    </Router>
  ), document.getElementById('app'))
}
