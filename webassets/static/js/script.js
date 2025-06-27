import { quill, startAIStream, addMessage } from "./quill_editor.js";
const button = document.getElementsByClassName("button")[0];
// let first = false
// if (! first){
//     quill.insertText(quill.getLength()-1,"👤 : ",true)
//     first = true
// }
function GetText() {
  let editor = document.getElementById("editor");
  let content = editor.innerText.trim();
  // console.log(typeof(content));
  //   let content = quill.getText().trim();
  if (!content) return;
  addMessage(content, "user");
  quill.setText("");
  fetch("/process", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ user: content }),
  }).then((response) => {
    const reader = response.body.getReader();
    const decoder = new TextDecoder();

    async function read() {
      const aiStream = startAIStream();

      while (true) {
        const { done, value } = await reader.read();
        if (done) {
          console.log("streaming finished");
          aiStream.complete();
          break;
        }

        let chunk = decoder.decode(value, { stream: true });
        aiStream.appendChunk(chunk);
      }
    }
    read();
  });
}
button.addEventListener("click", GetText);
