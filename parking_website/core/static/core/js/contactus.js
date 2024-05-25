// Initialize
// For design purpose only. To show indicator of where the user is. There are better ways!!!
const linkDiv = document.querySelector('.link-set-items');
const activeChild = linkDiv.querySelector('.active');
if (activeChild) {
    activeChild.classList.remove('active');
}

document.getElementById("contactUsLink-desktop").classList.add("active");
document.getElementById("contactUsLink-mobile").classList.add("active");

const id = document.getElementById("request-id").value;
const conversationUrl = `http://localhost:8000/chats/conversations/?id=${id}`
const mailBox = document.getElementById("mailbox");

const newConversationButton = document.getElementById("newConversationButton");

const mailPerPage = 7;
const paginationBar = document.getElementById("pagination-bar");

const readConversationModal = document.getElementById("readConversationModal")
const conversationBlock = document.getElementById("conversation-history")
const conversationTitle = document.getElementById("readConversationTitle")
const replyButton = document.getElementById("reply-button")

retrieveInboxForm(conversationUrl);
// Ending of initialization

// NEW CONVERSATION FORM
document.getElementById("newConversationForm").addEventListener('submit', function(e) {
    newConversationButton.disabled = true;
    newConversationButton.textContent = "Submitting...";
    e.preventDefault();

    // Disable button
    
    const url = 'http://localhost:8000/chats/new/';
    const newTopic = document.getElementById("new-topic");
    const newTopicBody = document.getElementById("new-topic-body");

    const data = {
        user: id,
        topic: newTopic.value,
        newtopicbody: newTopicBody.value
    };

    const options = {
        method: 'POST', // HTTP method
        headers: {
          'Content-Type': 'application/json' // Specify the content type
        },
        body: JSON.stringify(data) // Convert data to JSON string
    };
  
    fetch(url, options)
    .then(response => {
        if (!response.ok) {
        throw new Error('Network response was not ok ' + response.statusText);
            alert("Cannot process events now! Try again later.");
        }
        setTimeout(function() {
            newConversationButton.disabled = false;
            newConversationButton.textContent = "Submit";
        }, 1000);
        return response.json(); // Parse the JSON response
    })
    .then(data => {
        alert("Conversation created. Refresh your inbox!");
        newTopic.value = "";
        newTopicBody.value = "";
        $('#newConversationModal').modal('hide');
        retrieveInboxForm(`http://localhost:8000/chats/conversations/?id=${id}`);
    })
    .catch(error => {
        console.error('Error:', error); // Handle any errors
        alert("Cannot process events now! Try again later.");
    });

    
}
)

// Retrieve Inbox
async function retrieveInboxForm(url) {
    
    const data = await fetchData(url);

    if ("error" in data) {
        mailBox.innerHTML = ""
        // Cannot retrieve conversations
        
        let err_inbox_msg = document.createElement("h5");
        err_inbox_msg.classList.add('text-center', 'text-muted');
        err_inbox_msg.textContent = "Cannot retrieve messages. Please try again.";

        let err_msg_box = document.createElement("div");
        err_msg_box.appendChild(err_inbox_msg);

        mailBox.appendChild(err_msg_box)

        return
    }

    mailBox.innerHTML = ""; // Clear inbox
    let mails = data['results'];

    mails.forEach(mail => {
        console.log(mail)
        var m = createMail(mail['topic'], mail['latest_message'], mail['id'], mail['topic'])
        mailBox.appendChild(m);
    });

    // Then paginate
    var pages = Math.ceil(data['count']/mailPerPage);
    paginationBar.innerHTML = "";

    for (let i = 1; i<=pages; i++) {
        var p = createPageNumber(i, conversationUrl+`&page=${i}`);
        paginationBar.appendChild(p);
    }

}

// Create a mail
function createMail(topic, body, id, topic){
    let newMail = document.createElement("div");
    newMail.className = "mail";

    // Header
    let newMailHeader = document.createElement("div");
    newMailHeader.className = "mail-header";

    let headerButton = document.createElement("button");
    headerButton.setAttribute("type", "button");
    headerButton.setAttribute("data-toggle", "modal");
    headerButton.setAttribute("data-target", "#readConversationModal");
    headerButton.setAttribute("onclick", "openConversation('" + id + "','" + topic+"')")

    let topicName = document.createElement("h5");
    topicName.textContent = topic;

    let conversationId = document.createElement("input")
    conversationId.type="hidden";
    conversationId.value = id

    headerButton.appendChild(topicName);
    newMailHeader.appendChild(headerButton);
    newMailHeader.appendChild(conversationId)

    // Body
    let newMailBody = document.createElement("div");
    newMailBody.className = "mail-body";
    let mailContent = document.createElement("div")
    mailContent.className = "mail-content"

    let mailContentBody = document.createElement("p")
    mailContentBody.textContent = body;

    mailContent.appendChild(mailContentBody);
    newMailBody.appendChild(mailContent);

    newMail.appendChild(newMailHeader);
    newMail.appendChild(newMailBody);

    return newMail
}

// Create pagination bar
function createPageNumber(number, conversationUrl) {
    let page = document.createElement("li");
    page.className = "page-item";

    let button = document.createElement("button");
    button.className = "page-link";
    button.textContent = number;

    button.setAttribute("onclick", "retrieveInboxForm('" + conversationUrl + "')")

    page.appendChild(button);
    
    return page
}

// Make a get request
async function fetchData(url) {
    try {
        // Options for the fetch request
        const options = {
            method: 'GET', // Specifies that the request is a GET request
            headers: {
                'Content-Type': 'application/json' // Sets the content type to JSON
            }
        };

        const response = await fetch(url, options);

        if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
        }

        const data = await response.json();
        return data;

    } catch (err) {
        return {
            error:err.message
        }
    }   
}

async function openConversation(conversation_id, topic) {
    let row = conversationBlock.children[0].children[0];
    row.innerHTML = ""
    conversationTitle.innerText = topic;

    // For sending replies
    var form = document.getElementById('reply-form');
    form.addEventListener('submit', function(e){
        e.preventDefault();
        replyButton.disabled = true;
        replyButton.innerText = "Sending...";

        // Get reply
        const reply = document.getElementById("reply-msg");
        let body_msg = reply.value;
        const url = 'http://localhost:8000/chats/conversations/messages/create/';
        
        const data = {
            body: body_msg,
            sender: id,
            conversation: conversation_id
        };

        reply.value = ""

        const options = {
            method: 'POST', // HTTP method
            headers: {
              'Content-Type': 'application/json' // Specify the content type
            },
            body: JSON.stringify(data) // Convert data to JSON string
        };

        fetch(url, options)
        .then(response => {
            if (!response.ok) {
            throw new Error('Network response was not ok ' + response.statusText);
                alert("Cannot process events now! Try again later.");
            }
            
            return response.json(); // Parse the JSON response
        })
        .then(data => {
            console.log(data)
            // Post it now
            let msg = myMessage(data['body'], data['created_at'])
            row.prepend(msg)
            
        })
        .catch(error => {
            console.error('Error:', error); // Handle any errors
            let error_msg = myMessage("Connect process events now! Try again later.")
            row.prepend(error_msg)
            alert("Cannot process events now! Try again later.");
        });

        setTimeout(function() {
            replyButton.disabled = false;
            replyButton.innerText = "Reply";
        }, 1000);


    })

    // Set the chat history
    let url = `http://localhost:8000/chats/conversations/messages/${conversation_id}/`
    const data = await fetchData(url);
    const results = data['results']
    
    results.forEach(result =>{
        // Check owner
        var msg;
        if (result['sender'] == id) {
            msg = myMessage(result['body'], result['created_at']);
        } else {
            msg = otherMessage(result['body'], result['created_at']);
        }

        row.append(msg);
    });

    scrollToBottom();
}

// Template for messages sent by user
function myMessage(message, datetime) {
    let msg_block = document.createElement("div");
    msg_block.classList.add('col-12', 'mt-1', 'mb-1', 'd-flex', 'justify-content-end')

    let msg_container = document.createElement("div");
    msg_container.classList.add('alert', 'alert-success', 'text-end', 'conversation-message');
    msg_container.setAttribute('role', "alert");

    let msg = document.createElement("p");
    msg.textContent = message;

    let dt = document.createElement("p");
    dt.classList.add('small', 'text-muted')
    dt.textContent = convertDateTime(datetime)

    msg_container.appendChild(msg)
    msg_container.appendChild(dt)
    msg_block.appendChild(msg_container);

    return msg_block
}

// Template for messages sent by Others
function otherMessage(message,datetime) {
    let msg_block = document.createElement("div");
    msg_block.classList.add('col-12', 'mt-1', 'mb-1')

    let msg_container = document.createElement("div");
    msg_container.classList.add('alert', 'alert-dark', 'conversation-message');
    msg_container.setAttribute('role', "alert");

    let msg = document.createElement("p");
    msg.textContent = message;

    let dt = document.createElement("p");
    dt.classList.add('small', 'text-muted')
    dt.textContent = convertDateTime(datetime)

    msg_container.appendChild(msg)
    msg_container.appendChild(dt)
    msg_block.appendChild(msg_container);

    return msg_block
}

function convertDateTime(date) {
    const dt = new Date(date);
    const options = {
        year: 'numeric',
        month: 'long',
        day: 'numeric',
        hour: '2-digit',
        minute: '2-digit',
        second: '2-digit',
        hour12: true
    };

    return dt.toLocaleString('en-US', options);

}

function scrollToBottom() {
    const modalElement = document.getElementById("readConversationModal");
    const modalBody = modalElement.querySelector('.modal-body');

    modalBody.scrollTop = modalBody.scrollHeight;
}
