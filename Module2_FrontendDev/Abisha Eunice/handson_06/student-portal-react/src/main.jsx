import React from "react";
import ReactDOM from "react-dom/client";

import { BrowserRouter } from "react-router-dom";

import { Provider } from "react-redux";

import { EnrollmentProvider } from "./context/EnrollmentContext";

import store from "./redux/store";

import App from "./App";

import "./App.css";



ReactDOM.createRoot(document.getElementById("root")).render(

    <React.StrictMode>

        <Provider store={store}>

            <EnrollmentProvider>

                <BrowserRouter>

                    <App />

                </BrowserRouter>

            </EnrollmentProvider>

        </Provider>

    </React.StrictMode>

);