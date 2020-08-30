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

    //https://nwmdata.nohrsc.noaa.gov/latest/forecasts/medium_range/streamflow?station_id=6269188

    componentDidMount() {
      fetch("https://nwmdata.nohrsc.noaa.gov/latest/forecasts/medium_range/streamflow?station_id=6269188")
        .then(res => res.json()
        )
        .then(
          (result) => {
            console.log(result)
            this.setState({
              isLoaded: true,
              data: result[0].data
            }
            );
            console.log(this.state.data)
            console.log(this.state.isLoaded)
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
      //this.parseData()
      console.log(this.state.items)
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
              labels={({ datum }) => `${Math.round(datum.x, 2)}, ${Math.round(datum.y, 2)}`}
            />
          }
        >
          <VictoryLine
            interpolation="natural"
            style={{
              data: { stroke: "#c43a31" },
              parent: { border: "1px solid #ccc"}
            }}
            data={[
              { x: 1, y: 2 },
              { x: 2, y: 3 },
              { x: 3, y: 5 },
              { x: 4, y: 4 },
              { x: 5, y: 7 }
            ]}
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

     {/*
    parseData(riverData){
      let data =  this.state.riverData.data.map(buildInput)
    function buildInput(datum){
      //console.log(datum.value)
      //console.log(datum['forecast-time'])
      //console.log(Object.keys(datum))
      return({x:datum['forecast-time'],y:datum.value})
      }
    this.setState({ riverData: data })  
    }
  */}


