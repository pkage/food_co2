import { put, takeEvery, takeLatest, all, delay } from "redux-saga/effects";
import * as scanActions from "../actions/scan";
import * as scanTypes from "../constants/scan";
import * as authActions from "../actions/auth";
import * as authTypes from "../constants/auth";

import { store } from "../index";

const url = "http://127.0.0.1:5000";

/* --- DASHBOARD --- */

function* resolveDashboard () {
    // TODO...
    yield put(scanActions.setDashboard({}))
}

function* watchDashboard() {
    yield takeLatest(scanTypes.SCAN_GET_DASHBOARD, resolveDashboard);
}

/* --- LOOKUP FUNCTIONS --- */

function* scanLookupRequest(action) {
    yield put(scanActions.requestLookup())
    console.log(action)

    yield delay(1500);

    yield put(
        scanActions.resolveLookup( scanTypes.DEBUG_EXAMPLE_SCAN )
    );
}

function* watchScanLookupRequests() {
    yield takeLatest(scanTypes.SCAN_CODE_SCANNED, scanLookupRequest);
}

/* --- LOGIN FUNCTIONS --- */

function* handleLoginRequests(action) {
    yield put(authActions.loginClear());

    let res;
    try {
        res = yield fetch(url + "/auth", {
            method: "POST",
            body: JSON.stringify({
                username: action.user,
                password: action.pass
            }),
            headers: {
                "Content-Type": "application/json"
            }
        });
        console.log(res);
    } catch (e) {
        res = null
    }

    yield resolveDashboard()

    // TODO: replace with real login
    if (res !== null && res.status == 200) {
        // success
        yield put(authActions.loginSuccess(res.json().access_token));
    } else {
        yield put(authActions.loginFailure("didn't work chief"));
        yield delay(5000);
        yield put(authActions.loginClear());
    }
}

function* watchLoginRequests() {
    yield takeLatest(authTypes.AUTH_LOGIN_REQUESTED, handleLoginRequests);
}

export default function* rootSaga() {
    yield all([watchScanLookupRequests(), watchLoginRequests()]);
}
