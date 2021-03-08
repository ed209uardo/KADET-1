import Accordion from 'react-bootstrap/Accordion';
import Card from 'react-bootstrap/Card'

import React, { Component } from "react";
import axios from "axios";

  /*
      Throw axios and constructor to declare state
        for the render below function to output the data from backend/residentrequests/api/
        Maybe terrence or draco can do it, should be fairly simple. (otherwise i can do it but not till next wednesday)
    */

class Requests extends Component {
    
    constructor(props) {
        super(props);
        this.state = {
          requestList: [],
          
        };
    }
    
    componentDidMount() {
        this.refreshList();
    }
    
    refreshList = () => {
        axios
          .get("/requests/api/")
          .then((res) => this.setState({ criteriaList: res.data }))
          .catch((err) => console.log(err));
    };

    renderRequests = () => {
        const newItems = this.state.requestList;

        return newItems.map((item) => (
          <li
            key={item.id}
            className="list-group-item d-flex justify-content-between align-items-center"
          >
            <span
              className={`mr-2`}
            >
              {item.RotationType}
            </span>

          </li>
        ));
    };

    render() {
    return (
        <main className="container">
        <h3 className="text-center">Schedule Requests</h3>
        <div className="row">
          <div className="col-md-8 col-sm-10 mx-auto p-0">
            <div className="card p-3">
        <Accordion defaultActiveKey="">

        <Card>
        
        <Accordion.Toggle as={Card.Header} eventKey="0">
        '"First Name" + "Lastname"''
        </Accordion.Toggle>
        <Accordion.Collapse eventKey="0">
        <Card.Body>
        <p>Email Address:</p>
        <p>Request 1:</p>
        <p>Request 2:</p>
        <p>Request 3:</p>
        </Card.Body>
        </Accordion.Collapse>
        
        </Card>

        
        <Card>
        <Accordion.Toggle as={Card.Header} eventKey="1">
        Click me!
        </Accordion.Toggle>
        <Accordion.Collapse eventKey="1">
        <Card.Body>Hello! I'm another body</Card.Body>
        </Accordion.Collapse>
        </Card>
        </Accordion>
        </div>
        </div>
        </div>
        </main>
        );
    };
}
export default Requests;

    
//export default ListRequests;