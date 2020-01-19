import {
    useSelector
} from 'react-redux'
import {
    useLocation
} from 'wouter'

export const useAuthenticated = () => {
    const [location, setLocation] = useLocation()
    const authToken               = useSelector( state => state.auth.get('token') )

    if (authToken === null && location !== '/') {
        setLocation('/')
    }
}

