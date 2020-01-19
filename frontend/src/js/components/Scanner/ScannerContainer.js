import React, {
    useRef,
    useState,
    useLayoutEffect
} from 'react'

import './ScannerContainer.css'
import Scanner from './Scanner'

/**
 * Wraps the scanner so it lays out like display: block;
 */
const ScannerContainer = props => {
    const ref = useRef(null)
    const [dimensions, setDimensions] = useState(null)

    useLayoutEffect(() => {
        console.log(ref.current)
        setTimeout(() => {
            const rect = ref.current.getBoundingClientRect()
            console.log(rect)

            setDimensions({width: rect.width, height: rect.height})
        }, 150)
    }, [])

    return (
        <div className="ScannerContainer" ref={ref}>
            {(dimensions !== null && dimensions.height !== 0) &&
                <Scanner
                    onDetected={props.onDetected}
                    width={dimensions.width}
                    height={dimensions.height}/>
            }
        </div>
    )
}

export default ScannerContainer

