import Plot from "react-plotly.js";
import React from "react";
// import Graph from "../Graph/Graph";
const Graph = props => {
    let data = [];
    if (props.data && Object.keys(props.data).length > 0) {
        data = [
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
        ];
    }
    const plot_props = {
        data: data,
        layout: {
            autosize: true,
            responsive: true,
            barmode: "overlay",
            margin: { b: 25, t: 25 }
        }
    };
    const styles = {
        height: "100%",
        width: "100%"
    };
    return <Plot {...plot_props} responsive={true} style={styles} />;
};

export default Graph;
