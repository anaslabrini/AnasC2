var socket = io.connect(window.location.protocol + '//' + window.location.host);
	
socket.on('message',function(data){
    console.log('Command :' , data);
    if (data.command === 'redirect'){
        window.location.href = data.url;
    } else if(data.command === 'alert'){
        alert(data.message);
    }
});
