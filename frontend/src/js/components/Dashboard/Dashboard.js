import Plot from "react-plotly.js";
import React from "react";
// import Graph from "../Graph/Graph";
const Graph = props => {
    const plot_props = {
        data: [
            {
                type: "bar",
                x: Object.keys(props.data),
                y: Object.values(props.data).map(el => el.max),
                name: "Maximum Co2 emissions",
                marker: {
                    color: "red"
                }
            },
            {
                type: "bar",
                x: Object.keys(props.data),
                y: Object.values(props.data).map(el => el.min),
                name: "Minimum Co2 emissions",
                marker: {
                    color: "green"
                }
            }
        ],
        layout: {
            width: 640,
            height: 480,
            title: "A Fancy Plot",
            barmode: "overlay"
        }
    };
    return <Plot {...plot_props} />;
};

const Dashboard = props => {
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
};

export default Dashboard;
