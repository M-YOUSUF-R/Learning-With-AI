import quill from "./quill_editor.js";
const button = document.getElementsByClassName('button')[0]
let first = false
if (! first){
    quill.insertText(quill.getLength()-1,"👤 : ",true)
    first = true
}
function GetText() {
    // let editor = document.getElementsByClassName("editor")[0]
    // let content = editor.innerText;
    // console.log(typeof(content));
    let content = quill.getText()
    let lines =  content.split('\n')
    let last_line = lines[lines.length - 2]
    console.log(last_line)

    fetch("/process", {
        method: "POST",
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ 'user': last_line })
    })
    .then(response => {
        const reader = response.body.getReader()
        const decoder = new TextDecoder()

        async function read(){
            quill.insertText(quill.getLength()-1,"\n🥸 : ",true)
            while(true){
                const {done,value} = await reader.read()
                if(done){
                    console.log("streaming finished")
                    break;
                }
                let chunk = decoder.decode(value,{stream:true})
                // console.log(typeof(chunk))
                // content += chunk
                
                quill.insertText(quill.getLength()-1,chunk,true)
                
            }
            quill.insertText(quill.getLength()-1,"\n👤 : ",true)
        }
        read()
    })
}
button.addEventListener("click", GetText)