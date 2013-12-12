var chatid = 0;

function getProfile(username) {
    if(username) {
    window.location = '/profile/' + username;
    }
}
function createChat() {
    var username = $('#owner').val();
    var chatbox = '<div class="chat_box main_chat'+chatid+'" id="chat_id '+ chatid + '">\
        <!--chat_box-->\
        <div class="user_box">\
            <div class="name open_chat1 left"> ' + username + '</div>\
            <div class="closed1 right">x &nbsp;</div>\
            <div class="clear"></div>\
        </div>\
        <div id ="wrapbox"class="wrap_box">\
        <div id="message_content" class="message_content">\
                <!--message_content-->\
                <div id="reply_output'+chatid+'">\
                </div>\
            </div>\
        </div>\
        <!--message_content-->\
            <div name="box_reply" class="box_reply">\
                <form id="reply" onsubmit="return sendMessage(text_reply'+chatid+',+'+chatid+');">\
                    <input type="text" id="text_reply'+chatid+'" name="text_reply'+chatid+'" class="text_reply'+chatid+'">\
                </form>\
            </div>\
        </div>';
    $('#chat_area').append(chatbox);

    chatid++;

}

function sendMessage(textbox, chatid) {
    var message = textbox.value;
    var messagebox = ' <div class=\"message_post\"><img src="http://www.globalwoodmart.my/_img/logo_peka.gif" width="35" class="left user_img">\
                        <div class="message_text left">' + message +'</div>\
                        <div class="clear"></div>\
                    </div>'
     $('#reply_output'+chatid).append(messagebox);
     textbox.value = ''

    return false;

     }
function receiveMessage() {
    var username = $('#username').value
    var url = '/message/'+ username
    $.ajax({
        url: url,
        data:username,
            complete: function() {
            setTimeout(receiveMessage(),1000);
        }
    })
}
//receiveMessage();
//createChat();


$(document).ready(function () {

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

