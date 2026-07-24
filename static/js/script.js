document.addEventListener("DOMContentLoaded",()=>{

    const form=document.querySelector("form");

    const button=document.querySelector("button");

    form.addEventListener("submit",()=>{

        button.innerHTML="Analyzing Resume...";

        button.disabled=true;

    });

});