import React, {
    useState
} from 'react'

import { Switch, Route, Link } from 'wouter'

import ScannerContainer from '../Scanner/ScannerContainer'
import Sidebar from '../Sidebar/Sidebar'
import LinkButton from '../Sidebar/LinkButton'
import Splash from '../Splash/Splash'
import Login from '../Login/Login'
import ScanPage from '../Scanner/ScanPage'
import Dashboard from '../Dashboard/Dashboard'
import ShowLookupResults from '../Results/Results'


const App = () => {
    const [results, setResults] = useState([])

    const addResult = res => setResults([res, ...results])

    
    // <ScannerContainer onDetected={res => console.log(res)}/>
    return (
        <>
            <Sidebar>
                <LinkButton href="/">splash</LinkButton>
                <LinkButton href="/login">login</LinkButton>
                <LinkButton href="/scan">scan</LinkButton>
                <LinkButton href="/dashboard">dashboard</LinkButton>
            </Sidebar>
            <Route path="/">
                <Splash/>
            </Route>
            <Route path="/login">
                <Login/>
            </Route>
            <Route path="/scan">
                <ScanPage/>
            </Route>
            <Route path="/results">
                <ShowLookupResults/>
            </Route>
            <Route path="/dashboard">
                <Dashboard/>
            </Route>
        </>
    )
}

export default App

