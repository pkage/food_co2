import React, { useState } from 'react'
import { useDispatch, useSelector} from 'react-redux'
import { useLocation } from 'wouter'
import { requestLogin } from '../../actions/auth'

import './Login.css'

import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import CircularProgress from '@material-ui/core/CircularProgress';
import InputAdornment from '@material-ui/core/InputAdornment'
import AccountCircle from '@material-ui/icons/AccountCircle'

import { useLoginStatus } from '../../utils'

const Login = props => {
    // controlled form
    const [username, setUsername] = useState('')
    const [password, setPassword] = useState('')

    const [location, setLocation] = useLocation()
    const dispatch = useDispatch();

    const isPending = useSelector( state => state.auth.get('pending') )
    const error = useSelector( state => state.auth.get('error') )
    const errorMessage = useSelector( state => state.auth.get('errorMessage') )
    const loggedIn = useLoginStatus()

    if (loggedIn) {
        // TODO tweak to point elsewhere
        setLocation('/scan')
    }

    // submission helper
    const submit = e => {
        e.preventDefault()
        console.log(username, password)
        dispatch(requestLogin(username, password))
    }

    return (
        <div className="Login">
            {isPending ?
                <CircularProgress/> :
                <form className="Login__card" onSubmit={submit}>
                    {error && <div className="Login__error">{errorMessage}</div>}
                    <TextField
                        id="Login__username"
                        label="Username"
                        required
                        autoComplete="off"
                        value={username}
                        onChange={e => setUsername(e.target.value)}/>
                    <br/>
                    <TextField
                        id="Login__password"
                        label="Password"
                        required
                        type="password"
                        autoComplete="off"
                        value={password}
                        onChange={e => setPassword(e.target.value)}/>
                    <br/>
                    <Button variant="contained" color="primary" type="submit">
                        Login
                    </Button>
                </form>
            }
        </div>
    )
}

export default Login
