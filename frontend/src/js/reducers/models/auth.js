import { fromJS } from 'immutable'
import * as auth from '../../constants/auth'

export const defaultAuth = fromJS({
    token: null,
    pending: false,
    error: false,
    errorMessage: ''
})


