import { fromJS } from 'immutable'
import * as scan from '../../constants/scan'

export const defaultScan = fromJS({
    response: scan.DEBUG_EXAMPLE_SCAN,
    responsePending: false,
    current: null
})

