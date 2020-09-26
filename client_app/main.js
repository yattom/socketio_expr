const io = require('socket.io-client');
const socket = io('http://localhost:5000/')
console.log('start');


socket.on('connect', () => {
    console.log('connected');
    socket.emit('join');
})

socket.on('joined', () => {
    console.log('joined');

    setInterval(sendMsg, 1000);
})

socket.on('msg received', () => {
    console.log('msg received');
})

function sendMsg() {
    console.log('sending msg...');
    socket.emit('msg', { data: 123456789 });
    console.log('finighed sending msg...');
}