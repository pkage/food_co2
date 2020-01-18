import React from 'react';
import { render } from 'react-dom';
import App from './components/App/App.js'

import '../css/custom.scss';

import { Provider } from 'react-redux'
import configureStore from './store'

export const store = configureStore()

render(
    <Provider store={store}>
        <App />
    </Provider>,
    document.getElementById('root')
);
