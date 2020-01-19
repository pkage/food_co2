import { put, takeEvery, takeLatest, all, delay } from "redux-saga/effects";
import * as scanActions from "../actions/scan";
import * as scanTypes from "../constants/scan";
import * as authActions from "../actions/auth";
import * as authTypes from "../constants/auth";

import { store } from "../index";

const url = "https://hackcambridge.findoslice.com"

/* --- DASHBOARD --- */

function* resolveDashboard(token=null) {
    const access_token = token || store.getState().scan.get('token')
    console.log('using token ' + access_token)

    const graph_data = yield fetch(url + "/api/user/daily", {
        headers: {
            Authorization: `JWT ${access_token}`
        },
        method: "GET"
    }).then(r => r.json());
    const entries_res = yield fetch(url + "/api/user/entries", {
        headers: {
            Authorization: `JWT ${access_token}`
        },
        method: "GET"
    }).then(r => r.json());

    yield put(
        scanActions.setDashboard({
            data: graph_data,
            entries: entries_res["entries"],
            products: entries_res["products"]
        })
    );
}

function* watchDashboard() {
    yield takeLatest(scanTypes.SCAN_GET_DASHBOARD, resolveDashboard);
}

/* --- LOOKUP FUNCTIONS --- */

function* scanLookupRequest(action) {
    yield put(scanActions.requestLookup());
    console.log(action);

    const access_token = store.getState().scan.get('token')

    const res = yield fetch(url + `/api/emissions/${action.code}?weight=${action.weight / 1000.0}`, {
        headers: {
            Authorization: `JWT ${access_token}`
        },
        method: "GET"
    }).then(r => r.json());

    yield put(scanActions.resolveLookup(res));
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
        res = null;
    }


    // TODO: replace with real login
    if (res !== null && res.status == 200) {
        // success
        const token = (yield res.json()).access_token
        yield resolveDashboard(token)
        yield put(authActions.loginSuccess(token));
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
    yield all([watchScanLookupRequests(), watchLoginRequests(), watchDashboard()]);
}
