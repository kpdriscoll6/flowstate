import React from "react";
import RiverCard from "./RiverCard";
import {Container} from "reactstrap";
import RiverTable from "./RiverTable";


class Home extends React.Component {
    constructor(props) {
        super(props);
        this.onRiverSelect = this.onRiverSelect.bind(this);    
    this.state = {
        selection:''
    }
}
    onRiverSelect(selection){
        this.setState({ selection: selection })
        //console.log(this.state.selectedRiver);

    }
    render() {
    return (
        <React.Fragment>
            <RiverCard selection = {this.state.selection}/>
            <Container fluid>
                <RiverTable onRiverSelect={this.onRiverSelect}/>
            </Container>
        </React.Fragment>
    )
}
}


export default Home;