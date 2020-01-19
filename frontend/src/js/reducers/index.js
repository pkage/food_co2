import { combineReducers } from 'redux';
import scan from './functions/scan'
import auth from './functions/auth'

const rootReducer = combineReducers({
    scan,
    auth
})

export default rootReducer
