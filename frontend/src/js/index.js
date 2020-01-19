import React from 'react';
import { render } from 'react-dom';
import App from './components/App/App.js'

import '../css/base.css';

import { Provider } from 'react-redux'
import configureStore from './store'

import { createMuiTheme, makeStyles, ThemeProvider } from '@material-ui/core/styles'

const theme = createMuiTheme({
    palette: {
        primary: {
            main: '#244F26'
        },
        secondary: {
            main: '#424342'
        }
    }
});

export const store = configureStore()

render(
    <ThemeProvider theme={theme}>
        <Provider store={store}>
            <App />
        </Provider>
    </ThemeProvider>,
    document.getElementById('root')
);
