import React from 'react';
import {VictoryChart,VictoryLine,VictoryTheme,VictoryVoronoiContainer } from 'victory';
import {
  Row,
  Col,
  Card,
  CardBody,
  CardTitle,
  Table,
  Button
    } from "reactstrap";
import riverInfo from '../assets/riverInfo';

const featureIDs = ['6478281','6269342','2040709','2040853']




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
      fetch(`https://nwmdata.nohrsc.noaa.gov/latest/forecasts/medium_range/streamflow?station_id=${this.props.featureID}`)
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
    componentDidUpdate() {
      fetch(`https://nwmdata.nohrsc.noaa.gov/latest/forecasts/medium_range/streamflow?station_id=${this.props.featureID}`)
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
      if (!this.state.riverData) {
        return <div />
      }
      if (this.props.featureID){
        let graphVals = []
        console.log(graphVals)
        // THIS ISN'T WORKING RIGHT (GRAPH VALUES ARE NOTE UPDATING)
        //Divide by 8 to achieve days in future for now (3 hours increments)
        this.state.riverData.map((datum,index) => graphVals.push({x:index/8,y:datum.value}))
        //console.log(this.state.riverData[0])
        //NEED TO RETURN A GOOGLE MAPS LINK INSTEAD
        //console.log(riverInfo.filter(river => river.featureID==this.props.featureID)[0]['Put In'].split(',')[0])
        return (
          <Col xs={{size:8,offset:2}}>
          <Card className="m-2">
          <CardTitle className= "mt-5 mb-0">
            <h2>{riverInfo.filter(river => river.featureID==this.props.featureID)[0].RiverName}</h2>
            <strong>{riverInfo.filter(river => river.featureID==this.props.featureID)[0].RunName}</strong>
          </CardTitle>
          <CardBody>
          <Row>
          <Col xs="8">
          {console.log(graphVals)}
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
          </Col>
          </Row>
          <Table responsive>
            <thead>
              <tr>
                <th>Class</th>
                <th>Put In</th>
                <th>Take Out</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>{riverInfo.filter(river => river.featureID==this.props.featureID)[0].Class}</td>
                <td>{riverInfo.filter(river => river.featureID==this.props.featureID)[0]['Put In']}</td>
                <td>{riverInfo.filter(river => river.featureID==this.props.featureID)[0]['Take Out']}</td>
              </tr>
            </tbody>
          </Table>
          </CardBody>
          </Card>
          </Col>
        )
      }else{
        return(<div/>)
      }

  }
  }


function RiverCard({selection}){
  if (selection){
  console.log(selection)
  return (
    <React.Fragment>
        <Row className="position-sticky">
            <BuildGraph featureID={selection} index={0}/>
        </Row>
</React.Fragment>
  )
  }
  else{
    return <div/>
  }
}

 export default RiverCard;

