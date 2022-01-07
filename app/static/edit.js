var editButton = document.getElementsByClassName("edit");
for(let i = 0;i<editButton.length;i++){
    editButton[i].addEventListener('click',function (evt){
        post = evt.target.parentNode.parentNode.parentNode.nextElementSibling;
        let title = post.previousElementSibling.firstElementChild.lastElementChild
        let content = post.firstElementChild;
        let id = post.previousElementSibling.firstElementChild.firstElementChild
        title.setAttribute("contentEditable","true")
        content.setAttribute("contentEditable","true")
        button = document.createElement("button")
        button.innerText = "OK"
        button.classList.add("btn", "btn-danger")
        
        post.appendChild(button)
        button.addEventListener('click',function(){
            form = document.getElementById("edit-form");
            console.log(form)
            document.getElementById("edit-post-content").value = content.innerText;
            document.getElementById("edit-post-id").value = id.innerText
            document.getElementById("edit-post-title").value = title.innerText
            form.submit()
        })
        console.log(post);
    })
}