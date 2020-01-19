import React from "react";
import Plot from "react-plotly.js";

const Graph = props => {
    const plot_props = {
        data: [
            {
                x: Object.keys(props.data),
                y: props.data.map(el => el.max)
            },
            {
                x: Object.keys(props.data),
                y: props.data.map(el => el.min)
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

export default Graph;
