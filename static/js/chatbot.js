let botui = new BotUI('my-botui-app');
let usersName = "";
let container = $('.calc-height').height();
$('.botui-app-container').css('max-height', container);

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
                    botui.message.add({
                        delay: 2000,
                        loading: true,
                        content: "Sure, so we offer both subscription based websites and single websites, essentially a buy and collect service. Are you looking for a subscription based service?"
                    }).then(function newSiteOptions(){
                        botui.action.button({
                            action: [
                                {text: "Yes, I want a subscription", value: "y"},
                                {text: "No, I just want a single website", value: "n"},
                                {text: "I want more information on a subscription service", value: "moreInfo"}
                            ]
                        }).then(function(res){
                            if (res.value == "moreInfo"){
                                botui.message.add({
                                    delay: 2000,
                                    loading: true,
                                    content: "Our subscription is currently charged annually. Within our subscriptions we offer multiple perks, which allow our customers leave the heavy lifting to us completely. The perks of subscription services include: domain registration and upkeep, SSL certificates, web hosting, web design, graphic design, search engine optimization and more.",
                                }).then(function(){
                                    botui.message.add({
                                        delay: 2000,
                                        loading: true,
                                        content: "Manage My Web currently offer two different plans, 'Silver' and 'Gold'. These are designed to provide levels of support that cover different websites. You can view these plans by using the buttons below: (opens in new tab)"
                                    }).then(function(){
                                        botui.action.button({
                                            action: [
                                                {text: "Silver Package", value:"silver"},
                                                {text: "Gold Package", value:"gold"},
                                                {text: "Back To Options", value:"back"},
                                            ]
                                        }).then(function openSub(res){
                                            if (res.value == "silver"){
                                                // Url for silver pack
                                                let url = "/subscriptions";
                                                //window.open(url);
                                                botui.message.add({
                                                    content: "I will now open a new tab for you. If this is blocked by your browser, please enable popups and click 'Open Silver Subscription' below."
                                                }).then(function(){
                                                    botui.action.button({
                                                        action: [
                                                            {text: "Open Silver Subscription", value: "r"}
                                                        ]
                                                    }).then(function(res){
                                                        window.open(url);
                                                        standby();
                                                    })
                                                })
                                                standby();
                                            }else if (res.value == "gold"){
                                                // Url for gold pack
                                                let url = "";
                                                botui.message.add({
                                                    content: "I will now open a new tab for you. If this is blocked by your browser, please enable popups and click 'Open Gold Subscription' below."
                                                }).then(function(){
                                                    botui.action.button({
                                                        action: [
                                                            {text: "Open Gold Subscription", value: "r"}
                                                        ]
                                                    }).then(function(res){
                                                        window.open(url);
                                                        standby();
                                                    })
                                                })
                                                standby();
                                                window.open(url);
                                            }else if (res.value == "back"){
                                                newSiteOptions();
                                            }
                                        })
                                    })
                                })
                            }else if (res.value == "y"){
                                botui.message.add({
                                    delay: 2000,
                                    loading: true,
                                    content: "Our subscription based services are aimed to provide your website, with an entire IT department without the need to hire any internal staff. Although we will be the creators of your new website, you will retain all rights, and copyrights to this website."
                                }).then(function(){
                                    botui.message.add({
                                        delay: 2000,
                                        loading: true,
                                        content: "We currently offer two different packages, aimed at providing the perfect level of support regardless of website / business type."
                                    }).then(function newSubOptions(){
                                        botui.action.button({
                                            action: [
                                                {text: "Silver Package", value: "s"},
                                                {text: "Gold Package", value: "g"},
                                                {text: "Silver Package", value: "s"},
                                            ]
                                        }).then(function(res){
                                            if (res.value == "s"){
                                                botui.message.add({
                                                    delay: 2000,
                                                    loading: true,
                                                    content: "Our silver package is designed specifically to both individuals and businesses."
                                                }).then(function(){
                                                    botui.message.add({
                                                        delay: 2000,
                                                        loading: true,
                                                        content: "This subscription service will grant you access to our SEO and development teams throughout your subscription. This means all variations, SEO, hosting plans and more will be completely looked after for you. We understand that customers will want to participate in varying amounts, so, we can provide you with this service with minimal, or maximum input from you."
                                                    }).then(function(){
                                                        botui.message.add({
                                                            delay:2000,
                                                            loading: true,
                                                            content: "You can view the full details of this subscription plan, or contact us to find out more by clicking the links below:"
                                                        }).then(function(){
                                                            botui.action.button({
                                                                action : [
                                                                    {text: "View Silver Package", value: "v"},
                                                                    {text: "Contact Us", value: "c"},
                                                                    {text: "View Options", value: "o"},
                                                                ]
                                                            }).then(function(){
                                                                if (res.value == "o"){
                                                                    newSubOptions();
                                                                }else if (res.value == "v"){
                                                                    
                                                                    window.location("");
                                                                }else if (res.value == "c"){
                                                                    // Contact link
                                                                    window.location("");
                                                                }
                                                            })
                                                        })
                                                    })
                                                })
                                            }
                                        })
                                    })
                                })
                            }
                        })
                    })
                }
            });
        })
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
            content: "Are you looking for a 'one off' or subscription based service?"
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
                                botui.message.add({
                                    type: 'text',
                                    delay:2000,
                                    loading: true,
                                    content: "Please provide further information and we will contact you shortly."
                                }).then(function(){
                                    $('#chatFormContain').show();
                                })
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
                                        }else if (res.value == "n"){
                                            standby();
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
function pay(){
    botui.message.add({
        delay: 2000,
        loading: true,
        content: "Manage My Web currently uses Stripe for all payment processing."
    }).then(function(){
        botui.message.add({
            delay: 2000,
            loading: true,
            content: "We can facilitate other methods on an individual basis if needed. Would you like to know more about Stripe or our custom payments?"
        }).then(function(){
            botui.action.button({
                action:[
                    {value:"stripe", text: "Stripe Payments"},
                    {value:"custom", text: "Custom Payments"},
                ]
            }).then(function(res){
                if (res.value == "stripe"){
                    botui.message.add({
                        delay: 2000,
                        loading: true,
                        content: "Stripe is an global leader in online payment processing. They provide a secure & seamless user experience. More information on Stripe can be found at their website Stripe.com"
                    }).then(function(){
                        standby();
                    })
                }else if (res.value = "custom"){
                    botui.message.add({
                        delay: 2000,
                        loading: true,
                        content: "Our custom payments are dealt with on an individual basis. Although we do offer these payments in certain situations, we retain the right to refuse custom payment applications. Would you like to apply for a custom payment?"
                    }).then(function(){
                        botui.action.button({
                            action:[
                                {value:"yes", text:"Yes"},
                                {value:"no", text:"No"},
                            ]
                        }).then(function(res){
                            if (res.value == "yes"){
                                $('#chatFormContain').show();
                            }else{
                                options();
                            }
                        })
                    })
                }
            })
        })
    })
}
function refund(){
    botui.message.add({
        delay: 2000,
        loading: true,
        content: "For all refund requests, please fill out the form provided."
    }).then(function(){
        $('#chatFormContain').show();
    })
}
function aboutus(){
    botui.message.add({
        delay: 2000,
        loading: true,
        content: "Manage My Web is a web development team based in Dublin, Ireland. We offer various website services including design/development, search engine optimization and graphics."
    }).then(function(){
        botui.message.add({
            delay: 2000,
            loading: true,
            content: "Our team is made up of various departments which are experts in their respective fields. For more information on us, please visit our about page."
        }).then(function(){
            standby();
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
                {value: "website", text : "Website / Web Design" },
                {value: "pay", text : "Payments" },
                {value: "refund", text : "Refunds" },
                {value: "aboutus", text : "About Us" },
            ],
        }).then(function (result) { 
            i = result.value;
            if (i == "seo"){
                seo();
            }
            if (i == "website"){
                website();
            }
            if (i == "pay"){
                pay();
            }
            if (i == "refund"){
                refund();
            }
            if (i == "aboutus"){
                aboutus();
            }
        });
    })
}