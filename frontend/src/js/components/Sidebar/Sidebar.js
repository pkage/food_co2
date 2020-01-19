import React, {
    useState   
} from 'react'

import {
    Link
} from 'wouter'

import MenuIcon from '@material-ui/icons/Menu'
import classNames from 'class-names'
import './Sidebar.css'

const Sidebar = props => {
    const [active, setActive] = useState(false)

    const baseName = classNames('Sidebar', {'Sidebar--active': active})

    return (
        <div className={baseName}>
            <div className="Sidebar__menucontainer" >
                <div className="Sidebar__menu" onClick={() => setActive(false)}>
                    {props.children}
                </div>
                <div className="Sidebar__button" onClick={() => setActive(!active)}>
                    <MenuIcon/>
                </div>
                <div className="Sidebar__closearea" onClick={() => setActive(false)}></div>
            </div>
        </div>
    )
}

export default Sidebar

