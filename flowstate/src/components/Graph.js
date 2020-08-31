import React from 'react';
import {VictoryChart,VictoryLine,VictoryTheme,VictoryVoronoiContainer } from 'victory';
import {
  Row,
  Col,
  Card,
  CardBody,
  CardTitle,
  Container
    } from "reactstrap";

class BuildGraph extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      riverData:[],
      error: null,
      isLoaded: false,
      data: [1,2,3,4],
      };
    }

    componentDidMount() {
      fetch("https://nwmdata.nohrsc.noaa.gov/latest/forecasts/medium_range/streamflow?station_id=6269188")
        .then(res => res.json()
        )
        .then(
          (result) => {
            //console.log(result)
            this.setState({
              isLoaded: true,
              data: result[0].data
            }
            );
            //console.log(this.state.data)
          },
          (error) => {
            this.setState({
              isLoaded: true,
              error
            });
          }
        )
    }
    render() {
      const graphVals = []
      //Divide by 8 to achieve days in future for now (3 hours increments)
      this.state.data.map((datum,index) => graphVals.push({x:index/8,y:datum.value}))
      console.log(graphVals)
      return (
        <Col className="md-6">
        <Card className="m-5">
        <CardTitle className= "mt-5 mb-0">
          <h5>Chattooga</h5>
        </CardTitle>
        <CardBody>
        <VictoryChart
          theme={VictoryTheme.material}
          containerComponent={
            <VictoryVoronoiContainer
            //NO LABELS FOR NOW
              //labels={({ datum }) => `${Math.round(datum.x, 2)}, ${Math.round(datum.y, 2)}`}
            />
          }
        >
          <VictoryLine
            interpolation="natural"
            style={{
              data: { stroke: "#c43a31" },
              parent: { border: "1px solid #ccc"}
            }}
            data={graphVals}
          />
        </VictoryChart>
        </CardBody>
        </Card>
        </Col>
      )
    }
  }


function Graph(props){
  return (
    <React.Fragment>
    <Container>
        <Row>
            <BuildGraph/>
        </Row>
    </Container>
</React.Fragment>
  )
}


 export default Graph;