import React from 'react';
import {VictoryChart,VictoryLine,VictoryTheme,VictoryVoronoiContainer } from 'victory';
import {
  Row,
  Col,
  Card,
  CardBody,
  CardTitle,
  Container,
  CardText,
  Table,
    } from "reactstrap";
import riverInfo from '../assets/riverInfo';

const featureID = '6478281'
//riverInfo.map(river =>console.log(river.RiverName))
console.log(riverInfo.filter(river => river.featureID==featureID))



class BuildGraph extends React.Component {
  constructor(props) {
    super(props);
    this.state = {
      riverData:[],
      error: null,
      isLoaded: false,
      };
    }
    componentDidMount() {
      fetch(`https://nwmdata.nohrsc.noaa.gov/latest/forecasts/medium_range/streamflow?station_id=${featureID}`)
        .then(res => res.json()
        )
        .then(
          (result) => {
            //console.log(result)
            this.setState({
              isLoaded: true,
              riverData: result[0].data
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
      this.state.riverData.map((datum,index) => graphVals.push({x:index/8,y:datum.value}))
      //console.log(graphVals)
      return (
        <Col className="md-6">
        <Card className="m-5">
        <CardTitle className= "mt-5 mb-0">
          <h2>{riverInfo.filter(river => river.featureID==featureID)[0].RiverName}</h2>
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
        <Table>
          <thead>
            <tr>
              <th>River Name</th>
              <th>Run Name</th>
              <th>Class</th>
              <th>Put In</th>
              <th>Take Out</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>{riverInfo.filter(river => river.featureID==featureID)[0].RiverName}</td>
              <td>{riverInfo.filter(river => river.featureID==featureID)[0].RunName}</td>
              <td>{riverInfo.filter(river => river.featureID==featureID)[0].Class}</td>
              <td>{riverInfo.filter(river => river.featureID==featureID)[0]['Put In']}</td>
              <td>{riverInfo.filter(river => river.featureID==featureID)[0]['Take Out']}</td>
            </tr>
          </tbody>
        </Table>
        </CardBody>
        </Card>
        </Col>
      )
    }
  }


function RiverCard(props){
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


 export default RiverCard;