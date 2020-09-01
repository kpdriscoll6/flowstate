import React from "react";
import RiverCard from "./RiverCard";
import {Container} from "reactstrap";

function Home(props) {
    return (
        <React.Fragment>
            <Container fluid>
                <RiverCard/>
            </Container>
        </React.Fragment>
    )
}


export default Home;