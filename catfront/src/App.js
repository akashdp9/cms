import React, { Component } from 'react';
import './App.css';
import {
  BrowserRouter as Router,
  Switch,
  Route,
  Link
} from "react-router-dom";
import {Brand } from './components';
// import Categories from './components/categories';
class App extends Component {
  render() {
    return (
      <div className="App">
         <Router>
          <div>
            <nav>
              <div className='Link'>
                <Link to="/home">Home</Link>
                <Link to="/product">Product</Link>
                <Link to="/brand">Brand</Link>
                <Link to="/categories">Categories</Link>
              </div>
            </nav>
            <Switch>
              {/* <Route path="/home">
                <Home />
              </Route>
              <Route path="/product">
                <Product />
              </Route> */}
              <Route path="/brand">
                <Brand />
              </Route>
              {/* <Route path="/categories">
                <Category />
                </Route> */}
            </Switch>
          </div>
    </Router>
      </div>
    );
  }
}
export default App;