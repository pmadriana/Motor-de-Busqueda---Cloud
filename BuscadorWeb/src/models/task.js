const mongoose = require('mongoose');
const db = require('../database')
const {Schema} = mongoose;

const TaskSchema = new Schema({
    word: {type: String, required: true, index:true},
    papers: {type: Array, required: true},
},
{
    collection: 'indexs'
}
);

module.exports = mongoose.model('index', TaskSchema);


