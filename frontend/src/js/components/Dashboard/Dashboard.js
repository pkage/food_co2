import React from 'react'

import Container from '@material-ui/core/Container'
import Typography from '@material-ui/core/Typography'

import Graph from './Graph'
import './Dashboard.css'


const Dashboard = props => {
    /*
    return (
        <Graph
            data={{
                "2020-01-01": { min: 1, max: 2 },
                "2020-01-02": { min: 3, max: 5 },
                "2020-01-03": { min: 2, max: 4 },
                "2020-01-04": { min: 1, max: 3 },
                "2020-01-05": { min: 2, max: 6 },
                "2020-01-06": { min: 2, max: 2.5 }
            }}
        />
    );
    */
    return (
        <Container className="Dashboard">
            <Typography variant="h2">Overview</Typography>
            <div className="Dashboard__graph">
            </div>
            <div className="Dashboard__events">
                <div className="Dashboard__side"></div>
                <div className="Dashboard__feed"></div>
            </div>
        </Container>
    )
};

export default Dashboard;
