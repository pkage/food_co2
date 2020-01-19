import React, {
    useState
} from 'react'
import './ScanPage.css'

import Button from '@material-ui/core/button'
import ScannerContainer from './ScannerContainer'
import TextField from '@material-ui/core/TextField';
//import Button from '@material-ui/core/Button';
import CircularProgress from '@material-ui/core/CircularProgress';
import Input from '@material-ui/core/Input';
import InputAdornment from '@material-ui/core/InputAdornment';
import FormHelperText from '@material-ui/core/FormHelperText';
import FormControl from '@material-ui/core/FormControl';

import { useAuthenticated } from '../../utils'

const ScanPage = props => {
    useAuthenticated()

    const [result, setResult] = useState(null)
    const [weight, setWeight] = useState(1)
    const submit = e => {
        e.preventDefault()
        console.log('submitting ', result, weight)
    }

    return (
        <div className="ScanPage">
            {(result === null) ?
                <div className="ScanPage__stage1">
                    <ScannerContainer onDetected={res => setResult(res)}/>
                </div> :
                <form className="ScanPage__stage2" onSubmit={submit}>
                    <FormControl>
                        <Input
                            id="standard-adornment-weight"
                            value={weight}
                            onChange={e => setWeight(e.target.weight)}
                            endAdornment={<InputAdornment position="end">g</InputAdornment>}
                        />
                        <FormHelperText id="standard-weight-helper-text">Weight</FormHelperText>
                    </FormControl>
                    <Button variant="contained" color="primary" type="submit">
                        Login
                    </Button>
                </form>
            }

        </div>
    )
}

export default ScanPage
