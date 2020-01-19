import { put, takeEvery, takeLatest, all, delay } from 'redux-saga/effects'
import * as scanActions from '../actions/scan'
import * as scanTypes  from '../constants/scan'
import * as authActions from '../actions/auth'
import * as authTypes  from '../constants/auth'

import { store } from '../index'

/* --- LOOKUP FUNCTIONS --- */

function* scanLookupRequest(action) {
    const code = store.scan.get('current')

    yield delay(1500)

    yield put(scanActions.resolveLookup({
        key: 'value'
    }))
}

function* watchScanLookupRequests() {
    yield takeLatest(scanTypes.SCAN_LOOKUP_REQUESTED, scanLookupRequest)
}

/* --- LOGIN FUNCTIONS --- */

function* handleLoginRequests(action) {
    yield put(authActions.loginClear())

    yield delay(2000)

    // TODO: replace with real login
    if (false) {
        // success
        yield put(authActions.loginSuccess('foo'))
    } else {
        yield put(authActions.loginFailure('didn\'t work chief'))
        yield delay(5000)
        yield put(authActions.loginClear())
    }
}

function* watchLoginRequests() {
    yield takeLatest(authTypes.AUTH_LOGIN_REQUESTED, handleLoginRequests)
}


export default function* rootSaga() {
    yield all([
        watchScanLookupRequests(),
        watchLoginRequests()
    ])
}
