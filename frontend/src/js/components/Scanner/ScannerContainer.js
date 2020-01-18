import React, {
    useRef,
    useState,
    useLayoutEffect
} from 'react'

/**
 * Wraps the scanner so it lays out like display: block;
 */
const ScannerContainer = props => {
    const ref = useRef(null)
    const [dimensions, setDimensions] = useState(null)

    useLayoutEffect(() => {
        console.log(ref.current)
        const rect = ref.current.getBoundingClientRect()

        setDimensions({width: rect.width, height: rect.height})
    }, [])

    return (
        <div className="ScannerContainer" ref={ref}>
            {(dimensions !== null) &&
                <Scanner
                    onDetected={props.onDetected}
                    width={dimensions.width}
                    height={dimensions.height}/>
            }
        </div>
    )
}

export default ScannerContainer

