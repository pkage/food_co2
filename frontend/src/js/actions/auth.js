import * as authTypes from '../constants/auth'

export const requestLogin = (user, pass) => ({
    type: authTypes.AUTH_LOGIN_REQUESTED,
    user,
    pass
})

export const loginSuccess = token => ({
    type: authTypes.AUTH_LOGIN_SUCCESS,
    token
})

export const loginFailure = message => ({
    type: authTypes.AUTH_LOGIN_FAILURE,
    message
})

export const loginClear = () => ({
    type: authTypes.AUTH_LOGIN_CLEAR
})
