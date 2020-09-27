const io = require('socket.io-client');
const socket = io('http://localhost:5000/', { transports: ['websocket'], upgrade: false })
// const socket = io('http://localhost:5000/')
console.log('start');

let seq = 1;

socket.on('connect', () => {
    console.log('connected');
    socket.emit('join');
})

socket.on('joined', () => {
    console.log('joined');

    setInterval(sendMsg, 10);
})

socket.on('msg received', () => {
    console.log('msg received');
})

function sendMsg() {
    console.log('sending msg...');
    socket.emit('msg', {
        timestamp: new Date().toLocaleString(),
        sequence: seq,
        data: 123456789
    });
    seq += 1;
    console.log('finished sending msg...');
}