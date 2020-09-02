import React from 'react';
import riverInfo from '../assets/riverInfo';
import BootstrapTable from 'react-bootstrap-table-next';
import {
Row,
Col,
Button,
      } from "reactstrap";
import { timers } from 'jquery';

class RiverTable extends React.Component {
    constructor(props) {
      super(props);
      this.state = {
        selectedRiver:'',
        error: null,
        isLoaded: false,
        };
      }
      render() {
          const columns = [{
              dataField: 'RiverName',
              text: 'River Name',
              sort: true,
          }, {
              dataField: 'RunName',
              text: 'River Section'
          }, {
              dataField: 'Class',
              text: 'Difficulty',
              sort: true,
          }];
          const rowEvents = {
            onClick: (e, row, rowIndex) => {
              this.props.onRiverSelect(row.featureID)
            }
          };
        return (
            <React.Fragment>
            <Row>
            <Col className="m-5">
                <BootstrapTable keyField='id' data={riverInfo.filter(river => river.State=='CO')} columns={ columns } rowEvents={ rowEvents }  selectedRiver = {this.props.isLoaded}/>
            </Col>
            </Row>
            </React.Fragment>
        )
      }
    }

export default RiverTable;
