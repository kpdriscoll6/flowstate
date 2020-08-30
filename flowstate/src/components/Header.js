import React, { Component } from "react";
import {
  Navbar,
  Nav,
  NavbarToggler,
  Collapse,
  NavItem,
  Jumbotron,
} from "reactstrap";
import { NavLink, Link } from "react-router-dom";
import logo from '../../src/assets/logo.png';

class Header extends Component {
  constructor(props) {
    super(props);

    this.toggleNav = this.toggleNav.bind(this);
    this.state = {
      isNavOpen: false,
    };
  }
  toggleNav() {
    this.setState({
      isNavOpen: !this.state.isNavOpen,
    });
  }
  render() {
    return (
      <React.Fragment>
        <Jumbotron fluid>
        </Jumbotron>
        <Navbar light sticky="top" expand="sm">
          <div className="container">
          <img className="mr-auto ml-4" src={logo} alt="logo"/>
            <NavbarToggler onClick={this.toggleNav} />
            <Collapse isOpen={this.state.isNavOpen} navbar>
              <Nav navbar className="ml-auto p-2" >
                <NavItem >
                  <NavLink className="nav-link" to="/home">
                    <h5>Home</h5>
                  </NavLink>
                </NavItem>
                <NavItem>
                  <NavLink className="nav-link" to="/aboutus">
                  <h5>About</h5>
                  </NavLink>
                </NavItem>
                <NavItem>
                  <NavLink className="nav-link" to="/contactus">
                  <h5>Contact</h5>
                  </NavLink>
                </NavItem>
              </Nav>
            </Collapse>
          </div>
        </Navbar>
      </React.Fragment>
    );
  }
}

export default Header;
