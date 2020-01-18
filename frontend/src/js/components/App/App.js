import React, {
    useState
} from 'react'
import ScannerContainer from '../Scanner/ScannerContainer'

const App = () => {
    const [results, setResults] = useState([])

    const addResult = res => setResults([res, ...results])

    
    return (
        //        <Scanner onDetected={res => console.log(res)}/>
        <ScannerContainer/>
    )
}

export default App

