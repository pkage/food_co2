import React from 'react';
import './Scanner.css'

class Scanner extends React.Component {
    constructor(props) {
        super(props)
        this.props = props
        console.log(props)

        this.cref = React.createRef()
    }

    render() {
        return (
            <div className="Scanner__container">
                <div id="interactive" className="viewport"/>
                <canvas
                    className="ScannerCanvas__canvas"
                    width={this.props.width}
                    height={this.props.height}
                    ref={this.cref}/>
            </div>
        );
    }

    componentDidMount() {
        Quagga.init({
            inputStream: {
                type : "LiveStream",
                constraints: {
                    width: this.props.width,
                    height: this.props.height,
                    facing: "environment" // or user
                }
            },
            locator: {
                patchSize: "medium",
                halfSample: true
            },
            numOfWorkers: 2,
            decoder: {
                readers : [ "code_128_reader", "ean_reader", "ean_8_reader", "upc_reader"]
            },
            locate: true
        }, function(err) {
            if (err) {
                return console.log(err);
            }
            Quagga.start();
        });
        Quagga.onDetected(this._onDetected.bind(this));
    }

    componentWillUnmount() {
        Quagga.offDetected(this._onDetected);
    }

    _onDetected(result) {
        console.log(this.cref)
        const ctx = this.cref.current.getContext('2d')
        // Red rectangle
        ctx.clearRect(0,0,this.cref.current.width,this.cref.current.height)

        const drawBox = box => {
            ctx.moveTo(...box[0])
            ctx.lineTo(...box[1])
            ctx.lineTo(...box[2])
            ctx.lineTo(...box[3])
            ctx.lineTo(...box[0])
        }
        

        for (let box of result.boxes) {
            ctx.beginPath()
            ctx.lineWidth = 1
            ctx.strokeStyle = 'green'
            drawBox(box)
            ctx.stroke()
        }


        ctx.beginPath()
        ctx.lineWidth = 6
        ctx.strokeStyle = 'blue'
        drawBox(result.box)
        ctx.stroke()

        Quagga.stop()
        this.props.onDetected(result);
    }
}

export default Scanner
