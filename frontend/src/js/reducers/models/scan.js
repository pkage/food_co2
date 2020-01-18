import { fromJS } from 'immutable'
import * as scan from '../../constants/scan'

export const defaultScan = fromJS({
    response: null,
    responsePending: false,
    current: null
})

