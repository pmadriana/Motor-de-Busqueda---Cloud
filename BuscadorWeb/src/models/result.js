const mongoose = require('mongoose');
const db = require('../database')
const {Schema} = mongoose;

const ResultSchema = new Schema({
    title: {type: String, required: true},
    rank: {type: Number, required: true},
});

module.exports = mongoose.model('result', ResultSchema);

