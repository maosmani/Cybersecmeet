

function myFunction() {
  /* Get the text field */
  var copyText = document.getElementById("myInput");

  /* Select the text field */
  copyText.select();
  copyText.setSelectionRange(0, 99999); /* For mobile devices */

  /* Copy the text inside the text field */
  document.execCommand("copy");

  /* Alert the copied text */
  alert("Copied zoom link: " + copyText.value);
}


        
<input type="text" class="form-control" name="myvalue"  id="myvalue" value="{{ meeting.zoom_url }}" readonly  />

     <button class="btn btn-primary btn-block" onclick="copyToClipboard()">Copy myvalue</button>
        </li>
    {% endfor %}
    </div>

<script >
   
function copyToClipboard() {
    var textBox = document.getElementById("myvalue");
    textBox.select();
    document.execCommand("copy");
}
 </script>