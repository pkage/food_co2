import React, {
    useState
} from 'react'

import { Switch, Route, Link } from 'wouter'

import ScannerContainer from '../Scanner/ScannerContainer'
import Sidebar from '../Sidebar/Sidebar'
import Splash from '../Splash/Splash'
import Login from '../Login/Login'
import Scanner from '../Scanner/Scanner'

const App = () => {
    const [results, setResults] = useState([])

    const addResult = res => setResults([res, ...results])

    
    // <ScannerContainer onDetected={res => console.log(res)}/>
    return (
        <>
            <Sidebar>
                <Link href="/">splash</Link>
                <Link href="/login">login</Link>
            </Sidebar>
            <Route path="/">
                <Splash/>
            </Route>
            <Route path="/login">
                <Login/>
            </Route>
            <Route path="/scan">
                <Scanner width="640" height="480" onDetected={res => console.log(res)}/>
            </Route>
        </>
    )
}

export default App

