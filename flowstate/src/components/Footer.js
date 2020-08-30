import React, { Component } from "react";
import { Link } from "react-router-dom";
import {
Button
} from "reactstrap";

class Footer extends Component {
  render() {
    return (
      <footer className="footer">
        <div className="container">
          <div className="row">
            <div className="col-6 text-center">
              <h5>FlowState</h5>
              <a
                className="btn btn-social-icon btn-instagram"
                href="http://instagram.com/"
              >
                <i className="fa fa-instagram" />
              </a>{" "}
              <a
                className="btn btn-social-icon btn-facebook"
                href="http://www.facebook.com/"
              >
                <i className="fa fa-facebook" />
              </a>{" "}
              <a
                className="btn btn-social-icon btn-github"
                href="http://github.com/"
              >
                <i className="fa fa-github" />
              </a>{" "}
            </div>

            <div className="col text-center">
              <p>
                <i className="fa fa-envelope-o"></i> Stay up to date on the latest from FlowState
              </p>
              <div className="col text-center">
                <input className="m-2 p-2 rounded"
                  type="email"
                  id="footerEmail"
                  name="footerEmail"
                  placeholder="Email"
                />
                <Button className="m-2 p-2 footer-button">
                  Sign Up
                </Button>
              </div>
            </div>
          </div>
        </div>
      </footer>
    );
  }
}

export default Footer;
