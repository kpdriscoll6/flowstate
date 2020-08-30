import React, { Component } from "react";
import Header from "./Header";
import { Switch, Route, Redirect, withRouter } from "react-router-dom";
import Contact from "./Contact";
import About from "./About";
import Home from "./Home";
import Footer from "./Footer";

class Main extends Component {
  render() {
    const HomePage = () => {
      return (
        <Home />
      );
    };
    return (
      <div>
        <Header />
        <Switch>
          <Route path="/home" component={HomePage} />
          <Route exact path="/contactus" render={() => <Contact />} />
          <Route exact path="/aboutus" render={() => <About />} />
          <Redirect to="/home" />
        </Switch>
        <Footer />
      </div>
    );
  }
}

export default Main;