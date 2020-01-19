import React from 'react'
import { Link } from 'wouter'
import Typography from '@material-ui/core/Typography'
import './LinkButton.css'

const LinkButton = props => (
    <span className="LinkButton">
        <Link href={props.href}>
            <Typography variant="button" >{props.children}</Typography>
        </Link>
    </span>
)

export default LinkButton
