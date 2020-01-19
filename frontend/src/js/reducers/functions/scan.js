import {
    fromJS
} from 'immutable'

import * as scanTypes from '../../constants/scan'
import { defaultScan } from '../models/scan'

class ScanReducer {
    /**
     * Scan a code (processed from barcode reader)
     */
    static scanCode(state, action) {
        return state.set('current', fromJS({code: action.code, weight: action.weight}))
    }

    /**
     * Show that a request is pending
     */
    static requestLookup(state, action) {
        return state.set('responsePending', true)
    }

    /**
     * Set the server response
     */
    static resolveLookup(state, action) {
        state = state.set('responsePending', false)
        return state.set('response', fromJS(action.response))
    }
}

export default function scan(state=defaultScan, action, opt_reducer=ScanReducer) {
    switch (action.type) {
        case scanTypes.SCAN_CODE_SCANNED:
            return opt_reducer.scanCode(state, action)
        case scanTypes.SCAN_LOOKUP_REQUESTED:
            return opt_reducer.requestLookup(state, action)
        case scanTypes.SCAN_LOOKUP_RESOLVED:
            return opt_reducer.resolveLookup(state, action)
        default:
            return state
    }
}
