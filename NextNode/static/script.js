function scrollToLatest() {
  var response_msgContainer = document.getElementById("response_msg");

  if (response_msgContainer.children.length > 0) {
    var lastMessage = response_msgContainer.lastElementChild;
    response_msgContainer.scrollTop = response_msgContainer.scrollHeight;
    lastMessage.scrollIntoView({
      behavior: "smooth",
    });
    
  }
}

$(document).ready(function () {
  var socket = io.connect();

  socket.on('message', function (message) {
    $('#response_msg').append($('<p>').text(message));
    scrollToLatest();
  });

  $('form#req_from').submit(function (e) {
    e.preventDefault();
    var message = $('#message-input').val();
    socket.emit('message', message);
    $('#message-input').value('');
    scrollToLatest();
    textarea.value = "";
    textarea.scrollTop = 0;
  });
});

var textarea = document.getElementById("message-input");

textarea.onkeydown = function (event) {
  if (event.keyCode == 13 && event.shiftKey) {
    textarea.insertNewLine();
  } else if (event.keyCode == 13) {

    var button = document.getElementById("request");
    event.preventDefault();

    button.click()
    textarea.value = "";
    textarea.scrollTop = 0;
  }
};