import React from 'react'

import { useSelector } from 'react-redux'
import { useLocation } from 'wouter'
import FullscreenCenter from '../Helpers/FullscreenCenter'

import './Results.css'
import { useAuthenticated } from '../../utils'

import CircularProgress from '@material-ui/core/CircularProgress'
import Container from '@material-ui/core/Container'
import Typography from '@material-ui/core/Typography'
import Chip from '@material-ui/core/Chip';

const EmissionsNumbers = props => {
    const formatNum = num => ((num * 100).toFixed(4))
    return (
        <div className="EmissionsNumbers">
            <div className="EmissionsNumbers__number EmissionsNumbers__number--min">
                <Typography variant="button">Minimum CO<sub>2</sub>:</Typography>
                <Typography variant="h1">{formatNum(props.results.min_total_emissions)} g</Typography>
                <Typography variant="overline">{formatNum(props.results.min_emissions_per_kg)} grams per unit kilogram</Typography>
            </div>
            <div className="EmissionsNumbers__number EmissionsNumbers__number--max">
                <Typography variant="button">Maximum CO<sub>2</sub>:</Typography>
                <Typography variant="h1">{formatNum(props.results.max_total_emissions)} g</Typography>
                <Typography variant="overline">{formatNum(props.results.max_emissions_per_kg)} grams per unit kilogram</Typography>
            </div>
        </div>
    )
}

const ResultOverview = props => {
    console.log(props.results)

    const ingredients = props.results.ingredients.map( ing => (
        <Chip key={ing} label={ing}/>
    ))

    return (
        <div className="ResultOverview">
            <Typography component="h2" variant="h2">{props.results.name}</Typography>
            <Typography variant="overline">Barcode: {props.results.barcode}, Net Wt. {props.results.weight_in_kg} Kg</Typography>

            <EmissionsNumbers results={props.results}/>


            <div className="ResultOverview__ingredients">
                {ingredients}
            </div>
            { props.results.palm_oil &&
                <Typography color="error" variant="overline"> This food contains palm oil! </Typography> 
            }
        </div>
    )
}

const ShowLookupResults = props => {
    const pending = useSelector( state => state.scan.get('responsePending') )
    const results = useSelector( state => state.scan.get('response') )

    return (
        <FullscreenCenter>

            {pending ?
                    <CircularProgress/> :
                    <Container>
                        <ResultOverview results={results.toJS()}/>
                    </Container>
            }

        </FullscreenCenter>
    )
}

export default ShowLookupResults
