import * as scanTypes from '../constants/scan'

export const scanCode = code => ({
    type: scanTypes.SCAN_CODE_SCANNED,
    code
})

export const requestLookup = () => ({
    type: scanTypes.SCAN_LOOKUP_REQUESTED,
})

export const resolveLookup = response => ({
    type: scanTypes.SCAN_LOOKUP_RESOLVED,
    response
})
