let botui = new BotUI('my-botui-app');
let usersName = "";
let container = $('.calc-height').height();
$('.botui-app-container').css('max-height', container);
function init(){
    botui.message.add({
        loading: true,
        delay: 3000,
        content: 'Hello! Welcome to the Manage My Web helper chat. Who am I speaking with?'
    }).then(function () { 
        botui.action.text({
            loading: true,
            delay: 3000,
            action: {
                placeholder: 'Please enter your name here.'
            }
        }).then(function(res){
            usersName = res.value; 
            botui.message.add({
                loading: true,
                delay: 3000,
                content: `Great! Thanks for speaking with us today ${usersName}.`
            }).then(function(){
                options();
            })
        })
    });
}
init();
function options(){
    botui.message.add({
        loading: true,
        delay: 2000,
        content: "To assist you further, which section would you like further help with?"
    }).then(function(){
        botui.action.button({
            action: [
                {value: "seo", text : "SEO" },
                {value: "ws", text : "Website / Web Design" },
                {value: "pay", text : "Payments" },
                {value: "re", text : "Refunds" },
                {value: "au", text : "About Us" },
            ],
        }).then(function (res) { 
            i = res.value;
            if (i == "seo"){
                seo();
            } else if (i = "ws"){
                website();
            }else if (i = "pay"){
                pay();
            }else if (i = "re"){
                refund();
            }else if (i = "au"){
                about();
            }
        });
    })
}
function seo(){
    botui.message.add({
        delay: 2000,
        loading: true,
        content: "We offer a range of SEO products and services."
    }).then(function(){
        botui.message.add({
            delay: 2000,
            loading: true,
            content: "Are you looking for a 'one off' or subscription based service today " + usersName + "."
        }).then(function(){
        botui.action.button({
            action: [
                {text: 'One Time SEO', value: 'a'},
                {text: 'Subscription Based SEO', value: 'b'},
            ]
            }).then(function (res) { 
                if (res.value == "a"){
                    let product = `<a href='{% url "products" %}' target="_blank">products page</a>`;
                    botui.message.add({
                        type: 'text',
                        delay: 2000,
                        loading: true,
                        content: `No Problem, we offer several once off SEO packages which can be found in our products page. Alternatively you can contact us on Admin@ManageMyWeb.org, or use the contact form located on the contact page. I have added links to these sections below.`
                    }).then(function(){
                        botui.action.button({
                            action: [
                                {text:"Products", value:"prod"},
                                {text:"Contact Us", value:"contact"},
                            ]
                        }).then(function(res){
                            if (res.value == "prod"){
                                window.location = "/products";
                            }else{
                                window.location = "/products";
                            }
                        })
                    })
                }else if (res.value == "b"){
                    botui.message.add({
                        delay: 2000,
                        loading: true,
                        content: "Great! Manage My Web currently offers a single, fixed price solution to subscription based SEO."
                    }).then(function(){
                        botui.message.add({
                            delay: 3000,
                            loading: true,
                            content: "Our service at this time is tied in for one year, meaning we charge an upfront fee for our service."
                        }).then(function(){
                            botui.message.add({
                                delay: 6000,
                                loading: true,
                                content: "After purchasing our subscription SEO. We will arrange through a call, or emails to get started working with your website. As a subscription customer, you will have unparalleled access to our team allowing for fast, valuable updates to your website."
                            }).then(function(){
                                standby();
                            })
                        })
                    })
                }
            });
        })
    })
}
function standby(){
    botui.action.button({
        action:[
            {value:"y", text: "Restart Chat"}
        ]
    }).then(function(res){
        if (res.value == "y"){
            options();
        }
    })
}