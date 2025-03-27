"use strict";
const required = (value) => value ? null : "This field is needed";
const regex = (pattern, errorMessage) => (value) => pattern.test(value) ? null : errorMessage;
const minLength = (length) => (value) => value.length >= length ? null : '';
