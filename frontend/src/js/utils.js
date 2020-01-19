import {
    useSelector
} from 'react-redux'
import {
    useLocation
} from 'wouter'

export const useLoginStatus = () => {
    return useSelector( state => state.auth.get('token') !== null )
}

export const useAuthenticated = () => {
    const [location, setLocation] = useLocation()
    const loggedIn = useLoginStatus()
    console.log('login: ', loggedIn)

    if (!loggedIn && location !== '/') {
        setLocation('/')
    }
}

