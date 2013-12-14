// Chat client code.

// Keep track of the last message received (to avoid receiving the same message several times).
// This global variable is updated every time a new message is received.
var success;
var timestamp = 0;
var id = 0;
var created = false;
var chatFound = false;
// URL to contact to get updates.
var url = null;

// How often to call updates (in milliseconds)
var CallInterval = 500;
// ID of the function called at regular intervals.
var IntervalID = 0;
var exisitingRoom = null;
// A callback function to be called to further process each response.
var prCallback = null;

function callServer(){
	// At each call to the server we pass data.
	$.get(url, // the url to call.
			{time: timestamp}, // the data to send in the GET request.
			function(payload) { // callback function to be called after the GET is completed.
							processResponse(payload);
							},
			'json');
	};
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function processResponse(payload) {
	// if no new messages, return.
	if(payload.status == 0) return;
	// Get the timestamp, store it in global variable to be passed to the server on next call.
	timestamp = payload.time;
	for(message in payload.messages) {
		$("#chatwindow").append(payload.messages[message].text);
	}
	// Scroll down if messages fill up the div.
	var objDiv = document.getElementById("chatwindow");
	objDiv.scrollTop = objDiv.scrollHeight;
	// Handle custom data (data other than messages).
	// This is only called if a callback function has been specified.
	if(prCallback != null) prCallback(payload);
}

//function createChat(owner, visitor) {
//    $.get('/chat/get_room/'+ owner+'/'+visitor,
//        function(data) {
//            if(data != '' && data[0].pk!=undefined) {
//                 InitChatWindow(data[0]);
//            }
//            else {
//                $.post('/chat/create/',{"owner":owner,"visitor":visitor },
//                    function(data) {
//                        if(data.status != 0){
//
//                            InitChatWindow(data[0]);
//                         }
//                     }
//
//                );
//            }
//        }
//    );
//
//}

function create(owner, visitor) {
    if(!chatFound) {
            $.post('/chat/create/',{"owner":owner,"visitor":visitor },
                    function(data) {
                        if(data.status != 0){

                            InitChatWindow(data[0]);
                         }
                     }

            );
    }

}

function checkChat(owner, visitor) {
    if(!created) {
         $.get('/chat/get_room/'+ owner+'/'+visitor,
            function(data) {
                if(data != '' && data[0].pk!=undefined) {
                 InitChatWindow(data[0]);
                }
                else {
                    checkChat(owner,visitor);
                }
            }

         );
    }


}

function InitChatWindow(room){
    document.getElementById('index_reload').style.display = 'block';
    document.getElementById('userChat').innerHTML = room.fields.name;

    created = true;
    chatFound = true;

/**   The args to provide are:
	- the URL to call for AJAX calls.
	- A callback function that handles any data in the JSON payload other than the basic messages.
	  For example, it is used in the example below to handle changes to the room's description. */

	$("#loading").remove(); // Remove the dummy 'loading' message.

	// Push the calling args into global variables so that they can be accessed from any function.
	url = '/chat/room/' + room.pk + '/ajax/';
	//prCallback = ProcessResponseCallback;

	// Read new messages from the server every X milliseconds.
	IntervalID = setInterval(callServer, CallInterval);

	// The above will trigger the first call only after X milliseconds; so we
	// manually trigger an immediate call.
	callServer();

	// Process messages input by the user & send them to the server.
	$("form#chatform").submit(function(){
		// If user clicks to send a message on a empty message box, then don't do anything.
		if($("#msg").val() == "") return false;

		// We don't want to post a call at the same time as the regular message update call,
		// so cancel that first.
		clearInterval(IntervalID);
            var csrf = getCookie('csrftoken');
		$.post(url,
				{
				time: timestamp,
				action: "postmsg",
				message: $("#msg").val(),
                csrfmiddlewaretoken:csrf
           		},
           		function(payload) {
         						$("#msg").val(""); // clean out contents of input field.
         						// Calls to the server always return the latest messages, so display them.
         						processResponse(payload);
       							},
       			'json'
       	);
       	
       	// Start calling the server again at regular intervals.
       	IntervalID = setInterval(callServer, CallInterval);
       	
		return false;
	});


} // End InitChatWindow

/**	This code below is an example of how to extend the chat system.
 * It's used in the second example chat window and allows us to manage a user-updatable
 * description field.
 *  */

// Callback function, processes extra data sent in server responses.
function HandleRoomDescription(payload) {
	$("#chatroom_description").text(payload.description);
}

function InitChatDescription(){

	$("form#chatroom_description_form").submit(function(){
		// If user clicks to send a message on a empty message box, then don't do anything.
		if($("#id_description").val() == "") return false;
		// We don't want to post a call at the same time as the regular message update call,
		// so cancel that first.
		clearInterval(IntervalID);
		$.post(url,
				{
				time: timestamp,
				action: "change_description",
				description: $("#id_description").val()
           		},
           		function(payload) {
         						$("#id_description").val(""); // clean out contents of input field.
         						// Calls to the server always return the latest messages, so display them.
         						processResponse(payload);
       							},
       			'json'
       	);
       	// Start calling the server again at regular intervals.
       	IntervalID = setInterval(callServer, CallInterval);
		return false;
	});

}

$(document).ready(function () {
if(visitor != null)
        checkChat(owner, visitor);
    //Dont worry about this script im using php to loop this is just temporary
    //Close
    $('.closed1').click(function () {
        $('.wrap_box1').hide();
        $('.main_chat1').addClass('hide_wrap_box');
    });

    //Open
    $('.open_chat1').click(function () {
        $('.wrap_box1').show();
        $('.main_chat1').removeClass('hide_wrap_box');
    });

    //Close
    $('.closed2').click(function () {
        $('.wrap_box2').hide();
        $('.main_chat2').addClass('hide_wrap_box');
    });

    //Open
    $('.open_chat2').click(function () {
        $('.wrap_box2').show();
        $('.main_chat2').removeClass('hide_wrap_box');
    });
});