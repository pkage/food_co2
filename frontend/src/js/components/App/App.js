import React, {
    useState
} from 'react'

import { Switch, Route, Link } from 'wouter'

import ScannerContainer from '../Scanner/ScannerContainer'
import Sidebar from '../Sidebar/Sidebar'
import Splash from '../Splash/Splash'
import Login from '../Login/Login'
import ScanPage from '../Scanner/ScanPage'
import Dashboard from '../Dashboard/Dashboard'

const App = () => {
    const [results, setResults] = useState([])

    const addResult = res => setResults([res, ...results])

    
    // <ScannerContainer onDetected={res => console.log(res)}/>
    return (
        <>
            <Sidebar>
                <Link href="/">splash</Link>
                <br/>
                <Link href="/login">login</Link>
                <br/>
                <Link href="/scan">scan</Link>
                <br/>
                <Link href="/dashboard">dashboard</Link>
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
            <Route path="/dashboard">
                <Dashboard/>
            </Route>
        </>
    )
}

export default App

