import { fromJS } from 'immutable'
import * as auth from '../../constants/auth'

export const defaultAuth = fromJS({
    token: 'DUMMY_TOKEN',
    pending: false,
    error: false,
    errorMessage: ''
})


