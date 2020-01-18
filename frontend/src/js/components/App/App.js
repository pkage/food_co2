import React, {
    useState
} from 'react'
import ScannerContainer from '../Scanner/ScannerContainer'
import Sidebar from '../Sidebar/Sidebar'

const App = () => {
    const [results, setResults] = useState([])

    const addResult = res => setResults([res, ...results])

    
    return (
        //        <ScannerContainer onDetected={res => console.log(res)}/>

        <Sidebar/>
    )
}

export default App

