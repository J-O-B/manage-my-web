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
            delay: 500,
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
                {text: "Return To Options", value: "c"}
            ]
            }).then(function (res) { 
                if (res.value == "c"){
                    options();
                }
                else if (res.value == "a"){
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
                                // User clicked products
                                botui.message.add({
                                    delay: 2000,
                                    loading: true,
                                    content: "Great, We offer various SEO products that are categorized into 'Reports', and 'Technical'."
                                }).then(function(){
                                    botui.message.add({
                                        delay: 4000,
                                        loading: true,
                                        content: "Reports are handmade website reports that contain materials on a websites health, linking profiles and more. Our technical SEO category includes products that are more hands on, where we will implement technical SEO on your websites markup language."
                                    }).then(function(){
                                        botui.message.add({
                                            delay: 5000,
                                            loading: true,
                                            content: "Which type of SEO products would you like to view today?"
                                        }).then(function(){
                                            botui.action.button({
                                                action: [
                                                    {text: "SEO Reports", value: "r"},
                                                    {text: "Technical", value: "t"}
                                                ]
                                            }).then(function (res) { 
                                                if (res.value == "r"){
                                                    botui.message.add({
                                                        content: "Redirecting to display SEO Report products."
                                                    })
                                                    standby();
                                                    let counter = 3;
                                                    setInterval(function() {
                                                        counter--;
                                                        if (counter === 0) {
                                                            clearInterval(counter);
                                                            window.location = "/products/12"
                                                        }
                                                    }, 1000);
                                                }
                                                else if (res.value == "t"){
                                                    botui.message.add({
                                                        content: "Redirecting to display Technical SEO products."
                                                    })
                                                    standby();
                                                    let counter = 3;
                                                    setInterval(function() {
                                                        counter--;
                                                        if (counter === 0) {
                                                            clearInterval(counter);
                                                            window.location = "/products/14"
                                                        }
                                                    }, 1000);
                                                }   
                                            });
                                        })

                                    })
                                })
                            }else{
                                // User clicked contact
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
                                botui.message.add({
                                    delay: 6000,
                                    loading: true,
                                    content: "Would you like to view more information on our subscription based SEO service?"
                                }).then(function(){
                                    botui.action.button({
                                        action: [
                                          {text: 'Yes', value: 'y'},
                                          {text: 'No', value: 'n'},
                                        ]
                                    }).then(function (res) { 
                                        if (res.value == "y"){
                                            botui.message.add({
                                                delay: 1000,
                                                loading: true,
                                                content: "Great, I will redirect you now to this service."
                                            }).then(function(){
                                                standby();
                                                let counter = 3;
                                                setInterval(function() {
                                                    counter--;
                                                    if (counter === 0) {
                                                        clearInterval(counter);
                                                        window.location = "/products/?category=report"
                                                    }
                                                }, 1000);
                                            })
                                        }
                                    });
                                })
                            })
                        })
                    })
                }
            });
        })
    })
}

function website(){
    botui.message.add({
        delay: 3000,
        loading: true,
        content: "Manage My Web offers a wide range of web design products so I will try my best to help you today."
    }).then(function(){
        botui.message.add({
            delay: 2000,
            loading: true,
            content: "Do you currently own a website, or are you looking to create a new website?"
        }).then(function(){
            botui.action.button({
                action: [
                    {
                        text: 'I already have a website',
                        value: 'a'
                    },
                    {
                        text: 'I want to build a new website',
                        value: 'b'
                    },
                ]
            }).then(function (res) {
                if (res.value == "a"){
                    botui.message.add({
                        delay: 2000,
                        loading: true,
                        content: "Ok, we can offer help with pre made websites but will need further information to proceed."
                    }).then(function(){
                        botui.action.text({
                            action: {
                                sub_type: 'email',
                                placeholder: 'Please enter your email'
                            }
                        }).then(function(res){
                            let email = res.value;
                            botui.message.add({
                                delay: 2000,
                                loading: true,
                                content: `Great, so just to confirm your name is ${usersName} and email is ${email}. Is this correct?`
                            }).then(function(){
                                botui.action.button({
                                    action: [
                                        {text: 'Yes',value: 'y'},
                                        {text: 'No',value: 'n'},
                                    ]
                                }).then(function (res) { 
                                    if (res.value == "y"){
                                        // Notify admin to contact user
                                    }else if (res.value == "n"){
                                        botui.message.add({
                                            delay: 2000,
                                            loading: true,
                                            content: "Please enter your email:"
                                        }).then(function(){
                                            botui.action.text({
                                                action: {
                                                    sub_type: "email",
                                                    placeholder: "Please enter your email"
                                                }
                                            }).then(function(res){
                                                email = res.value;
                                                botui.message.add({
                                                    delay: 2000,
                                                    loading: true,
                                                    content: "Please enter your name"
                                                }).then(function(){
                                                    botui.action.text({
                                                        action:{
                                                            placeholder: "Please enter your name"
                                                        }
                                                    }).then(function(res){
                                                        usersName = res.value;
                                                        botui.message.add({
                                                            content: `Ok ${usersName}, I am submitting your request now. Please do not refresh or close this chat. This browser window may refresh.`
                                                        })
                                                        let subject = "Website Request - Existing Website";
                                                        let name = usersName;
                                                        let emails = new String(email);
                                                        let data = ({"subject":subject,"name":name,"email":emails});
                                                        var json = JSON.stringify(data);
                                                        let url = `/about/chatbotHook/${json}/`;
                                                        $.post(url, json);
                                                        standby();
                                                    })
                                                })
                                            })
                                        })
                                    }
                                });
                            })
                        })
                    })
                }else if (res.value == "b"){

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