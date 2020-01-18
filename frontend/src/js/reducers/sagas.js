import { put, takeEvery, takeLatest, all, call } from 'redux-saga/effects'
import * as scanActions from '../actions/scan'
import * as scanTypes  from '../constants/scan'

import { store } from '../index'

function* scanLookupRequest(action) {
    const code = store.scan.current

    yield delay(1500)

    yield put(scanActions.resolveLookup({
        key: 'value'
    }))
}

function* watchScanLookupRequests() {
    return takeLatest(scanTypes.SCAN_LOOKUP_REQUESTED, scanLookupRequest)
}


export default function* rootSaga() {
    yield all([
        watchScanLookupRequests
    ])
}
