
//========================================================================
// Web page elements for functions to use
//========================================================================
var Rovercommand=document.getElementById("command")
var predResult2 = document.getElementById("predresult2");

//========================================================================
// Main button events
//========================================================================


function submit() {
   try{
var inputVal = "";
if (Rovercommand) {
    inputVal = Rovercommand.value;
}

  // call the predict function of the backend
     predict(inputVal,predResult2.innerHTML);
    // predResult.innerHTML=null;
  } catch (err) {
        txt = "There was an error on this page.\n\n";
        txt += "Error description: " + err.message + "\n\n";
        txt += "Click OK to continue.\n\n";
        alert(txt);
    }
}


//========================================================================
// ssending the values to the backend
//auto refresher using ajax to update the front end value for the position
//========================================================================
function predict( commands,predResult) {

var server_data = [
      {"commands": commands},
      {"position": predResult},
     ];

 $.ajax({
   type: "POST",
   url: "/mars",
   data: JSON.stringify(server_data),
   contentType: "application/json",
   dataType: 'json',
   success: function(data) {
   displayResult(data);
   }
 });
}

// update the rssult in the div tag
function displayResult(data) {

  predResult2.innerHTML = data.newResult;
}
