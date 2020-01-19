import React from "react";

import Container from "@material-ui/core/Container";
import Typography from "@material-ui/core/Typography";

import Graph from "./Graph";
import "./Dashboard.css";

import { useLocation } from "wouter";
import { useSelector } from "react-redux";
import { useAuthenticated } from "../../utils";

const Entry = props => {
    return (
        <>
            <h2>{props.name}</h2>
            <p>weight: {props.weight}</p>
            <ul>
                <li>max CO2/kg: {props.max_emissions_kg}</li>
                <li>min CO2/kg: {props.min_emissions_kg}</li>
                <li>max CO2 in this serving: {props.max_total_emissions}</li>
                <li>min CO2 in this serving: {props.min_total_emissions}</li>
            </ul>
            <small style={{ color: props.palm_oil ? "red" : "black" }}>This product {props.palm_oil ? "contains" : "does not contain"} palm oil</small>
        </>
    );
};

const Dashboard = props => {
    const dashboard = useSelector(state => state.scan.get("dashboard"));
    useAuthenticated()


    dashboard
        .get("entries")
        .toJS()
        .map((entry, i) => <Entry key={i} {...entry}/>)

    return (
        <Container className="Dashboard">
            <Typography variant="h2">Overview</Typography>
            <div className="Dashboard__graph">
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
            </div>
            <div className="Dashboard__events">
                <div className="Dashboard__side"></div>
                <div className="Dashboard__feed">
                    {dashboard.entries.map(el => {
                        <Entry {...el} />;
                    })}
                </div>
            </div>
        </Container>
    );
};

export default Dashboard;
