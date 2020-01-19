import * as scanTypes from '../constants/scan'

export const scanCode = (code, weight) => ({
    type: scanTypes.SCAN_CODE_SCANNED,
    code,
    weight
})

export const requestLookup = () => ({
    type: scanTypes.SCAN_LOOKUP_REQUESTED,
})

export const resolveLookup = response => ({
    type: scanTypes.SCAN_LOOKUP_RESOLVED,
    response
})

export const getDashboard = () => ({
    type: scanTypes.getDashboard
})

export const setDashboard = data => ({
    type: scanTypes.setDashboard,
    data
})
