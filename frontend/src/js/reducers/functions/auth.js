import {
    fromJS
} from 'immutable'

import * as authTypes from '../../constants/auth'
import { defaultAuth } from '../models/auth'

class AuthReducer {
    /**
     * Request a login (sets pending)
     */
    static requestLogin(state, action) {
        return state.set('pending', true)
    }

    /**
     * unsuccessful login
     */
    static setFailure(state, action) {
        state = state.set('error', true)
        state = state.set('pending', false)
        return state.set('errorMessage', action.message)
    }

    /**
     * Clear the login
     */
    static clearLoginStatus(state, action) {
        state = state.set('error', false)
        return state.set('errorMessage', '')
    }

    /**
     * successful login
     */
    static setToken(state, action) {
        state = state.set('token', action.token)
        state = state.set('pending', false)
        return AuthReducer.clearLoginStatus(state, action)
    }
}

export default function scan(state=defaultAuth, action, opt_reducer=AuthReducer) {
    switch (action.type) {
        case authTypes.AUTH_LOGIN_REQUESTED:
            return opt_reducer.requestLogin(state, action)
        case authTypes.AUTH_LOGIN_SUCCESS:
            return opt_reducer.setToken(state, action)
        case authTypes.AUTH_LOGIN_FAILURE:
            return opt_reducer.setFailure(state, action)
        case authTypes.AUTH_LOGIN_CLEAR:
            return opt_reducer.clearLoginStatus(state, action)
        default:
            return state
    }
}

